import os
import requests
import httpx
import asyncio
from typing import Any, Optional

# ===============================
# CONFIG
# ===============================

ENDPOINT_ID = os.getenv("RUNPOD_ENDPOINT_ID")
BASE_URL = f"https://umin480jkz1koq-8000.proxy.runpod.net"

HEADERS = {
    "Content-Type": "application/json",
}

# ===============================
# SYNC CLIENT
# ===============================

def call_runpod_sync(endpoint: str, payload: dict) -> dict:
    """Call RunPod endpoint synchronously (direct HTTP POST)"""
    url = f"{BASE_URL}/{endpoint}"
    
    try:
        response = requests.post(
            url,
            json=payload,
            headers=HEADERS,
            timeout=300
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error calling {endpoint}: {str(e)}")
        return {}

# ===============================
# ASYNC CLIENT
# ===============================

async def call_runpod_async(endpoint: str, payload: dict) -> dict:
    """Call RunPod endpoint asynchronously (direct HTTP POST)"""
    url = f"{BASE_URL}/{endpoint}"
    
    try:
        async with httpx.AsyncClient(timeout=300) as client:
            response = await client.post(
                url,
                json=payload,
                headers=HEADERS
            )
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"Async error calling {endpoint}: {str(e)}")
        # Fallback to sync
        return call_runpod_sync(endpoint, payload)

# ===============================
# STT CALLS
# ===============================

async def stt_async(audio_b64: str) -> dict:
    """Call STT endpoint with base64 audio"""
    return await call_runpod_async("stt", {"audio_b64": audio_b64})

def stt_sync(audio_b64: str) -> dict:
    """Call STT endpoint synchronously"""
    return call_runpod_sync("stt", {"audio_b64": audio_b64})

# ===============================
# LLM CALLS
# ===============================

async def llm_async(text: str) -> dict:
    """Call LLM endpoint with text (changed from 'prompt' to 'text')"""
    return await call_runpod_async("llm", {"text": text})

def llm_sync(text: str) -> dict:
    """Call LLM endpoint synchronously"""
    return call_runpod_sync("llm", {"text": text})

# ===============================
# TTS CALLS
# ===============================

async def tts_async(text: str) -> dict:
    """Call TTS endpoint with text"""
    return await call_runpod_async("tts", {"text": text})

def tts_sync(text: str) -> dict:
    """Call TTS endpoint synchronously"""
    return call_runpod_sync("tts", {"text": text})
