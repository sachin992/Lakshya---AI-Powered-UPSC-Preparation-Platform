# Lakshya Migration: React + FastAPI + LangChain + LangGraph

This migration keeps the same business modules from the original app:
- Authentication (signup/login)
- UPSC GPT (chat + PDF RAG)
- Test Generator (Prelims/Mains)
- Mains Evaluator
- Current Affairs
- UPSC Puzzle
- Dashboard

## New Structure

- backend/: FastAPI API server with SQLAlchemy + LangChain + LangGraph
- frontend/: React (Vite) client
- existing Streamlit files are untouched

## 1) Run Backend

```bash
cd backend
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
copy .env.example .env
# Set OPENAI_API_KEY in .env
uvicorn app.main:app --reload --port 8000
```

## 2) Run Frontend

```bash
cd frontend
npm install
# optional: set VITE_API_BASE in .env to http://127.0.0.1:8000/api/v1
npm run dev
```

## 3) One-Command Docker Startup (Frontend + Backend + Reverse Proxy)

From project root:

```bash
# Create docker env file
copy .env.docker.example .env

# Build and start all services
docker compose up --build -d
```

Open in browser:

```text
http://localhost
```

Useful commands:

```bash
# View logs
docker compose logs -f

# Stop stack
docker compose down

# Stop and remove volume (resets backend sqlite data)
docker compose down -v
```

Services in Docker setup:

- `reverse-proxy` (Nginx): public entrypoint on port `80`
- `frontend` (React static build served by Nginx)
- `backend` (FastAPI on internal port `8000`)

Routing in Docker setup:

- `/` -> frontend
- `/api/*` -> backend

## API Overview

- POST /api/v1/auth/register
- POST /api/v1/auth/login
- GET /api/v1/auth/me
- POST /api/v1/upsc-gpt/chat
- POST /api/v1/upsc-gpt/upload?thread_id=...
- POST /api/v1/upsc-gpt/feedback
- POST /api/v1/tests/generate
- POST /api/v1/tests/submit
- GET /api/v1/tests/history
- POST /api/v1/mains/upload?thread_id=...
- POST /api/v1/mains/evaluate
- GET /api/v1/current-affairs
- POST /api/v1/puzzle/init
- POST /api/v1/puzzle/question
- POST /api/v1/puzzle/score
- GET /api/v1/dashboard

## Notes

- Current affairs service currently uses sample records and is API-ready for live source integration.
- Dashboard is now connected to persisted test attempts.
- Puzzle grid generation is deterministic using a seed to avoid rerun reshuffle.
- Password hashing upgraded to bcrypt.
