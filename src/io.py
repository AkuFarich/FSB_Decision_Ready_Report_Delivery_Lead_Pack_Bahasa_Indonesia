import csv,json
from pathlib import Path
def read_metrics(path):
 with Path(path).open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
def read_content(path):return json.loads(Path(path).read_text(encoding='utf-8'))
def write_text(path,text):p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')
