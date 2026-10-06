REQUIRED={'metric','rank','dimension','value'}
def validate_rows(rows):
 if not rows:raise ValueError('metrics_empty')
 missing=REQUIRED-set(rows[0]);
 if missing:raise ValueError(f'missing_columns={sorted(missing)}')
 seen=set()
 for i,r in enumerate(rows,2):
  key=(r['metric'],r['dimension'])
  if key in seen:raise ValueError(f'duplicate_metric_key={key}')
  seen.add(key)
  try:float(r['value'])
  except ValueError:raise ValueError(f'non_numeric_value row={i} value={r["value"]}')
 required={('total_transactions',''),('total_revenue',''),('aov',''),('unique_buyers',''),('repeat_buyers',''),('category_revenue','Electronics'),('city_revenue','Unknown')}
 absent=required-seen
 if absent:raise ValueError(f'missing_required_metrics={sorted(absent)}')
 return True
def validate_content(c):
 if len(c.get('insights',[]))!=3:raise ValueError('exactly_3_insights_required')
 txt=json_text(c)
 if 'TODO' in txt:raise ValueError('content_contains_TODO')
def json_text(x):
 import json
 return json.dumps(x,ensure_ascii=False)
