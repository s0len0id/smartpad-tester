import pygame.midi
import time


pygame.midi.init()
print("start")
# for port in (pygame.midi.get_count())
#     info = pygame.midi.get_device_info(port)

print("single")
player = pygame.midi.Output(3)
player.set_instrument(0)
channel = 1
for velocity in range(0, 127):
    print(velocity)
    for note in range(0,127, 1):
        player.note_on(note, velocity)
        time.sleep(0.1)
    time.sleep(0.1)
    for note in range(0, 127, 1):
        player.note_off(note, velocity)
        # player.note_on(note, 0)
        time.sleep(0.1)
    # time.sleep(0.1)
del player
pygame.midi.quit()
print ("end")

