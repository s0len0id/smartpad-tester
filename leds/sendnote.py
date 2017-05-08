import pygame.midi
import time

pygame.midi.init()
print("start")
# for port in (pygame.midi.get_count())
#     info = pygame.midi.get_device_info(port)

print("notes")
player = pygame.midi.Output(3)
player.set_instrument(0)
channels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
for channel in channels:
    print(channel)
    for velocity in range(127):
        print(channel, velocity)
        for note in range(0,127,4):
            print(channel, velocity, note)
            player.note_on(note, velocity)
            time.sleep(0.1)
            player.note_off(note, velocity)
del player
pygame.midi.quit()
print ("end")

