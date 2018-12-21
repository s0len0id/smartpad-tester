import pygame.midi
import time


pygame.midi.init()
print("start")
# for port in (pygame.midi.get_count())
#     info = pygame.midi.get_device_info(port)

print("channel")
player = pygame.midi.Output(3)
player.set_instrument(0)
# led RED  = channel 0, note#, note_on
# led BLUE = channel 0, note#, note_off
# is that all ?! :(
for channel in range(0, 16):
    for velocity in range(16, 128, 16):
        print("=== ON ===")
        for note in range(0, 8):
            print(channel, velocity, note)
            player.note_on(note, velocity, channel)
            time.sleep(0.5)
        print("=== OFF ===")
        for note in range(0, 8):
            player.note_off(note, velocity, channel)
del player
pygame.midi.quit()
print ("end")

