# 🧠 DocuMind AI

Project AI Engineer — **100% free tools**, cover semua requirement loker PT. All Data International.

## 🗂️ Struktur Project

```
documind/
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── core/
│   │   ├── config.py        # Semua config via .env
│   │   ├── logger.py        # Logging setup (loguru)
│   │   └── llm_factory.py   # Groq / Ollama abstraction
│   ├── rag/                 # RAG pipeline (next)
│   ├── agents/              # LangGraph agents (next)
│   ├── api/                 # FastAPI routers (next)
│   └── utils/               # Helper functions (next)
├── data/
│   ├── raw/                 # File upload masuk sini
│   ├── processed/           # Hasil chunking
│   └── vectorstore/         # ChromaDB persist
├── logs/
│   ├── app.log              # Application logs
│   └── mlflow/              # MLflow tracking
├── tests/
├── .env.example
├── requirements.txt
└── Makefile
```

## 🛠️ Tech Stack (Semua Gratis)

| Komponen | Tool | Keterangan |
|---|---|---|
| LLM | Groq API | Free tier, 6000 req/day |
| LLM On-prem | Ollama | Local, unlimited |
| Agent | LangGraph | Multi-step reasoning |
| RAG | LangChain + LlamaIndex | Pipeline lengkap |
| Vector DB | ChromaDB | Local, gratis |
| Embedding | sentence-transformers | Local CPU |
| API | FastAPI | Production-ready |
| Monitoring | MLflow | Local tracking |
| Caching | diskcache | Persistent cache |

## 🚀 Quick Start

```bash
# 1. Clone / masuk folder
cd documind

# 2. Install dependencies
make install

# 3. Setup environment
make setup-env
# → edit .env, isi GROQ_API_KEY

# 4. Jalankan server
make dev

# 5. Buka docs
# http://localhost:8000/docs
```

## 📋 Roadmap

- [x] Setup & struktur project
- [ ] RAG Pipeline (chunking, embedding, retrieval)
- [ ] LangGraph Agent (multi-step, tool calling)
- [ ] FastAPI endpoints (streaming, rate limit, fallback)
- [ ] Klasifikasi & Summarization
- [ ] MLflow monitoring
- [ ] Deploy ke HuggingFace Spaces / Railway

## 🔑 Cara Dapat Groq API Key (Gratis)

1. Buka https://console.groq.com
2. Sign up (bisa pakai Google)
3. Create API Key
4. Copy ke `.env` → `GROQ_API_KEY=...`
