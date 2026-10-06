# Panduan Pelaksanaan

Jalankan seluruh perintah dari folder utama proyek.

```bash
python preflight.py
python checks/01_input_smoke.py
python checks/02_metrics_contract.py
python generate_report.py --metrics data/input/metrics.csv --content content/report_content.json --output data/output/report.md
python checks/03_report_acceptance.py
python checks/04_traceability.py
python checks/05_failure_controls.py
python checks/06_delivery_integrity.py
python delivery_check.py
```

Meja kerja notebook bersifat pilihan:

```bash
jupyter notebook notebooks/Report_Delivery_Workbench.ipynb
```
