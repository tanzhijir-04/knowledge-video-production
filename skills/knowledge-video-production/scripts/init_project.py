"""Initialize an empty video project; never overwrite existing work."""
import argparse,json
from pathlib import Path

def main():
    p=argparse.ArgumentParser();p.add_argument('directory',type=Path);p.add_argument('--topic',required=True)
    p.add_argument('--width',type=int);p.add_argument('--height',type=int);p.add_argument('--fps',type=int)
    a=p.parse_args();root=a.directory.resolve()
    if root.exists():p.error('Destination already exists; select a new directory')
    data=json.loads((Path(__file__).resolve().parents[1]/'assets/production-defaults.json').read_text(encoding='utf-8'))
    data['topic']=a.topic
    for k in ['width','height','fps']:
        if getattr(a,k) is not None:
            if getattr(a,k)<=0:p.error(k+' must be positive')
            data['video'][k]=getattr(a,k)
    from math import gcd
    w,h=data['video']['width'],data['video']['height'];g=gcd(w,h);data['video']['aspect']=f'{w//g}:{h//g}'
    root.mkdir(parents=True)
    for folder in ['research','script','design/storyboard','project/compositions','project/lib','project/media/images','project/media/fonts','project/media/audio/voice','project/media/audio/music','project/media/audio/sfx','project/data','project/scripts','delivery','covers','publishing','evidence','cache']:(root/folder).mkdir(parents=True,exist_ok=True)
    (root/'project/data/assets.json').write_text(json.dumps({'schemaVersion':1,'assets':[]},indent=2)+'\n',encoding='utf-8')
    (root/'production.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    (root/'STATUS.md').write_text('# Production status\n\nStage: initialized. No film, voice, assets, timeline or review completed.\n\nNext: inspect topic/script, load zhijie-writing as needed, record evidence and scene contracts.\n',encoding='utf-8')
    print('INITIALIZED',root)

if __name__=='__main__':main()
