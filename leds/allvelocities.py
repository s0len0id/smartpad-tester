import pygame.midi
import time

pygame.midi.init()
print("start")

player = pygame.midi.Output(3) # 3rd midiport on my machine
player.set_instrument(0)

channel = 2 # any channel?
note = 0

player.note_off(note, 0)
time.sleep(0.1)

for velocity in range(0,128,1):
 print(velocity)
 player.note_on(note, velocity)
 time.sleep(0.1)

 player.note_off(note, 1) # any velocity?
 time.sleep(0.1)


del player
pygame.midi.quit()
print ("end")

