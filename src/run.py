import typewriter
import jukebox
import time
import key
from key import Key

jukebox.init()
typewriter.init()


def key_pressed(key):
  track = key.track
  jukebox.enqueue_track(track)

typewriter.on_key_press(key_pressed)

typewriter.start()
jukebox.start()

while 1:
  time.sleep(0.01)