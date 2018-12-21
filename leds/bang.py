import pygame.midi
import time

pygame.midi.init()
print("start")

player = pygame.midi.Output(3)
player.set_instrument(0)

# black (0-15) , white (16-31), yellow (32-47), aqua (48-63), purple (64-79), blue (80-95), green (96-111), red (112-127)
velocity = 16

# for velocity in range(16, 127, 16):
for column in range(0, 8):
    for row in range(0, 113, 16):
        print(column + row)
        player.note_on(column + row, velocity)
# why does this hang every so often?


# time.sleep(0.1)
del player
pygame.midi.quit()
print("end")
