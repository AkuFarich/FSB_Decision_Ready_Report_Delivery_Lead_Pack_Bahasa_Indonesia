# Laporan Penjualan Siap Keputusan

**Cakupan:** Data uji gerbang: 22 transaksi valid; hanya gambaran sesaat

## Ringkasan Eksekutif
- Pendapatan tercatat Rp9.745.000 dari 22 transaksi.
- Nilai transaksi rata-rata adalah Rp397.500; pembeli unik 14; pembeli berulang 8.
- Electronics menyumbang 87,7% pendapatan pada data uji ini.

## Ringkasan Metrik
| Metrik | Nilai | Kunci sumber |
|---|---:|---|
| Total transaksi | 22 | total_transactions |
| Total pendapatan | Rp9.745.000 | total_revenue |
| Nilai transaksi rata-rata | Rp397.500 | aov |
| Pembeli unik | 14 | unique_buyers |
| Pembeli berulang | 8 | repeat_buyers |
| Porsi Electronics | 87,7% | category_revenue/Electronics |
| Pendapatan kota Unknown | Rp900.000 | city_revenue/Unknown |

## Temuan
### 1. Pendapatan sangat terkonsentrasi pada Electronics
- **Bukti:** Electronics menghasilkan Rp8.550.000 dari total Rp8.745.000 atau 97,8%.
- **Makna:** Total pendapatan sensitif terhadap satu kategori.
- **Tindakan:** Validasi tren periode lain dan periksa margin sebelum mengambil keputusan persediaan.
- **Batasan:** Data uji berukuran kecil serta tidak memiliki tanggal transaksi atau margin.

### 2. Webcam mendominasi jumlah unit
- **Bukti:** Webcam terjual sebanyak 19 dari total 22 unit.
- **Makna:** Permintaan pada data uji terkonsentrasi pada satu produk.
- **Tindakan:** Periksa persediaan, waktu tunggu, dan konsistensi permintaan pada periode lain.
- **Batasan:** Jumlah unit yang tinggi tidak membuktikan laba tertinggi.

### 3. Analisis kota memiliki data hilang yang material
- **Bukti:** Kota Unknown menyumbang Rp900.000.
- **Makna:** Peringkat kota bergantung pada kebijakan penanganan nilai kosong.
- **Tindakan:** Perbaiki kelengkapan data kota dan tampilkan Unknown secara jelas.
- **Batasan:** Nilai Unknown tidak boleh dipindahkan ke kota tertentu tanpa bukti.

## Asumsi
- tx_id unik dan setiap transaksi mewakili satu baris transaksi yang valid.
- Harga produk diperlakukan sebagai harga satuan transaksi.

## Batasan
- Data uji berukuran kecil dan tidak memiliki rentang waktu sehingga tren tidak dapat dinilai.
- Data biaya, margin, promosi, atau persediaan tidak tersedia; pendapatan tidak sama dengan laba.
- Analisis bersifat deskriptif dan tidak membuktikan hubungan sebab-akibat.

## Langkah Berikutnya
- Tambahkan tanggal dan margin, kemudian ulangi analisis berdasarkan periode dan kategori.

## Ketertelusuran
Dihasilkan dari `data/input/metrics.csv`. Kunci metrik terhubung ke berkas SQL Sesi 4. Perintah tercantum dalam `EXECUTION_RUNBOOK.md`.
