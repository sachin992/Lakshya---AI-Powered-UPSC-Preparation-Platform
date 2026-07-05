# Lakshya - AI Powered UPSC Preparation Platform

Lakshya is an AI-enabled UPSC preparation platform with a React frontend and a FastAPI backend. It includes authentication, UPSC GPT chat, test generation, mains evaluation, current affairs, a puzzle module, and a performance dashboard.

## Architecture

- Frontend: React + Vite
- Backend: FastAPI + SQLAlchemy
- AI Layer: LangChain + LangGraph + OpenAI
- Vector Search: FAISS
- Database: SQLite
- Deployment: Docker Compose + Nginx reverse proxy

## Features

1. Authentication
- User registration and login
- JWT token-based auth
- Password hashing and profile fields (attempt, commitment)

2. UPSC GPT
- UPSC-focused AI chat
- Optional PDF upload for context
- RAG-enabled answering from uploaded documents

3. Test Generator
- Prelims and Mains test generation
- Source mode options (mock/PYQ/mixed)
- Current affairs toggle and language selection
- Test submission and history persistence

4. Mains Evaluator
- Upload answer PDF
- AI-based qualitative feedback with examiner-style suggestions

5. Current Affairs
- API-backed list and filtering interface
- Designed for live feed integration (currently sample records)

6. UPSC Puzzle
- Grid-based gamified module
- Deterministic puzzle initialization and scoring APIs

7. Dashboard
- Test count, average score, and accuracy from saved attempts

## Project Structure

- backend: FastAPI app, services, schemas, API routes, requirements
- frontend: React app with routed pages and API integration
- docker: Nginx reverse proxy config
- docker-compose.yml: Full stack orchestration

## Environment Setup

Create root env file for Docker Compose:

1. Copy example:
- copy .env.docker.example .env

2. Set required key:
- OPENAI_API_KEY=your_openai_api_key

Optional variables:
- OPENAI_MODEL=gpt-4o-mini
- EMBEDDING_MODEL=text-embedding-3-small
- SECRET_KEY=replace-with-strong-secret
- ALLOWED_ORIGINS=http://localhost,http://127.0.0.1

## Run with Docker (Recommended)

1. Start stack:
- docker compose up --build -d

2. Open app:
- http://localhost

3. API base:
- http://localhost/api/v1

4. Stop stack:
- docker compose down

## Run without Docker

Backend:
1. cd backend
2. python -m venv .venv
3. .venv\Scripts\activate
4. pip install -r requirements.txt
5. copy .env.example .env
6. uvicorn app.main:app --reload --port 8000

Frontend:
1. cd frontend
2. npm install
3. npm run dev

## Notes

- If OPENAI_API_KEY is missing, AI endpoints will return a configuration error.
- Auth and database routes still work without OpenAI key.
- For full migration and deployment details, see MIGRATION_REACT_FASTAPI.md.
