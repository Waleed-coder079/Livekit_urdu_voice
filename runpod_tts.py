import base64
from runpod_client import call_runpod_async  # make sure to use async version

class RunPodTTS:
    async def synthesize(self, text: str) -> bytes:
        # Payload MUST be a dict
        payload = {"text": text}

        # Call async RunPod API
        result = await call_runpod_async("tts", payload)  # <- async function

        # Get audio_base64
        audio_b64 = result.get("audio_b64")
        if not audio_b64:
            raise ValueError("No audio returned from RunPod TTS")

        return base64.b64decode(audio_b64)
