import thread
import time
import pygame

queue = []
current_track = None

def init():
  queue = []
  pygame.mixer.init()

def enqueue_track(track):
  track.is_queued = True
  queue.append(track)

def next_track():
  track = None
  if len(queue) > 0:
    track = queue.pop()
    track.is_queued = False
  return track

# this blocks till play is over
def play(track):
  current_track = track
  print(track.path)
  pygame.mixer.music.load(track.path)
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy() == True:
    pass
  current_track = None

def stop():
  if pygame.mixer.music.get_busy == True:
    pygame.mixer.music.fadeout()

def loop():
  while 1:
    track = next_track()
    if track:
      play(track)
    else:
      time.sleep(0.01)

def start():
  thread.start_new_thread(loop, ())