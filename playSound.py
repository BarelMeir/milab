import RPi.GPIO as GPIO
import pygame
from time import sleep
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import Adafruit_DHT

#Set up script to use the right pin configuration
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#MCP3008 setup
CLK = 18
MISO = 23
MOSI = 24
CS = 25
mcp = Adafruit_MCP3008.MCP3008(clk = CLK, cs = CS, miso = MISO, mosi = MOSI)

sensorLastValue = mcp.read_adc(0)

def updateSensorValue():
	global sensorLastValue
	sensorLastValue = mcp.read_adc(0)

def updateVolume(volume):
	pygame.mixer.music.set_volume(volume)

#music load
pygame.mixer.init()
pygame.mixer.music.load("best_friend.mp3")
#play music
pygame.mixer.music.play()
updateVolume(1)
while True:
	treshold = 150
	potentiometerValue = mcp.read_adc(0)
	if(potentiometerValue - sensorLastValue > treshold):
		print("potentiometer changed")
		print("last: ",sensorLastValue)
		print("current: ", potentiometerValue)
		updateSensorValue()
		updateVolume(0.2)