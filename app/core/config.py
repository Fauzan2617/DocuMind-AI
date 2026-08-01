from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Kelas konfigurasi utama aplikasi menggunakan Pydantic.

    Secara otomatis membaca variabel dari environment file (.env) jika
    tersedia.
    """

    # --- Konfigurasi Aplikasi ---
    app_name: str = "DocuMind AI"  # Nama aplikasi
    app_version: str = "0.1.0"  # Versi aplikasi
    debug: bool = True  # Mode debug (True untuk pengembangan)
    log_level: str = "INFO"  # Tingkat detail pencatatan log (DEBUG, INFO, WARNING, ERROR)

    # --- Konfigurasi LLM Utama (Groq) ---
    groq_api_key: str = ""  # API key untuk layanan Groq Cloud (diisi via .env)
    groq_model: str = (
        "llama-3.1-8b-instant"  # Model LLM default yang digunakan di Groq
    )

    # --- Konfigurasi LLM Opsional (Ollama - Lokal) ---
    ollama_base_url: str = (
        "http://localhost:11434"  # URL server lokal Ollama
    )
    ollama_model: str = "llama3.1"  # Nama model lokal Ollama
    use_ollama: bool = False  # Flag untuk mengaktifkan LLM lokal (set True jika ingin pakai Ollama)

    # --- Konfigurasi Model Embedding ---
    embedding_model: str = (
        "sentence-transformers/all-MiniLM-L6-v2"  # Model HuggingFace untuk merubah teks jadi vektor
    )

    # --- Konfigurasi Vector Database ---
    chroma_persist_dir: str = (
        "./data/vectorstore"  # Folder penyimpanan data database vektor (ChromaDB)
    )

    # --- Konfigurasi Server API (FastAPI/Uvicorn) ---
    host: str = "0.0.0.0"  # IP address untuk bind server (0.0.0.0 agar bisa diakses eksternal)
    port: int = 8000  # Port berjalan server
    max_upload_size_mb: int = (
        10  # Batas maksimum ukuran file dokumen yang diunggah (dalam MB)
    )

    # --- Konfigurasi Caching ---
    cache_ttl_seconds: int = 300  # Waktu simpan cache dalam detik (Time-To-Live, 300s = 5 menit)
    cache_max_size: int = 100  # Jumlah maksimum entri data yang disimpan di cache

    # --- Konfigurasi MLflow (Pencatatan Eksperimen & Evaluasi Model) ---
    mlflow_tracking_uri: str = (
        "./logs/mlflow"  # Direktori/URL penyimpanan log eksperimen MLflow
    )
    mlflow_experiment_name: str = (
        "documind-experiments"  # Nama eksperimen di MLflow
    )

    # --- Konfigurasi Rate Limiting (Pembatasan Akses API) ---
    rate_limit_per_minute: int = (
        20  # Batas maksimal request API per menit per pengguna
    )

    class Config:
        """Metadata konfigurasi Pydantic."""

        env_file = ".env"  # File environment tempat membaca variabel rahasia
        env_file_encoding = "utf-8"  # Enkoding file .env


@lru_cache()
def get_settings() -> Settings:
    """Fungsi pembantu untuk mengambil instansiasi konfigurasi Settings.

    Menggunakan dekorator `@lru_cache()` agar konfigurasi hanya dibaca
    sekali dari sistem/file .env (Singleton Pattern), sehingga menghemat
    memori dan performa aplikasi.
    """
    return Settings()