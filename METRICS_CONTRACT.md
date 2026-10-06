# Kontrak Metrik

`data/input/metrics.csv` adalah antarmuka yang disetujui antara alur analitik sebelumnya dan pembuat laporan.

## Kolom wajib
- `metric`
- `rank`
- `dimension`
- `value`

## Kunci wajib
- `total_transactions / ""`
- `total_revenue / ""`
- `aov / ""`
- `unique_buyers / ""`
- `repeat_buyers / ""`
- `category_revenue / Electronics`
- `city_revenue / Unknown`

## Kendali
- Kombinasi `(metric, dimension)` harus unik.
- `value` harus berupa angka.
- Seluruh kunci wajib harus tersedia.
- Masukan hanya boleh dibaca dan tidak boleh diubah.
- Masukan yang tidak valid harus gagal sebelum laporan ditulis.
