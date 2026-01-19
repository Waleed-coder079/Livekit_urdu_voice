import base64
import io
import wave
from livekit.agents.stt import STT, STTCapabilities, SpeechEvent
import requests
import os
import tempfile
from typing import NamedTuple
from runpod_client import call_runpod_sync


class Alternative(NamedTuple):
    """Simple alternative for SpeechEvent."""
    text: str


class RunPodSTT(STT):
    """
    RunPod STT adapter for LiveKit agents.
    """

    def __init__(self):
        super().__init__(
            capabilities=STTCapabilities(streaming=False, interim_results=False)
        )

    async def _recognize_impl(self, audio_frame, language="ur", **kwargs):
        """Process audio frame and send to RunPod for transcription."""
        try:
            # Convert frame to WAV bytes
            wav_bytes = audio_frame.to_wav_bytes()
            
            # Encode as base64
            audio_b64 = base64.b64encode(wav_bytes).decode("utf-8")
            
            # Call RunPod using existing client
            result = call_runpod_sync({"audio_b64": audio_b64, "language": language})
            
            if result:
                text = result.get("text", "").strip()
                if text:
                    return SpeechEvent(type="final", alternatives=[Alternative(text=text)])
            
        except Exception as e:
            print(f"STT Error: {e}")

        return SpeechEvent(type="final", alternatives=[Alternative(text="")])

