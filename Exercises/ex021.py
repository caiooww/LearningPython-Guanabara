import pygame

#*Create a program that loads and plays an mp3 file


pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()


#? It didn't work at all, I don't understand
#? Now it works, in the latest updates you need to add "input()" before the event
