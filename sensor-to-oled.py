import RPi.GPIO as GPIO
import time
import board
import adafruit_ssd1306
import digitalio
import math
from PIL import Image, ImageDraw, ImageFont

GPIO.setmode(GPIO.BCM)

TRIG = 23

ECHO = 24

######Start OLED Information#####
#Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Display Information
oled_reset = digitalio.DigitalInOut(board.D4)
width = 128
height = 64 
BORDER = 5
i2c = board.I2C()
disp = adafruit_ssd1306.SSD1306_I2C(width, height, i2c, addr=0x3C, reset=oled_reset)
#######END OELD INFORMATION#######

time.sleep(1)

GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)


GPIO.output(TRIG, True)

time.sleep(0.00001)

GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
    pulse_start = time.time()
    
while GPIO.input(ECHO)==1:
    pulse_end = time.time()
    
pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print (distance,"cm")

#convert cm to feet
cm=distance
feet=0.0328*cm
feet2=(round(feet,2))
print(feet2,("feet"))
out=(feet2)
s = out
str(s)

#convert cm into inches
cm=distance
inches=0.394*cm
inches2=(round(inches,2))
print(inches2,("inches"))

# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (width, height))

# Load default font.
font = ImageFont.load_default(10)

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as this python script!
# Some nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

# Create drawing object.
draw = ImageDraw.Draw(image)

# Define text and get total width.
text = str(s),'Feet'
maxwidth, unused = draw.textsize(text,(font))

# Set animation and sine wave parameters.
amplitude = height/4
offset = height/2 - 4
velocity = -2
startpos = width

# Animate text moving in sine wave.
print('Press Ctrl-C to quit.')
pos = startpos
while True:
    # Clear image buffer by drawing a black filled box.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    # Enumerate characters and draw them offset vertically based on a sine wave.
    x = pos
    for i, c in enumerate(text):
        # Stop drawing if off the right side of screen.
        if x > width:
            break
        # Calculate width but skip drawing if off the left side of screen.
        if x < -10:
            char_width, char_height = draw.textsize(c, font=font)
            x += char_width
            continue
        # Calculate offset from sine wave.
        y = offset+math.floor(amplitude*math.sin(x/float(width)*2.0*math.pi))
        # Draw text.
        draw.text((x, y), c, font=font, fill=255)
        # Increment x position based on chacacter width.
        char_width, char_height = draw.textsize(c, font=font)
        x += char_width
    # Draw the image buffer.
    disp.image(image)
    disp.show()
    
    # Move position for next frame.
    pos += velocity
    # Start over if text has scrolled completely off left side of screen.
    if pos < -maxwidth:
        pos = startpos
    # Pause briefly before drawing next frame.
    time.sleep(0.1)
#while False: 
# Clear display
#disp.fill(0)
#disp.show()
