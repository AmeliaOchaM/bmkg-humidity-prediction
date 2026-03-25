"""
Script untuk menggabungkan semua file Excel laporan iklim harian dari folder data_bulan
menjadi satu file Excel.

Kolom output: TANGGAL, TN, TX, TAVG, RH_AVG, RR, SS, FF_X, DDD_X, FF_AVG, DDD_CAR

Setiap file memiliki:
- Baris 1-7 (0-indexed 0-6): metadata stasiun
- Baris 8 (0-indexed 7): header kolom
- Baris 9 dst (0-indexed 8 dst): data harian, jumlah hari bervariasi tiap file
- Setelah data: baris keterangan/footnote
"""

import pandas as pd
import os
import glob

# ============================================================
# KONFIGURASI
# ============================================================
INPUT_DIR = "data_bulan"
OUTPUT_FILE = "data_gabungan_iklim_harian.xlsx"

# Nama kolom standar yang diinginkan
KOLOM_OUTPUT = [
    "TANGGAL", "TN", "TX", "TAVG", "RH_AVG",
    "RR", "SS", "FF_X", "DDD_X", "FF_AVG", "DDD_CAR"
]

# ============================================================
# PROSES
# ============================================================

def is_data_row(row):
    """
    Mengecek apakah sebuah baris merupakan baris data (tanggal valid).
    Baris data diawali dengan format tanggal (dd-mm-yyyy).
    Baris footnote biasanya diawali dengan teks deskripsi.
    """
    val = str(row.iloc[0]).strip()
    # Cek apakah nilai di kolom pertama memiliki format tanggal (dd-mm-yyyy)
    # Minimal: 2 digit angka di awal
    if len(val) >= 10 and val[2] == '-' and val[5] == '-':
        try:
            # Coba cek apakah bagian pertama (hari) adalah angka
            int(val[:2])
            return True
        except ValueError:
            return False
    return False


def baca_file(filepath):
    """
    Membaca satu file Excel laporan iklim harian.
    - Membaca dari baris ke-9 (index 8) hingga baris terakhir yang merupakan data tanggal.
    - Mengembalikan DataFrame dengan kolom standar.
    """
    # Baca seluruh file tanpa header
    df_raw = pd.read_excel(filepath, header=None, sheet_name=0)

    # Header ada di baris index 7 (baris ke-8, 1-indexed)
    # Data dimulai dari baris index 8 (baris ke-9, 1-indexed)
    df_data = df_raw.iloc[8:].copy()
    df_data.columns = KOLOM_OUTPUT
    df_data.reset_index(drop=True, inplace=True)

    # Filter hanya baris yang memiliki tanggal valid (bukan footnote)
    mask = df_data.apply(is_data_row, axis=1)
    df_data = df_data[mask].copy()
    df_data.reset_index(drop=True, inplace=True)

    return df_data


def main():
    # Cari semua file xlsx di folder input
    pattern = os.path.join(INPUT_DIR, "*.xlsx")
    files = sorted(glob.glob(pattern))

    if not files:
        print(f"Tidak ada file .xlsx ditemukan di folder '{INPUT_DIR}'!")
        return

    print(f"Ditemukan {len(files)} file Excel di folder '{INPUT_DIR}':")
    for f in files:
        print(f"  - {os.path.basename(f)}")

    # Baca dan gabungkan semua file
    all_data = []
    for filepath in files:
        try:
            df = baca_file(filepath)
            all_data.append(df)
            print(f"  ✓ {os.path.basename(filepath)}: {len(df)} baris data")
        except Exception as e:
            print(f"  ✗ {os.path.basename(filepath)}: GAGAL - {e}")

    if not all_data:
        print("Tidak ada data yang berhasil dibaca!")
        return

    # Gabungkan semua DataFrame
    df_gabungan = pd.concat(all_data, ignore_index=True)

    # Urutkan berdasarkan tanggal
    df_gabungan["TANGGAL"] = pd.to_datetime(df_gabungan["TANGGAL"], format="%d-%m-%Y", errors="coerce")
    df_gabungan.sort_values(by="TANGGAL", inplace=True)
    df_gabungan.reset_index(drop=True, inplace=True)

    # Simpan ke file Excel
    df_gabungan.to_excel(OUTPUT_FILE, index=False)

    print(f"\n{'='*50}")
    print(f"BERHASIL! Data gabungan disimpan ke: {OUTPUT_FILE}")
    print(f"Total baris data: {len(df_gabungan)}")
    print(f"Rentang tanggal: {df_gabungan['TANGGAL'].min()} s/d {df_gabungan['TANGGAL'].max()}")
    print(f"Kolom: {list(df_gabungan.columns)}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
