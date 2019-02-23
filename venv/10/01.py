#使用 Python 生成类似于下图中的字母验证码图片
import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import string
# 随机字母
def rndChar():
    return random.choice(string.ascii_letters)
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width=60*4
height=60
image = Image.new('RGB',(width,height),(255,255,255))
font = ImageFont.truetype('arial.ttf',36)
draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())

for t in range(4):
    draw.text((60*t+10,10),rndChar(),fill=rndColor2(),font=font)
image=image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')