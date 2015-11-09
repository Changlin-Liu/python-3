from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def rndChar():
    return chr(random.randint(65, 90))

# 设置背景色
def rndColor():
    return (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))

# 设置字体颜色
def rndColor2():
    return (random.randint(16, 64), random.randint(16, 64), random.randint(16, 64))

# 设置图片宽高
width = 40 * 6
height = 40
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建draw对象[画空图]
draw = ImageDraw.Draw(image)

# 使用随机颜色填充背景
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

# 创建字体对象
font = ImageFont.truetype(r'D:\msyh.ttc', 24)

# 使用随机颜色创建字母
for t in range(6):
    draw.text((40 * t + 10, 5), rndChar(), font=font, fill=rndColor2())

# 对图片模糊处理
# image = image.filter(ImageFilter.BLUR)
image.save(r'D:\code.jpg', 'jpeg')
