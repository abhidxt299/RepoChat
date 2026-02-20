# RepoChat 🤖

Chat with any public GitHub repository. Generate docs, analyze code quality, and ask questions — all powered by Claude AI and RAG.

## Features

- 💬 **Chat** — Ask questions about any part of the codebase. Gets relevant code via semantic search.
- 📄 **Docs** — Auto-generate markdown documentation for any file or the whole repo.
- 🔍 **Analyze** — Scan for bugs, code smells, security issues, and improvement suggestions.
- 📁 **File browser** — Browse indexed files with filtering.
- ⚡ **Streaming** — Chat responses stream in real-time.
- 🧠 **RAG** — ChromaDB + sentence-transformers for semantic retrieval. Scales to large repos.

## Tech Stack

| Layer | Tech |
|-------|------|
| Frontend | React + Vite + Tailwind |
| Backend | FastAPI (Python) |
| AI | Claude claude-sonnet-4-6 (Anthropic) |
| Embeddings | `all-MiniLM-L6-v2` (sentence-transformers) |
| Vector DB | ChromaDB (in-memory) |
| Repo Ingestion | GitHub REST API |
| Deployment | Docker + Compose |

## Quick Start (Local)

### Prerequisites
- Docker & Docker Compose
- An [Anthropic API key](https://console.anthropic.com)
- (Optional) [GitHub token](https://github.com/settings/tokens) for higher rate limits

### 1. Clone & configure
```bash
git clone <this-repo>
cd repo-chat
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### 2. Run
```bash
docker compose up --build
```

Frontend: http://localhost:3000  
Backend API: http://localhost:8000  
API Docs: http://localhost:8000/docs

## Local Dev (without Docker)

### Backend
```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # fill in your keys
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Deploying to Railway

1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Add two services: `backend` and `frontend` (pointing to respective subdirectories)
4. Set env vars: `ANTHROPIC_API_KEY`, `GITHUB_TOKEN`
5. Deploy!

## Deploying to Render

1. Create two Web Services on [render.com](https://render.com):
   - **Backend**: Root dir `backend`, build `pip install -r requirements.txt`, start `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Frontend**: Root dir `frontend`, build `npm install && npm run build`, serve `dist/`
2. Set env vars on backend service
3. Update `VITE_API_URL` on frontend to point to backend URL if needed

## Deploying to Fly.io

```bash
# Backend
cd backend
fly launch
fly secrets set ANTHROPIC_API_KEY=xxx GITHUB_TOKEN=xxx
fly deploy

# Frontend
cd ../frontend
fly launch
fly deploy
```

## API Reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/ingest` | POST | Ingest a public GitHub repo |
| `/api/chat` | POST | Chat with the codebase (SSE stream) |
| `/api/docs` | POST | Generate documentation |
| `/api/analyze` | POST | Analyze code quality |
| `/api/files/{repo_url}` | GET | List indexed files |
| `/health` | GET | Health check |

Full interactive docs at `/docs` (Swagger UI).

## Limitations & Roadmap

**Current limitations:**
- Repo state is in-memory (resets on restart) — swap ChromaDB for persistent storage for production
- Max 300 files, 100KB per file indexed
- No auth layer

**Roadmap:**
- [ ] Persistent vector store (Supabase pgvector, Pinecone)
- [ ] Auth (GitHub OAuth)
- [ ] Share indexed repos between users
- [ ] File-level chat with line references
- [ ] Diff analysis (PR review mode)
- [ ] Export docs to PDF/Word

## License

MIT