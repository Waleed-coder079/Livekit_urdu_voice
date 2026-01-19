from runpod_client import call_runpod

class RunPodLLM:
    async def generate(self, prompt: str) -> str:
        result = await call_runpod("llm", {"prompt": prompt})
        return result.get("response", "")
