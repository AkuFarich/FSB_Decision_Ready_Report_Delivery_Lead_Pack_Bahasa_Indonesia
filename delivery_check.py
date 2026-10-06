import subprocess,sys,os
files=['01_input_smoke.py','02_metrics_contract.py','03_report_acceptance.py','04_traceability.py','05_failure_controls.py','06_delivery_integrity.py'];bad=[]
for f in files:
 r=subprocess.run([sys.executable,'checks/'+f],text=True,capture_output=True,env={**os.environ,'PYTHONPATH':'.'});print(f,r.stdout.strip());bad += [f] if r.returncode else []
print('READY FOR REVIEW' if not bad else 'NOT READY '+str(bad));raise SystemExit(bool(bad))
