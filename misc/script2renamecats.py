import os
import random

flist = os.listdir()
flist.remove("scr.py")

flist.sort(key=lambda f: int(''.join(filter(str.isdigit, f))), reverse=True)

namelist = [f"car_{n}.jpg" for n in range(1,501)]

for f in flist:
	name = random.choice(namelist)
	namelist.remove(name)
	os.rename(f, name)