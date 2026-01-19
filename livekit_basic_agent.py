import io
import asyncio
import base64
import torch
import torchaudio
import numpy as np
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
        # Generate audio bytes from RunPodTTS
        audio_bytes = await session.tts.synthesize(text)

        # Load WAV bytes into tensor
        waveform, sample_rate = torchaudio.load(io.BytesIO(audio_bytes))

        # Convert to float32 numpy
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
        for start in range(0, num_samples, frame_size):
            end = min(start + frame_size, num_samples)
            frame = waveform[:, start:end]
            await session.send_audio_frame(frame, sample_rate=sample_rate)

    except Exception as e:
        print(f"[TTS Error] {e} | text={text[:50]}")

# --------------------------
# Main LiveKit entrypoint
# --------------------------
async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
    stt=RunPodSTT(),
    llm=RunPodLLM(),
    tts=RunPodTTS(),
    vad=silero.VAD.load(),
)




    await session.start(
        room=ctx.room,
        agent=Assistant()
    )

    await session.generate_reply(
        instructions="صارف کو خوش دلی سے اردو میں سلام کریں اور پوچھیں کہ آپ کس طرح مدد کر سکتے ہیں۔"
    )

# --------------------------
# Run as CLI worker
# --------------------------
if __name__ == "__main__":
    agents.cli.run_app(
        agents.WorkerOptions(entrypoint_fnc=entrypoint)
    )
