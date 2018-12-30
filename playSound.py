import pygame
from time import sleep

pygame.mixer.init()
pygame.mixer.music.load("maron5.mp3")
pygame.mixer.music.play()

print("volume: " + pygame.mixer.music.get_volume())
sleep(1)
vol = 1
pygame.mixer.music.set_volume(vol)

while pygame.mixer.music.get_busy() == True:
    vol-=0.1
    pygame.mixer.music.set_volume(vol)
    print("volume: " + pygame.mixer.music.get_volume())