# LLM Reliability & Safety Monitor

This project is a production-style observability setup for an LLM-powered application using the Gemini API, built to explore how reliability issues can be detected, monitored, and handled in real time.

The goal was not just to build an app, but to treat the LLM like a real backend dependency and apply SRE-style monitoring, incident response, and dashboards around it.

---

## What this project does

- Exposes a FastAPI backend that sends prompts to the Gemini API
- Instruments the service using Datadog APM
- Tracks latency, request volume, and error behavior
- Detects abnormal LLM behavior using monitors
- Simulates traffic and failure scenarios
- Declares and manages incidents inside Datadog

This mirrors how LLMs would be monitored in a real production system.

---

## Architecture Overview

- **FastAPI** backend
- **Gemini API** for text generation
- **Datadog APM & Metrics** for observability
- **Traffic generator** to simulate load and bad requests
- **Datadog dashboards, monitors, and incidents**

Flow:
Client → FastAPI → Gemini API

---

**Datadog APM → Monitors → Incident**
## Key Features

### 1. Latency Monitoring
- p95 latency tracking for the LLM-backed endpoint
- Detects slow responses caused by large prompts or upstream latency

### 2. Error Rate Monitoring
- Tracks HTTP and application-level errors
- Flags abnormal error spikes

### 3. LLM Duration Visibility
- Separates FastAPI handling time from Gemini API time
- Helps identify whether slowness is internal or upstream

### 4. Incident Response
- Monitors trigger Datadog incidents
- Incident timeline includes shared graphs and notes
- Manual declaration used to demonstrate incident workflows

---

## Dashboards

The main dashboard includes:
- Request count
- p95 latency
- Error rate
- Monitor status summary
- LLM call duration

These widgets provide a single operational view of LLM health.

---

## Traffic Simulation

`traffic_generator.py` is used to:
- Send normal requests
- Send oversized or noisy prompts
- Create observable latency spikes

This helps validate that monitors and dashboards behave as expected.

---

## Datadog Configuration

Datadog assets are exported and stored under:
datadog/

This includes:
- Dashboard JSON
- Monitor definitions

---

## Running the project locally

1. Create and activate a virtual environment
2. Install dependencies:

pip install -r requirements.txt
3. Set environment variables:

GEMINI_API_KEY= your_gemini_api_key
DD_SERVICE=llm-reliability-monitor
DD_ENV=dev

4. Run the server:
ddtrace-run uvicorn app.main:app --reload

5. (Optional) Run traffic generator in another terminal:


---

## Notes

- `.env` and `venv/` are intentionally excluded from version control
- The incident shown in screenshots was manually declared for demonstration
- This project focuses on observability patterns, not model quality

---

## Why this matters

As LLMs move into production systems, treating them like black boxes is risky. This project shows how standard reliability practices—monitoring, alerting, and incident response—can be applied to AI systems in a practical way.

