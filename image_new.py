from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random

def rnd_char():
    return chr(random.randint(65, 90))

def rnd_color():
    return (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))

def rnd_color2():
    return (random.randint(16, 64), random.randint(16, 64), random.randint(16, 64))


weight = 40 * 6
height = 40
image = Image.new('RGB', (weight, height), (255, 255, 255))
draw = ImageDraw.Draw(image)

for x in range(weight):
    for y in range(height):
        draw.point((x, y), fill=rnd_color())

Font = ImageFont.truetype(r'D:\msyh.ttc', 26)

for t in range(6):
    draw.text((40 * t + 5, 10), rnd_char(), font=Font, fill=rnd_color2())
im = image.filter(ImageFilter.BLUR)
im.save(r'D:\code1.jpg', 'JPEG')