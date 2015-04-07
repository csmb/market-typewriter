import sys
import serial
from string import ascii_uppercase

import pygame

try:
    arduino_conn = serial.Serial(port='/dev/ttyACM0',
                                 baudrate=9600,
                                 timeout=None)
except:
    # TO DO: handle this better, check for other tty devices.
    print('No Arduino detected.')
    sys.exit(1)

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.init()

keystroke_channel = pygame.mixer.Channel(1)
track_channel = pygame.mixer.Channel(2)
sound = pygame.mixer.Sound

# The number of keys and audio files.
key_count = 4

keystroke_sound = sound('audio/key01.wav')
track_list = [sound('audio/{}.wav'.format(i)) for i in range(key_count)]
track_queue = []

while True:
    keystroke = arduino_conn.read(1)
    if keystroke:
        print(keystroke)
        keystroke_channel.play(keystroke_sound)
        track_number = ascii_uppercase.index(keystroke)
        track = track_list[track_number]
        if track not in track_queue and len(queue) < 5:
            track_queue.append(track)

    # If we have a queued track and are not already playing a track.
    if track_queue and not track_channel.get_busy():
        track = track_queue.pop(0)
        track_channel.play(track)
