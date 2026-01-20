#runpod_tts
import base64
from pydoc import text
from time import time
from runpod_client import tts_async

class RunPodTTS:
    async def synthesize(self, text: str) -> bytes:
        import time
        start = time.time()
        result = await tts_async(text)
        end = time.time()
    
        audio_b64 = result.get("audio_b64")
        if not audio_b64:
            raise ValueError("No audio returned from RunPod TTS")
    
        print(f"[TTS LOG] Text length={len(text)} | Audio bytes={len(audio_b64)} | Duration={end-start:.2f}s")
        return base64.b64decode(audio_b64)
