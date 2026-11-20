#!/usr/bin/env python3
"""01편 조립 — parts/*.html 이어 붙이고 캐릭터 그림 묶음을 끼운다."""
import os, re, sys
ROOT=os.path.dirname(os.path.abspath(__file__))
PARTS=['p1_head.html','p2_lv12.html','p3_lv3.html','p4_lv45.html',
       'p5_duel_sum.html','p6_core.html','p7_panels.html','p8_kg.html']
OUT=os.path.join(ROOT,'01_clinical_stats_ai.html')

def sprite_bundle():
    base=open(os.path.join(ROOT,'sprites','base.js'),encoding='utf-8').read()
    add =open(os.path.join(ROOT,'sprites','add_interns.js'),encoding='utf-8').read()
    def grab(txt,name):
        m=re.search(r'var\s+'+name+r'\s*=\s*(\{.*?\});',txt,re.S)
        return m.group(1) if m else '{}'
    def merge(name):
        a,b=grab(base,name),grab(add,name)
        a,b=a.strip()[1:-1].strip(),b.strip()[1:-1].strip()
        body=', '.join(x for x in (a,b) if x)
        return 'var %s={%s};'%(name,body)
    return '\n'.join(merge(n) for n in ('SPRITE','SPRITE_ALIAS','SPRITE_FACING'))

out=[]
for p in PARTS:
    t=open(os.path.join(ROOT,'parts',p),encoding='utf-8').read()
    if '/*SPRITE_INJECT*/' in t:
        t=t.replace('/*SPRITE_INJECT*/',sprite_bundle())
    out.append(t)
html='\n'.join(out)
open(OUT,'w',encoding='utf-8').write(html)
print('조립 완료:',OUT,len(html),'바이트')
