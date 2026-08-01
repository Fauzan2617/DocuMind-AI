import sys
from loguru import logger  # Pustaka logging modern yang lebih sederhana dan fleksibel dari modul logging standar
from app.core.config import (
    get_settings,
)  # Mengimpor fungsi penarik konfigurasi aplikasi (dari file Settings sebelumnya)

# Memuat instansiasi konfigurasi aplikasi
settings = get_settings()


def setup_logger():
    """Fungsi untuk mengonfigurasi pustaka Loguru sesuai kebutuhan aplikasi.

    Mengatur dua output (Sink): Console (terminal) dan File Log.
    """
    # Mengapus handler default Loguru agar tidak terjadi pencatatan log ganda (duplicate logs)
    logger.remove()

    # --- Configuration 1: Console Output (Output ke Terminal) ---
    logger.add(
        sys.stdout,  # Mengarahkan output ke standar output terminal
        level=settings.log_level,  # Tingkat log minimal sesuai isi file settings (misal: "INFO")
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan> - <white>{message}</white>",  # Format visual menggunakan warna (Loguru color tags)
        colorize=True,  # Mengaktifkan pewarnaan teks di terminal
    )

    # --- Configuration 2: File Output (Penyimpanan ke File Log) ---
    logger.add(
        "./logs/app.log",  # Lokasi file tujuan penyimpanan log
        level="DEBUG",  # Menangkap semua log berlevel DEBUG ke atas ke dalam file
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",  # Format lengkap mencakup nama file, fungsi, & baris kode
        rotation="1 day",  # Rotasi file: membuat file log baru setiap 1 hari sekali
        retention="7 days",  # Retensi file: otomatis menghapus log yang umurnya lebih dari 7 hari
        compression="zip",  # Mengompresi file log lama yang dirotasi menjadi format .zip untuk menghemat disk
    )

    return logger


# Memanggil fungsi setup dan menyimpan objek logger ke dalam variabel global app_logger
# Variabel ini yang diimpor oleh modul lain (misalnya: `from app.core.logger import app_logger`)
app_logger = setup_logger()