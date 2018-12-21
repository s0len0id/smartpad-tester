import pygame.midi
import time

pygame.midi.init()
print("start")

player = pygame.midi.Output(3)
player.set_instrument(0)

channel = 2
note = 0
velocity1= 12
velocity2= 12

player.note_off(note, 0)
time.sleep(0.1)

for velocity in range(0,128,1):
 print(velocity)
 player.note_on(note, velocity)
 time.sleep(0.1)

 player.note_off(note, 0)
 time.sleep(0.1)


del player
pygame.midi.quit()
print ("end")

