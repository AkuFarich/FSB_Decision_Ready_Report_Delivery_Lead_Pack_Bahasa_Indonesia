from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.io import read_metrics
from src.validation import validate_rows
r=read_metrics('data/input/metrics.csv');validate_rows(r);print('PASS contract')
