from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.io import read_metrics,read_content
from src.report import render_report
t=render_report(read_metrics('data/input/metrics.csv'),read_content('content/report_content.json'));keys=['total_revenue','category_revenue/Electronics','city_revenue/Unknown'];ok=all(k in t for k in keys);print('PASS' if ok else 'FAIL',keys);raise SystemExit(not ok)
