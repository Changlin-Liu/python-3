from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rndChar():
    return chr(random.randint(65, 90))

def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 40 * 6
height = 40
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype(r'D:\msyh.ttc', 24)
draw = ImageDraw.Draw(image)

# for x in range(width):
    # for y in range(height):
        # draw.point((x, y), fill=rndColor())

for t in range(6):
    draw.text((40 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

# image = image.filter(ImageFilter.BLUR)
image.save(r'D:\code.jpg', 'jpeg')
