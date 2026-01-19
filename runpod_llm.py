from runpod_client import call_runpod
from knowledge_base import format_kb_for_llm, get_kb_summary

class RunPodLLM:
    async def generate(self, prompt: str) -> str:
        # Add knowledge base context to the prompt
        kb_context = format_kb_for_llm(prompt)
        
        # Enhance the prompt with KB information
        enhanced_prompt = f"""
آپ ایک اردو ٹیلیفونی ایسسٹنٹ ہیں جو سی ایم پنجاب آسان کاروبار فنانس اسکیم کے بارے میں معلومات فراہم کرتے ہیں۔

{kb_context}

صارف کا سوال: {prompt}

براہ کرم اردو میں واضح اور مفید جواب دیں۔
"""
        
        result = await call_runpod("llm", {"prompt": enhanced_prompt})
        return result.get("response", "")
