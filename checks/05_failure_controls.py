from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.io import read_metrics
from src.validation import validate_rows
bad=['missing_aov.csv','duplicate_key.csv','non_numeric.csv'];passed=0
for f in bad:
 try:validate_rows(read_metrics('data/failure_fixtures/'+f))
 except ValueError as e:print('EXPECTED',f,e);passed+=1
print('PASS' if passed==3 else 'FAIL');raise SystemExit(passed!=3)
