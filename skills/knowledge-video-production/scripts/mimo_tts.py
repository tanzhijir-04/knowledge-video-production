"""Generate hashed narration chunks with process-only credentials; dry-run supported."""
import argparse,base64,hashlib,json,os,re,urllib.request,urllib.error,wave
from pathlib import Path
DIRECTION='像理解技术的朋友面对面解释，正常日常语速，清楚亲近、连贯略明快。逗号轻连，句尾自然换气，不每个短句重起腔。不播音、不广告、不悬疑表演，不刻意气声或逐字拖长。英文术语自然读，不为固定秒数抢读。只读assistant正文。'

def main():
    p=argparse.ArgumentParser();p.add_argument('scenes',type=Path);p.add_argument('--out',required=True,type=Path)
    p.add_argument('--dry-run',action='store_true');p.add_argument('--voice',default='茉莉');p.add_argument('--model',default='mimo-v2.5-tts')
    p.add_argument('--endpoint',default='https://api.xiaomimimo.com/v1/chat/completions');p.add_argument('--direction',default=DIRECTION)
    a=p.parse_args();items=json.loads(a.scenes.read_text(encoding='utf-8-sig'));assert isinstance(items,list) and items
    ids=set();plan=[]
    for s in items:
        sid=s['id'];assert re.fullmatch(r'[A-Za-z0-9_-]+',sid) and sid not in ids;ids.add(sid);assert isinstance(s['text'],str) and s['text'].strip()
        body={'model':a.model,'messages':[{'role':'user','content':a.direction},{'role':'assistant','content':s['text']}],'audio':{'format':'wav','voice':a.voice}}
        digest=hashlib.sha256(json.dumps(body,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
        plan.append((sid,body,digest,a.out/f'{sid}-{digest[:12]}.wav'))
    if a.dry_run:
        print(json.dumps([{'id':sid,'fingerprint':d,'cached':f.exists()} for sid,b,d,f in plan],ensure_ascii=False));return
    key=os.environ.get('MIMO_API_KEY');assert key,'Set MIMO_API_KEY locally; no request sent'
    assert a.endpoint.startswith('https://'),'HTTPS endpoint required';a.out.mkdir(parents=True,exist_ok=True)
    opener=urllib.request.build_opener();report=[]
    for sid,body,digest,target in plan:
        if not target.exists():
            req=urllib.request.Request(a.endpoint,data=json.dumps(body,ensure_ascii=False).encode(),headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
            try:
                with opener.open(req,timeout=180) as response:result=json.load(response)
            except urllib.error.HTTPError as e:raise SystemExit(f'MiMo HTTP {e.code}; no retry performed') from None
            data=base64.b64decode(result['choices'][0]['message']['audio']['data'],validate=True)
            tmp=target.with_suffix('.tmp');tmp.write_bytes(data)
            with wave.open(str(tmp)) as w:assert w.getnframes()>0
            tmp.replace(target)
        with wave.open(str(target)) as w:duration=w.getnframes()/w.getframerate()
        report.append({'id':sid,'text':body['messages'][1]['content'],'fingerprint':digest,'file':target.name,'durationSeconds':duration,'timeStretch':False})
        print(sid,round(duration,3),'seconds',flush=True)
    (a.out/'voice-manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')

if __name__=='__main__':main()
