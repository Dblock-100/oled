import adafruit_ssd1306
import board
import busio
import digitalio

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
reset_pin = digitalio.DigitalInOut(board.D4)
cs_pin = digitalio.DigitalInOut(board.D5)
dc_pin = digitalio.DigitalInOut(board.D6)

oled = adafruit_ssd1306.SSD1306_SPI(128, 64, spi, dc_pin, reset_pin, cs_pin)