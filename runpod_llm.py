import time
from unittest import result
from click import prompt
from runpod_client import llm_async
from knowledge_base import format_kb_for_llm

class RunPodLLM:
    async def generate(self, prompt: str) -> str:
        import time
        kb_context = format_kb_for_llm(prompt)
        enhanced_prompt = f"""
آپ ایک اردو ٹیلیفونی ایسسٹنٹ ہیں جو سی ایم پنجاب آسان کاروبار فنانس اسکیم کے بارے میں معلومات فراہم کرتے ہیں۔

{kb_context}

صارف کا سوال: {prompt}

براہ کرم اردو میں واضح اور مفید جواب دیں۔
"""
        start = time.time()
        result = await llm_async(enhanced_prompt)
        end = time.time()
    
        response_text = result.get("response", "")
        print(f"[LLM LOG] Prompt length={len(enhanced_prompt)} | "
              f"Response length={len(response_text)} | "
              f"Duration={end-start:.2f}s")
        return response_text

