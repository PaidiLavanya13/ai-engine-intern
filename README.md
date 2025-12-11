# Mini Workflow Engine — Code Review Agent

## Overview
Small workflow/graph engine implemented with FastAPI. Supports:
- Nodes: async Python functions operating on shared state
- Edges + branching (via state["next"]) + simple looping
- In-memory graph & run storage
- Example workflow: Code Review Mini-Agent (rule-based)

## Run locally
1. Create and activate venv:
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

2. Install:
   pip install -r requirements.txt

3. Start server:
   uvicorn app.main:app --reload --port 8000

4. Open docs:
   http://127.0.0.1:8000/docs

## API
- POST /graph/create  -> {"preset":"code_review"} -> returns graph_id
- POST /graph/run     -> {"graph_id":"<id>", "initial_state": {...}} -> returns run_id
- GET /graph/state/{run_id}

## What to improve
- Persist runs to DB, WebSocket logs, unit tests
