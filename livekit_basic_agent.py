import io
import asyncio
import base64
import torch
import torchaudio
import numpy as np
import time
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession
from livekit.plugins import silero

from runpod_stt import RunPodSTT
from runpod_llm import RunPodLLM
from runpod_tts import RunPodTTS

load_dotenv(".env")

# --------------------------
# Define your Assistant
# --------------------------
class Assistant(Agent):
    def __init__(self):
        super().__init__(
            instructions="آپ ایک مددگار اور خوش اخلاق اردو وائس اسسٹنٹ ہیں۔"
        )

# --------------------------
# Helper to play TTS via LiveKit
# --------------------------
async def play_tts(session: AgentSession, text: str):
    try:
        start_total = time.time()
        # Generate audio bytes from RunPodTTS
        start_tts = time.time()
        audio_bytes = await session.tts.synthesize(text)
        end_tts = time.time()
        
        print(f"[TTS LOG] Text length={len(text)} | Audio bytes={len(audio_bytes)} | TTS duration={end_tts-start_tts:.2f}s")
        
        # Load WAV bytes into tensor
        waveform, sample_rate = torchaudio.load(io.BytesIO(audio_bytes))
        waveform = waveform.numpy()

        # Resample if needed to match LiveKit (assume 24000 Hz)
        if sample_rate != 24000:
            waveform = torchaudio.functional.resample(
                torch.tensor(waveform, dtype=torch.float32),
                orig_freq=sample_rate,
                new_freq=24000
            ).numpy()
            sample_rate = 24000

        # Ensure mono
        if waveform.shape[0] > 1:
            waveform = waveform.mean(axis=0, keepdims=True)

        # Send audio frame-by-frame
        frame_size = 1024
        num_samples = waveform.shape[1]
        start_send = time.time()
        for start in range(0, num_samples, frame_size):
            end = min(start + frame_size, num_samples)
            frame = waveform[:, start:end]
            await session.send_audio_frame(frame, sample_rate=sample_rate)
        end_send = time.time()
        
        print(f"[TTS LOG] Frame sending completed | Duration={end_send-start_send:.2f}s | Total TTS+Send={end_send-start_total:.2f}s")

    except Exception as e:
        print(f"[TTS ERROR] {e} | text={text[:50]}")

# --------------------------
# Main LiveKit entrypoint
# --------------------------
async def entrypoint(ctx: agents.JobContext):
    start_session = time.time()
    session = AgentSession(
        stt=RunPodSTT(),
        llm=RunPodLLM(),
        tts=RunPodTTS(),
        vad=silero.VAD.load(),
    )
    end_init = time.time()
    print(f"[SESSION LOG] AgentSession initialized | Duration={end_init-start_session:.2f}s")

    start_start = time.time()
    await session.start(
        room=ctx.room,
        agent=Assistant()
    )
    end_start = time.time()
    print(f"[SESSION LOG] Session started in room '{ctx.room}' | Duration={end_start-start_start:.2f}s")

    # Full roundtrip reply generation timing
    start_reply = time.time()
    await session.generate_reply(
        instructions="صارف کو خوش دلی سے اردو میں سلام کریں اور پوچھیں کہ آپ کس طرح مدد کر سکتے ہیں۔"
    )
    end_reply = time.time()
    print(f"[SESSION LOG] Full reply generation | Duration={end_reply-start_reply:.2f}s | Total session time={end_reply-start_session:.2f}s")

# --------------------------
# Run as CLI worker
# --------------------------
if __name__ == "__main__":
    agents.cli.run_app(
        agents.WorkerOptions(entrypoint_fnc=entrypoint)
    )
