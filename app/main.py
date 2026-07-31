"""
DocuMind AI — Main Application
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.config import get_settings
from app.core.logger import app_logger

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    app_logger.info(f"🚀 {settings.app_name} v{settings.app_version} starting...")
    app_logger.info(f"   LLM: {'Ollama (local)' if settings.use_ollama else 'Groq (cloud)'}")
    app_logger.info(f"   Docs: http://{settings.host}:{settings.port}/docs")
    yield
    # Shutdown
    app_logger.info("👋 Shutting down...")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI Engineer project — RAG, Agent, Streaming, MLOps",
    lifespan=lifespan,
)

# CORS (buat development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# === Health Check ===
@app.get("/", tags=["Health"])
async def root():
    return {
        "app": settings.app_name,
        "version": settings.app_version,
        "status": "running",
    }


@app.get("/health", tags=["Health"])
async def health():
    return {"status": "ok"}


# === Router placeholder (akan diisi per modul) ===
# from app.api import rag, agent, chat
# app.include_router(rag.router, prefix="/rag", tags=["RAG"])
# app.include_router(agent.router, prefix="/agent", tags=["Agent"])
# app.include_router(chat.router, prefix="/chat", tags=["Chat"])
