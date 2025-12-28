# app/gemini.py

import os
import time
from dotenv import load_dotenv
from google import genai
from ddtrace import tracer

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY not found")

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-2.5-flash"


def ask_gemini(prompt: str) -> dict:
    start_time = time.time()

    with tracer.trace(
        "gemini.generate",
        service="llm-reliability-monitor",
        resource=MODEL_NAME,
        span_type="llm",
    ) as span:

        span.set_tag("llm.provider", "google")
        span.set_tag("llm.model", MODEL_NAME)
        span.set_tag("llm.prompt_length", len(prompt))

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt, 
        )

        latency = time.time() - start_time

        span.set_tag("llm.latency_seconds", round(latency, 3))
        span.set_tag("llm.output_length", len(response.text))

    return {
        "text": response.text,
        "latency_seconds": round(latency, 3),
        "model": MODEL_NAME,
    }
