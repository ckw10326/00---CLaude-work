from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'figures'; OUT.mkdir(exist_ok=True)
FONT='C:/Windows/Fonts/msjh.ttc'
def font(n): return ImageFont.truetype(FONT,n)
INK='#16324a'; TEAL='#087f8c'; RED='#b33a36'; MUTED='#526678'
def base(title,sub,height=860):
    im=Image.new('RGB',(1600,height),'#f4f7fa'); d=ImageDraw.Draw(im)
    d.text((65,40),title,font=font(44),fill=INK)
    d.text((65,110),sub,font=font(25),fill=MUTED)
    return im,d
def box(d,xy,lines,color=TEAL):
    d.rounded_rectangle(xy,18,fill='white',outline=color,width=3)
    x1,y1,x2,y2=xy
    for j,line in enumerate(lines):
        b=d.textbbox((0,0),line,font=font(28)); w=b[2]-b[0]
        d.text(((x1+x2-w)/2,y1+18+j*40),line,font=font(28),fill=INK)
def arrow(d,pts,color=TEAL):
    d.line(pts,fill=color,width=6)
    x,y=pts[-1]; a,b=pts[-2]
    import math
    ang=math.atan2(y-b,x-a)
    d.polygon([(x,y),(x-18*math.cos(ang-.45),y-18*math.sin(ang-.45)),(x-18*math.cos(ang+.45),y-18*math.sin(ang+.45))],fill=color)

im,d=base('圖 1｜故障電流：把回路追查到電源','限定模型：中性點直接接地，外殼以連續金屬導體連回電源側。')
box(d,(80,220,400,335),['電源繞組','相端'])
box(d,(620,220,940,335),['相線','保護裝置'])
box(d,(1160,220,1480,335),['相線碰觸外殼','故障點'],RED)
box(d,(1160,490,1480,605),['設備接地導體','金屬回路'])
box(d,(80,490,400,605),['電源側連結點','中性點'])
arrow(d,[(400,277),(620,277)])
arrow(d,[(940,277),(1160,277)],RED)
arrow(d,[(1320,335),(1320,490)],RED)
arrow(d,[(1160,548),(400,548)])
arrow(d,[(240,490),(240,335)])
d.line([(240,605),(240,685),(600,685)],fill=MUTED,width=4)
d.text((625,662),'接地極與大地（其他並聯路徑省略）',font=font(26),fill=MUTED)
d.text((80,742),'箭頭表示追蹤方向，並非交流電流固定單向流動。不是施工接線圖。',font=font(27),fill=INK)
d.text((80,790),'依 DOE-HDBK-1092-2013 §5.5.1 與 OSHA 1910.304(g)(4) 自行整理。',font=font(23),fill=MUTED)
im.save(OUT/'01_fault_loop.png')

im,d=base('圖 2｜觸電風險：看人體接觸的兩個點','概念圖：電位差與完整通路使人體可能成為電流路徑的一部分。')
box(d,(80,215,440,330),['接觸點 A','例如設備金屬外殼'],RED)
box(d,(620,215,980,330),['人體及接觸通路','阻抗並非固定值'],RED)
box(d,(1160,215,1520,330),['接觸點 B','例如腳下或另一金屬物'],RED)
arrow(d,[(440,273),(620,273)],RED);arrow(d,[(980,273),(1160,273)],RED)
for x,title,lines in [(80,'接觸電壓',['手觸物體與腳下位置','關注手到腳的電位差']), (580,'步間電壓',['左腳位置與右腳位置','未碰設備也可能有風險']), (1080,'影響傷害的因素',['電流大小、通過時間','路徑與接觸狀況'])]:
    d.rounded_rectangle((x,420,x+440,650),20,fill='white')
    d.text((x+25,445),title,font=font(32),fill=TEAL)
    for j,line in enumerate(lines):d.text((x+25,510+j*48),line,font=font(25),fill=INK)
d.text((80,720),'圖中不設定人體安全電流或容許電壓，亦不表示可用人體試探電位差。',font=font(27),fill=INK)
d.text((80,780),'依 NIOSH 2009-113 §§1–2、OSHA 1910.269 Appendix C II.B 自行整理。',font=font(23),fill=MUTED)
im.save(OUT/'02_shock_path.png')

im,d=base('圖 3｜同樣的設備電位，接觸電壓可以不同','純算術教學例：同一瞬間的假設電位；不是現場量測、模擬或合格判定。',940)
for x,title,foot,touch in [(65,'情境 A',900,100),(830,'情境 B',100,900)]:
    d.rounded_rectangle((x,190,x+705,750),20,fill='white')
    d.text((x+35,220),title,font=font(32),fill=TEAL)
    box(d,(x+35,290,x+670,390),['設備外殼：1,000 V'],RED)
    d.text((x+35,435),f'腳下位置：{foot:,} V',font=font(31),fill=INK)
    d.text((x+35,510),f'兩點差值：1,000 - {foot:,}',font=font(31),fill=INK)
    d.text((x+35,580),f'預期接觸電壓 = {touch:,} V',font=font(34),fill=RED)
    d.text((x+35,675),'不能僅憑這個差值宣告安全。',font=font(26),fill=MUTED)
d.text((80,790),'遠方大地在兩例中均作為 0 V 參考。未接入人體，未計人體與足部接觸阻抗。',font=font(26),fill=INK)
d.text((80,850),'本報告自設例題；概念依 OSHA Appendix C II、Schneider Electrical Installation Guide 圖 B13。',font=font(22),fill=MUTED)
im.save(OUT/'03_potential_difference.png')
