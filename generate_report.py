import argparse
from src.io import read_metrics,read_content,write_text
from src.validation import validate_rows,validate_content
from src.report import render_report
def main():
 p=argparse.ArgumentParser();p.add_argument('--metrics',required=True);p.add_argument('--content',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 rows=read_metrics(a.metrics);c=read_content(a.content);validate_rows(rows);validate_content(c);text=render_report(rows,c);write_text(a.output,text);print(f'REPORT READY path={a.output} chars={len(text)}');return 0
if __name__=='__main__':raise SystemExit(main())
