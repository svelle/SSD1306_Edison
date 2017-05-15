import SSD1306
import Image, ImageFilter

# you can change this to SSD_1306.SSD1306_128_32() if you have a smaller display
disp = SSD1306.SSD1306_128_64()

disp.begin()
disp.clear()
disp.display()

image = Image.open('edison.png')
image = image.resize((128,64))  # set this according to your displays resolution
#image = image.filter(ImageFilter.SHARPEN)
image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
image = image.convert('1')

disp.image(image)
disp.display()
disp.invert()