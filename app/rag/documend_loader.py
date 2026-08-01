# Path: Digunakan untuk memanipulasi dan mengelola jalur file/direktori secara aman & lintas platform (Windows/Linux/Mac)
from pathlib import Path  

# List: Digunakan untuk memberikan tipe data petunjuk (type hinting) bahwa suatu variabel berisi daftar/kumpulan data
from typing import List  

# Document: Class standar dari LangChain yang digunakan untuk membungkus data teks beserta metadatanya (metadata & page_content)
from langchain_core.documents import Document  

# app_logger: Logger kustom dari aplikasi untuk mencatat log/pesan sistem (seperti info, error, warning) demi pencatatan debugging
from app.core.logger import app_logger

# ===================================================================================================
''' 3 FUNGSI DIBAWAH UNTUK MENGLOAD DOCUMENT DENGAN TIPE PDF/TXT/DOCX '''
def load_pdf(file_path: Path) -> List[Document]:
    """Membaca file PDF dan mengonversinya menjadi daftar dokumen LangChain."""
    # Mengimpor loader khusus file PDF dari LangChain
    from langchain_community.document_loaders import PyPDFLoader

    # Catat log bahwa proses loading file PDF dimulai
    app_logger.info(f"loading PDF: {file_path.name}")
    
    # Inisialisasi loader dengan mengonversi path objek ke string
    loader = PyPDFLoader(str(file_path))
    
    # Membaca isi file PDF (setiap halaman akan menjadi 1 objek Document)
    pdf = loader.load()
    
    # Catat jumlah halaman yang berhasil diekstrak
    app_logger.info(f" -> {len(pdf)} halaman doc ditemukan")
    return pdf


def load_txt(file_path: Path) -> List[Document]:
    """Membaca file teks mentah (.txt) dan mengonversinya menjadi dokumen LangChain."""
    # Mengimpor loader khusus file teks (.txt)
    from langchain_community.document_loaders import TextLoader
    
    # Catat log proses membaca file .txt
    app_logger.info(f" Loading Docs: {file_path.name}")
    
    # Inisialisasi loader dengan encoding utf-8 agar karakter spesial/lokal terbaca aman
    loader = TextLoader(str(file_path), encoding="utf-8")
    
    # Membaca seluruh isi file teks sebagai 1 objek Document
    txt = loader.load()
    
    # Catat log bahwa dokumen berhasil dimuat
    app_logger.info(f" -> {len(txt)} halaman doc ditemukan")
    return txt


# KOREKSI: Nama fungsi diubah dari load_txt menjadi load_docx
def load_docx(file_path: Path) -> List[Document]:
    """Membaca file Microsoft Word (.docx) dan mengonversinya menjadi dokumen LangChain."""
    # Mengimpor loader khusus file Word (.docx)
    from langchain_community.document_loaders import Docx2txtLoader
    
    # Catat log proses membaca file Word
    app_logger.info(f" Loading Docs: {file_path.name}")
    
    # Inisialisasi loader khusus file .docx
    loader = Docx2txtLoader(str(file_path))
    
    # Membaca dan ekstrak teks dari file Word menjadi objek Document
    docx = loader.load()
    
    # Catat log bahwa dokumen Word berhasil dimuat
    app_logger.info(f" -> {len(docx)} halaman doc ditemukan")
    return docx