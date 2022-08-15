import board
import digitalio
import adafruit_ssd1306

from PIL import Image

# Display Information
#oled_reset = digitalio.DigitalInOut(board.D4)
WIDTH = 128
HEIGHT = 64 
#BORDER = 5
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

# Initialize library.
#oled.begin()

# Clear display.
oled.fill(0)
oled.show()

# Load image based on OLED display height.  Note that image is converted to 1 bit color.
if HEIGHT == 64:
    image = Image.open('/home/k9/Documents/oled/happycat_oled_64.ppm').convert('1')
else:
    image = Image.open('happycat_oled_32.ppm').convert('1')

# Alternatively load a different format image, resize it, and convert to 1 bit color.
#image = Image.open('happycat.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

# Display image.
oled.image(image)
oled.show()
