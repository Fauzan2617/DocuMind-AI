# Path: Digunakan untuk memanipulasi dan mengelola jalur file/direktori secara aman & lintas platform (Windows/Linux/Mac)
from pathlib import Path  

# List: Digunakan untuk memberikan tipe data petunjuk (type hinting) bahwa suatu variabel berisi daftar/kumpulan data
from typing import List  

# Document: Class standar dari LangChain yang digunakan untuk membungkus data teks beserta metadatanya (metadata & page_content)
from langchain_core.documents import Document  

# app_logger: Logger kustom dari aplikasi untuk mencatat log/pesan sistem (seperti info, error, warning) demi pencatatan debugging
from app.core.logger import app_logger

# fungsi untuk load document dan split per halaman 
def load_pdf (file_path: Path) -> List[Document]:
    from langchain_community.document_loaders import PyPDFLoader

    app_logger.info(f"loading PDF: {file_path.name}")
    loader = PyPDFLoader(str(file_path))
    docs = loader.load()
    app_logger.info(f" -> {len(docs)} halaman doc ditemukan")
    return docs
    