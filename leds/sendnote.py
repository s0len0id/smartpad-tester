import pygame.midi
import time

pygame.midi.init()
print("start")
# for port in (pygame.midi.get_count())
#     info = pygame.midi.get_device_info(port)

print("notes")
player = pygame.midi.Output(3)
player.set_instrument(0)
channels = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
bases = [0,16,32,48,64,80,96,112]
for channel in channels:
    print(channel)
    for velocity in range(16, 128, 16):
        for base in bases:
            for note in range(0, 8):
                print(channel, velocity, note)
                player.note_on(base + note, velocity)
                time.sleep(0.3)
            print("=== OFF ===")
            for note in range(16, 25):
                player.note_off(base + note, 0)
                time.sleep(0.3)
del player
pygame.midi.quit()
print ("end")

