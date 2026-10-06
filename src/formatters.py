def rupiah(v):return 'Rp'+f'{int(round(float(v))):,}'.replace(',','.')
def number(v):return f'{int(float(v)):,}'.replace(',','.')
def percent(v,digits=1):return f'{float(v)*100:.{digits}f}%'.replace('.',',')
