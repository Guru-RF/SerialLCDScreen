import time
import board
import busio
import simpleio
import terminalio
import digitalio
import displayio
import adafruit_displayio_ssd1306
from simpleio import map_range
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text.label import Label
from digitalio import DigitalInOut, Direction, Pull

# release displays
displayio.release_displays()

# Our reset button
btn = DigitalInOut(board.GP15)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

# Create the I2C interface for the oled
i2c2 = busio.I2C(scl=board.GP21, sda=board.GP20)

# Display bus
display_bus = displayio.I2CDisplay(i2c2, device_address=60)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
display.brightness = 0.01

# Fonts
small_font = "fonts/Roboto-Medium-16.bdf"
#  glyphs for fonts
glyphs = b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-,.: '
#  loading bitmap fonts
small_font = bitmap_font.load_font(small_font)
small_font.load_glyphs(glyphs)

# Display content
splash = displayio.Group()
display.show(splash)

# Steps countdown
steps_countdown = Label(small_font, text='10 Left')
steps_countdown.x = 1
steps_countdown.y = 22

# Steps taken
text_steps = Label(small_font, text="0 Done    ")
text_steps.x = 1
text_steps.y = 40

# Steps per hour
text_sph = Label(small_font, text="0/H")
text_sph.x = 1
text_sph.y = 58

# Add to display
splash.append(text_sph)
splash.append(steps_countdown)
splash.append(text_steps)

while True:
    time.sleep(0.001)
