from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.io import read_metrics,read_content
from src.validation import validate_content
from src.report import render_report
c=read_content('content/report_content.json');validate_content(c);t=render_report(read_metrics('data/input/metrics.csv'),c);ok='# Laporan Penjualan Siap Keputusan' in t and 'Rp8.745.000' in t and '## Batasan' in t;print('PASS' if ok else 'FAIL');raise SystemExit(not ok)
