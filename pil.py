from PIL import Image, ImageFilter


im = Image.open(r'D:\test.jpg')
# w, h = im.size 
# print("Original image size: %s %s" %(w, h))
# im.thumbnail((w//2, h//2))
# im.save(r'D:\thumb.jpg', 'JPEG')
im2 = im.filter(ImageFilter.BLUR)
im2.save(r'D:\blur.jpg')