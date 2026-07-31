# DocuMind AI — Makefile
# Usage: make <command>

.PHONY: install run dev test clean mlflow help

install:
	@echo "📦 Installing dependencies..."
	pip install -r requirements.txt

run:
	@echo "🚀 Starting DocuMind AI..."
	uvicorn app.main:app --host 0.0.0.0 --port 8000

dev:
	@echo "🔧 Starting in dev mode (auto-reload)..."
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

test:
	@echo "🧪 Running tests..."
	pytest tests/ -v

mlflow:
	@echo "📊 Starting MLflow UI..."
	mlflow ui --backend-store-uri ./logs/mlflow --port 5000

clean:
	@echo "🧹 Cleaning cache..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	rm -rf ./data/vectorstore

setup-env:
	@echo "⚙️  Copying .env.example → .env"
	cp .env.example .env
	@echo "✅ Sekarang edit .env dan isi GROQ_API_KEY!"

help:
	@echo "Available commands:"
	@echo "  make install    — install semua dependency"
	@echo "  make run        — jalankan server"
	@echo "  make dev        — jalankan dengan auto-reload"
	@echo "  make test       — jalankan tests"
	@echo "  make mlflow     — buka MLflow dashboard"
	@echo "  make clean      — bersihkan cache"
	@echo "  make setup-env  — setup file .env"
