from pathlib import Path

t = f"{i[:1]}/{i[1:2]}/{i}"
for i in b:
	c = i.replace('-','')
	t = f"{i[:1]}/{i[1:2]}/{c}"
	if t.startswith('/'):
		t = t[1:]
	Path(f"media/{i}").rename(f"{t}")
