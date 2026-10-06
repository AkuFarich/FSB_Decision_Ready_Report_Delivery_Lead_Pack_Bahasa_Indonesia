from pathlib import Path
import sys,csv
ROOT=Path(__file__).resolve().parent
checks=[]
def check(label,condition,detail=''):
 checks.append(bool(condition)); print(('PASS' if condition else 'FAIL'),label,detail)
check('Python 3.11+',sys.version_info>=(3,11),sys.version.split()[0])
check('Project root',(ROOT/'src/report.py').exists(),str(ROOT))
path=ROOT/'data/input/metrics.csv'
try:
 rows=list(csv.DictReader(path.open(encoding='utf-8')))
 check('Metrics input',len(rows)==25,f'{len(rows)} rows')
except Exception as exc:check('Metrics input',False,str(exc))
print('\nREADY TO START WORK' if all(checks) else '\nSETUP BLOCKED')
raise SystemExit(0 if all(checks) else 1)
