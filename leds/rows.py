import pygame.midi
import time

# MODE Clip
# row by row, all colours

pygame.midi.init()
print("start")
# for port in (pygame.midi.get_count())
#     info = pygame.midi.get_device_info(port)

print("notes")
player = pygame.midi.Output(3)
player.set_instrument(0)
for channel in range (0, 16):
    for velocity in range(16, 128, 16):
        for base in range(0, 128, 16):
            for note in range(0, 8):
                print(channel, velocity, note)
                player.note_on(base + note, velocity)
                time.sleep(0.1)
            print("=== OFF ===")
            for note in range(0, 8):
                player.note_off(base + note, 0)
del player
pygame.midi.quit()
print ("end")

