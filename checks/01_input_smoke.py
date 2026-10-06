from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.io import read_metrics
r=read_metrics('data/input/metrics.csv');ok=len(r)==25;print('PASS' if ok else 'FAIL',len(r));raise SystemExit(not ok)
