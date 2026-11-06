#!/usr/bin/env python3
"""Find relevant UI design rules with bounded output; standard library only."""
import argparse, csv, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
CATALOG=ROOT/'assets/pattern-catalog.tsv'
ALIASES={'dropdown':['combobox','selection','search'], 'searchable':['filter','search','combobox'],
         'button':['action','cta','control'], 'darkmode':['dark','theme'],
         'font':['typography','typeface'], 'input':['form','field'],
         'animation':['motion','transition'], 'slider':['range','thumb','drag'], 'drag':['slider','range'], 'loading':['skeleton','status'],
         'error':['validation','feedback'], 'native':['platform','desktop']}
def words(s): return set(re.findall(r'[a-z0-9]+',s.lower()))-{'the','and','for','with','ui','ux','design'}
def search(query,limit=2,module=None):
    with CATALOG.open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
    if module: rows=[r for r in rows if module.lower() in r['module'].lower()]
    terms=words(query)
    def score(r):
        parts=[words(r[k]) for k in ('topic','tags','rule','module')]
        return sum(max(((6-i) if t in part else 0) for i,part in enumerate(parts))
                   for term in terms for t in [term, *ALIASES.get(term,[])])
    scored=sorted(((score(r),r) for r in rows),key=lambda p:(-p[0],p[1]['id']))
    return [{**{k:r[k] for k in ('id','topic','rule')},'module':str((ROOT/r['module']).resolve())}
            for s,r in scored if s>0][:max(1,min(10,limit))]
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('query',nargs='?',default='');p.add_argument('--limit',type=int,default=2)
    p.add_argument('--module');p.add_argument('--id');p.add_argument('--json',action='store_true')
    p.add_argument('--topics',action='store_true')
    a=p.parse_args()
    with CATALOG.open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
    if a.topics:
        for module in sorted(set(r['module'] for r in rows)):
            print(f"{module}: {sum(r['module']==module for r in rows)} patterns")
        return
    if a.id:
        items=[{**{k:r[k] for k in ('id','topic','rule')},'module':str((ROOT/r['module']).resolve())} for r in rows if r['id'].lower()==a.id.lower()]
    elif a.query: items=search(a.query,a.limit,a.module)
    else: p.error('Provide a topic, --topics, or --id')
    if a.json: print(json.dumps(items,ensure_ascii=False,indent=2))
    else:
        for r in items: print(f"{r['id']} | {r['topic']}\n  {r['rule']}\n  {r['module']}")
        if not items: print('No match; try a broader topic.')
if __name__=='__main__':main()
