#你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
from PIL import Image
import os

ext=['jpg','png','jpeg']
files=os.listdir('.')

def process(filename,mwidth=640,mheight=1136):
    image = Image.open(filename)
    w,h=image.size
    if w<=mwidth and h<mheight:
        return
    if 1.0*w/mwidth>1.0*h/mheight:
        scale=1.0*w/mwidth
        new_im = image.resize((int(w/scale),int(h/scale)),Image.ANTIALIAS)
    else:
        scale = 1.0 * h / mheight
        new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)
    new_im.save('new_'+filename)
    new_im.close()

for n in files:
    if n.split('.')[-1] in ext:
        process(n)