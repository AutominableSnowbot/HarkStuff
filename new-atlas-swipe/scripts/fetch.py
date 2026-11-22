import xml.etree.ElementTree as ET,re,json,html,urllib.request
raw=urllib.request.urlopen(urllib.request.Request('https://newatlas.com/index.rss',headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read()
r=ET.fromstring(raw);out=[]
for it in r.iter('item'):
    t=it.findtext('title');l=it.findtext('link');d=it.findtext('description') or ''
    m=re.search(r'srcset="[^"]*?(https://[^ ]+) 800w',d); s=re.search(r'src="([^"]+)"',d)
    img=m.group(1) if m else (s.group(1) if s else None)
    txt=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',d))).strip()
    out.append(dict(title=t,link=l,img=img,desc=txt[:300],date=it.findtext('pubDate'),cat=l.split('/')[3]))
json.dump(out,open('new-atlas-swipe/stories.json','w'),indent=1)
print(len(out),out[0]['title'])
