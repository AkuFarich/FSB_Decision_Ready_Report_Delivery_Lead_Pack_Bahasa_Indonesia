# Perintah Kerja AR-2026-082 — Laporan Penjualan Siap Keputusan

## Konteks bisnis
Tim Operasional Komersial telah menerima ekstrak metrik yang tervalidasi, tetapi belum dapat menyebarkannya langsung kepada pengambil keputusan. Ekstrak tersebut berisi angka yang benar, tetapi belum memiliki narasi, konteks keputusan, pemetaan sumber, atau batasan. Laporan Markdown yang dapat ditinjau harus tersedia sebelum rapat bisnis mingguan.

## Peran Anda
Anda adalah **Analis Data** yang bertanggung jawab mengubah `data/input/metrics.csv` menjadi laporan siap keputusan melalui alur kerja Python yang dapat diulang.

## Pertanyaan bisnis
1. Apa temuan paling material dalam gambaran penjualan saat ini?
2. Mengapa temuan tersebut penting bagi Tim Operasional Komersial?
3. Tindakan atau validasi apa yang harus dilakukan berikutnya?
4. Apa yang tidak dapat disimpulkan dari bukti yang tersedia?

## Hasil yang wajib diserahkan
- `data/output/report.md`
- `content/report_content.json` yang telah dilengkapi
- `src/report.py` yang telah diterapkan
- `workpapers/CLAIM_REGISTER.md`
- `workpapers/DELIVERY_HANDOFF.md`
- seluruh pemeriksaan otomatis berhasil

## Batasan pelaksanaan
- Jangan mengubah `data/input/metrics.csv`.
- Jangan menulis nilai metrik secara langsung di kode pembuat laporan.
- Setiap pernyataan material harus terhubung ke kunci metrik.
- Rekomendasi harus sebanding dengan bukti yang tersedia.
- Metrik wajib yang hilang, ganda, atau bukan angka harus menghentikan proses sebelum keluaran ditulis.

## Dasar penerimaan
- Sebanyak 25 baris metrik yang telah dinormalisasi diterima.
- Laporan memuat ringkasan eksekutif, ringkasan metrik, tepat tiga temuan yang telah ditinjau, asumsi, batasan, langkah berikutnya, dan ketertelusuran.
- Laporan berubah ketika salinan masukan yang disetujui berubah.
- Data uji yang tidak valid gagal dengan pesan yang jelas.
- Perintah akhir `python delivery_check.py` menampilkan `READY FOR REVIEW`.

## Di luar cakupan
- Penarikan kesimpulan sebab-akibat.
- Pernyataan profitabilitas tanpa data biaya atau margin.
- Analisis tren tanpa deret waktu.
- Penyuntingan manual terhadap nilai metrik yang dihasilkan.
