import pygame.midi
import time


pygame.midi.init()
print("start")
# for port in (pygame.midi.get_count())
#     info = pygame.midi.get_device_info(port)

print("single")
player = pygame.midi.Output(3)
player.set_instrument(0)

channel = 2
note = 32
velocity1= 127
velocity2= 0

for count in range(0,2):
 print(velocity1)
 player.note_on(note, velocity1)
 time.sleep(0.1)

 player.note_off(note, velocity2)
 time.sleep(0.1)

 player.note_off(note, 0)
 time.sleep(0.1)

del player
pygame.midi.quit()
print ("end")

