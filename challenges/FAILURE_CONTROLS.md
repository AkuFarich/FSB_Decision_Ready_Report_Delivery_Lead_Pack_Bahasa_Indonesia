# Panduan Kendali Kegagalan

## Tujuan
Buktikan bahwa hasil kerja merespons perubahan masukan dan menolak kontrak yang tidak valid sebelum menulis laporan yang menyesatkan.

## Data uji
| Data uji | Hasil yang diharapkan |
|---|---|
| `changed_revenue.csv` | Pendapatan pada laporan yang dihasilkan berubah. |
| `missing_aov.csv` | Validasi kontrak gagal dengan pesan yang jelas. |
| `duplicate_key.csv` | Kunci metrik ganda ditolak. |
| `non_numeric.csv` | Nilai bukan angka ditolak. |

## Catatan kejadian
| Data uji | Gejala | Dugaan | Pemeriksaan termurah | Penyebab utama | Verifikasi |
|---|---|---|---|---|---|
| | | | | | |
