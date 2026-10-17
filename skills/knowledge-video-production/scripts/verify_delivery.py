"""Technical checks only; never claims visual quality, no burned captions, or listening."""
import argparse,json,re,subprocess
from fractions import Fraction
from pathlib import Path

def run(args):
    p=subprocess.run(list(map(str,args)),capture_output=True,text=True,encoding='utf-8',errors='replace')
    if p.returncode:raise RuntimeError(p.stderr[-1800:])
    return p.stdout

def time_ms(s):
    h,m,sec,ms=map(int,re.split('[:,]',s));assert m<60 and sec<60 and ms<1000
    return ((h*60+m)*60+sec)*1000+ms

def main():
    p=argparse.ArgumentParser();p.add_argument('video',type=Path);p.add_argument('--srt',type=Path,required=True)
    p.add_argument('--width',type=int,default=3840);p.add_argument('--height',type=int,default=2560);p.add_argument('--fps',type=int,default=60)
    p.add_argument('--frames',type=int);p.add_argument('--expected-text',type=Path);p.add_argument('--report',type=Path)
    a=p.parse_args();probe=json.loads(run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',a.video]))
    streams=probe['streams'];v=next(s for s in streams if s['codec_type']=='video');audio=next(s for s in streams if s['codec_type']=='audio')
    assert (v['width'],v['height'])==(a.width,a.height),'Wrong dimensions'
    assert Fraction(v['r_frame_rate'])==a.fps and Fraction(v['avg_frame_rate'])==a.fps,'Wrong frame rate'
    assert not any(s['codec_type']=='subtitle' for s in streams),'Muxed subtitle stream found'
    if a.frames is not None:assert int(v['nb_frames'])==a.frames,'Wrong frame count'
    duration=float(probe['format']['duration']);assert duration>0
    blocks=re.split(r'\n\s*\n',a.srt.read_text(encoding='utf-8-sig').replace('\r\n','\n').strip());last=0;text=[]
    assert blocks and blocks[0].strip(),'Empty SRT'
    for i,b in enumerate(blocks,1):
        lines=b.splitlines();assert len(lines)>=3 and int(lines[0])==i,'SRT cue numbering/text invalid'
        match=re.fullmatch(r'(\d{2,}:\d{2}:\d{2},\d{3}) --> (\d{2,}:\d{2}:\d{2},\d{3})',lines[1]);assert match,'Invalid SRT timestamp'
        st,en=map(time_ms,match.groups());assert last<=st<en<=round(duration*1000),'SRT order/range invalid';last=en;text.extend(lines[2:])
    if a.expected_text:
        clean=lambda s:re.sub(r'\s+','',s)
        assert clean(''.join(text))==clean(a.expected_text.read_text(encoding='utf-8-sig')),'SRT differs from expected text'
    run(['ffmpeg','-nostdin','-v','error','-err_detect','explode','-i',a.video,'-f','null','-'])
    report={'technicalPass':True,'width':v['width'],'height':v['height'],'fps':a.fps,'frames':v.get('nb_frames'),'durationSeconds':duration,'audioCodec':audio['codec_name'],'subtitleCues':len(blocks),'checks':['dimensions','frameRate','audioPresent','noSubtitleStream','srtNumberingOrderRange','fullDecode'],'scope':'Does not certify absence of burned captions, visual quality, natural voice, listening or human approval.'}
    if a.expected_text:report['checks'].append('exactNarrationTextIgnoringWhitespace')
    if a.report:a.report.parent.mkdir(parents=True,exist_ok=True);a.report.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
