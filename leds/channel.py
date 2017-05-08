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
channels = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for channel in channels:
    for velocity in range(0, 127):
        print(channel, velocity)
        for note in range(16,32, 1):
            player.note_off(note, velocity, channel)
            print(note)
        time.sleep(1)
        for note in range(16, 32, 1):
            player.note_on(note, velocity, channel)
            # player.note_on(note, 0)
        time.sleep(1)
del player
pygame.midi.quit()
print ("end")

