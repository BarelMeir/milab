import pygame

pygame.mixer.init()
pygame.mixer.music.load("maron5.mp3")
pygame.mixer.music.play()

print(pygame.mixer.music.get_volume())
while pygame.mixer.music.get_busy() == True:
    continue