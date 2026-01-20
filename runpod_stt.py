# runpod_stt.py

import base64
import time
from livekit.agents.stt import STT, STTCapabilities, SpeechEvent
from typing import NamedTuple
from runpod_client import stt_sync

class Alternative(NamedTuple):
    """Direct mapping from RunPod response; attributes optional."""
    text: str
    confidence: float = None
    language: str = None
    speaker_id: str = None

class RunPodSTT(STT):
    """
    RunPod STT adapter for LiveKit agents.
    Passes the response from RunPod directly without forcing values.
    """

    def __init__(self):
        super().__init__(
            capabilities=STTCapabilities(streaming=False, interim_results=False)
        )

    async def _recognize_impl(self, audio_frame, language="ur", **kwargs):
        try:
            start_total = time.time()

            # Convert frame to WAV bytes
            start_conv = time.time()
            wav_bytes = audio_frame.to_wav_bytes()
            end_conv = time.time()

            # Encode as base64
            audio_b64 = base64.b64encode(wav_bytes).decode("utf-8")

            # Call RunPod STT
            start_call = time.time()
            result = stt_sync(audio_b64)
            end_call = time.time()

            # Extract the first alternative (like your test code)
            alternatives = []
            if result and "alternatives" in result:
                for alt in result["alternatives"]:
                    alternatives.append(
                        Alternative(
                            text=alt.get("text", "").strip(),
                            confidence=alt.get("confidence"),
                            language=alt.get("language"),
                            speaker_id=alt.get("speaker_id")
                        )
                    )

            if not alternatives:
                alternatives.append(Alternative(text=""))

            end_total = time.time()
            print(f"[STT LOG] Conversion: {end_conv - start_conv:.2f}s, "
                  f"RunPod call: {end_call - start_call:.2f}s, "
                  f"Total: {end_total - start_total:.2f}s, "
                  f"Text='{alternatives[0].text[:50]}'")

            return SpeechEvent(type="final", alternatives=alternatives)

        except Exception as e:
            print(f"[STT ERROR] {e}")
            # fallback empty alternative
            return SpeechEvent(type="final", alternatives=[Alternative(text="")])
