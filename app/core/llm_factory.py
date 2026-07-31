"""
LLM Factory — abstraksi provider LLM.

Cara kerja:
- use_ollama=False  → pakai Groq (cloud, free tier)
- use_ollama=True   → pakai Ollama (local, on-prem)

Tinggal ganti config, kode lain nggak perlu diubah.
"""

from langchain_core.language_models import BaseChatModel
from app.core.config import get_settings
from app.core.logger import app_logger

settings = get_settings()


def get_llm(
    temperature: float = 0.1,
    streaming: bool = False,
) -> BaseChatModel:
    """
    Return LLM sesuai config.
    
    Args:
        temperature: 0.0 = deterministik, 1.0 = kreatif
        streaming: aktifkan streaming response
    """
    if settings.use_ollama:
        return _get_ollama(temperature, streaming)
    return _get_groq(temperature, streaming)


def _get_groq(temperature: float, streaming: bool) -> BaseChatModel:
    from langchain_groq import ChatGroq

    app_logger.info(f"Using Groq | model: {settings.groq_model}")
    return ChatGroq(
        api_key=settings.groq_api_key,
        model=settings.groq_model,
        temperature=temperature,
        streaming=streaming,
        # Fallback otomatis kalau rate limit kena
        max_retries=3,
    )


def _get_ollama(temperature: float, streaming: bool) -> BaseChatModel:
    from langchain_community.chat_models import ChatOllama

    app_logger.info(f"Using Ollama (local) | model: {settings.ollama_model}")
    return ChatOllama(
        base_url=settings.ollama_base_url,
        model=settings.ollama_model,
        temperature=temperature,
        streaming=streaming,
    )


def get_embedding_model():
    """Return embedding model — jalan local, gratis."""
    from langchain_huggingface import HuggingFaceEmbeddings

    app_logger.info(f"Loading embedding: {settings.embedding_model}")
    return HuggingFaceEmbeddings(
        model_name=settings.embedding_model,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )
