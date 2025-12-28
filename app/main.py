# app/main.py

import time

# 🔹 Datadog: force patching BEFORE app starts
from ddtrace import patch_all
import ddtrace

patch_all()
ddtrace.config.service = "llm-reliability-monitor"

from fastapi import FastAPI
from pydantic import BaseModel
from app.gemini import ask_gemini

app = FastAPI(title="LLM Reliability Monitor")

class Prompt(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "LLM Reliability Monitor running"}

@app.post("/ask")
def ask(prompt: Prompt):
    start_time = time.time()

    result = ask_gemini(prompt.text)

    latency = time.time() - start_time

    return {
        "response": result["text"],
        "latency_seconds": latency,
        "model": result["model"],
        "status": "success"
    }
