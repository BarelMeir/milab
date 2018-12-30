import RPi.GPIO as GPIO
import pygame
from time import sleep
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import Adafruit_DHT
from mpu6050 import mpu6050

#Set up script to use the right pin configuration
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#MCP3008 setup
CLK = 18
MISO = 23
MOSI = 24
CS = 25
mcp = Adafruit_MCP3008.MCP3008(clk = CLK, cs = CS, miso = MISO, mosi = MOSI)

#music load
pygame.mixer.init()
pygame.mixer.music.load("best_friend.mp3")
pygame.mixer.music.play()

while True:
	print(mcp.read_adc(0))
	sleep(2)

# print("volume: ", pygame.mixer.music.get_volume())
# sleep(1)
# vol = 0.1
# pygame.mixer.music.set_volume(vol)
# print("volume: ", pygame.mixer.music.get_volume())
# while pygame.mixer.music.get_busy() == True:
# 	print(mcp.read_adc(0))
# 	continue