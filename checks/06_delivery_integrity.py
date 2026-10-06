from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pathlib import Path
p=Path('data/output/report.md')
ok=p.exists() and p.stat().st_size>500 and 'TODO' not in p.read_text(encoding='utf-8')
print('PASS' if ok else 'FAIL','delivery integrity')
raise SystemExit(not ok)
