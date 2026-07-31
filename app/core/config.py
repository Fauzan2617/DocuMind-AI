from pydantic_settings import BaseSettings
from pydantic import Field
from functools import lru_cache


class Settings(BaseSettings):
    # App
    app_name: str = "DocuMind AI"
    app_version: str = "0.1.0"
    debug: bool = True
    log_level: str = "INFO"

    # LLM — Groq (primary, free tier)
    groq_api_key: str = ""
    groq_model: str = "llama-3.1-8b-instant"

    # LLM — Ollama (optional, local)
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.1"
    use_ollama: bool = False  # set True kalau mau pakai local

    # Embedding (local, gratis)
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"

    # Vector DB
    chroma_persist_dir: str = "./data/vectorstore"

    # API
    host: str = "0.0.0.0"
    port: int = 8000
    max_upload_size_mb: int = 10

    # Caching
    cache_ttl_seconds: int = 300
    cache_max_size: int = 100

    # MLflow
    mlflow_tracking_uri: str = "./logs/mlflow"
    mlflow_experiment_name: str = "documind-experiments"

    # Rate Limiting
    rate_limit_per_minute: int = 20

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
