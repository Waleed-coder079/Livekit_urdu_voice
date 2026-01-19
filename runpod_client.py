# runpod_client.py
import os
import time
import requests
import httpx
import asyncio
from typing import Any, Optional

# ===============================
# CONFIG
# ===============================

API_KEY = os.getenv("URDU_API_KEY")
ENDPOINT_ID = os.getenv("RUNPOD_ENDPOINT_ID")

RUN_URL = f"https://api.runpod.ai/v2/{ENDPOINT_ID}/run"
STATUS_URL = f"https://api.runpod.ai/v2/{ENDPOINT_ID}/status"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

# ===============================
# HELPERS
# ===============================

def _clean_dict(d: dict) -> dict:
    """
    Remove None and NotGiven values (LiveKit/OpenAI compatibility).
    """
    clean = {}
    for k, v in d.items():
        if v is None:
            continue
        if "NotGiven" in str(type(v)):
            continue
        clean[k] = v
    return clean

# ===============================
# STATUS POLLING
# ===============================

def wait_for_result_sync(job_id: str, timeout: int = 300) -> Optional[dict]:
    """
    Poll RunPod synchronously until job is completed or fails.
    """
    start = time.time()

    while time.time() - start < timeout:
        try:
            resp = requests.get(f"{STATUS_URL}/{job_id}", headers=HEADERS, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            status = data.get("status")

            if status == "COMPLETED":
                return data.get("output")

            if status == "FAILED":
                raise RuntimeError(f"RunPod job failed: {data}")

        except requests.exceptions.RequestException as e:
            print("[Polling warning]", e)

        time.sleep(2)

    raise TimeoutError("RunPod job timed out")

async def wait_for_result_async(job_id: str, timeout: int = 300) -> Optional[dict]:
    """
    Async polling for LiveKit compatibility.
    """
    start = time.time()
    async with httpx.AsyncClient(timeout=120) as client:
        while time.time() - start < timeout:
            resp = await client.get(f"{STATUS_URL}/{job_id}", headers=HEADERS)
            resp.raise_for_status()
            data = resp.json()
            status = data.get("status")

            if status == "COMPLETED":
                return data.get("output")

            if status == "FAILED":
                raise RuntimeError(f"RunPod job failed: {data}")

            await asyncio.sleep(1)

    raise TimeoutError("RunPod job timed out")

# ===============================
# RUNPOD CALLS
# ===============================

def call_runpod_sync(payload: dict, timeout: int = 300) -> Optional[dict]:
    """
    Sync call to RunPod endpoint with polling for result.
    """
    payload = _clean_dict(payload)
    body = {"input": payload}

    try:
        resp = requests.post(RUN_URL, json=body, headers=HEADERS, timeout=120)
        resp.raise_for_status()
        job = resp.json()

        job_id = job.get("id")
        if not job_id:
            raise RuntimeError(f"Invalid RunPod response: {job}")

        return wait_for_result_sync(job_id, timeout)

    except requests.RequestException as e:
        print(f"[RunPod sync error] {e}")
        return None

async def call_runpod_async(payload: dict, timeout: int = 300) -> Optional[dict]:
    """
    Async call to RunPod endpoint with polling for result.
    """
    payload = _clean_dict(payload)
    body = {"input": payload}

    try:
        async with httpx.AsyncClient(timeout=120) as client:
            resp = await client.post(RUN_URL, json=body, headers=HEADERS)
            resp.raise_for_status()
            job = resp.json()

        job_id = job.get("id")
        if not job_id:
            raise RuntimeError(f"Invalid RunPod response: {job}")

        return await wait_for_result_async(job_id, timeout)

    except Exception as e:
        print(f"[Async failed → fallback sync] {e}")
        return call_runpod_sync(payload, timeout)

# ===============================
# BACKWARD COMPATIBILITY
# ===============================

# Default alias for async usage
call_runpod = call_runpod_async
