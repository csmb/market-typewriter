import RPi.GPIO as GPIO
import jukebox
import key as Key

def init():
  gpio_init()

def gpio_init():
  def get_channel(k): return k.gpio
  chan_list = map(get_channel, Key.all)

  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(chan_list, GPIO.IN)
  for channel in chan_list:
    GPIO.add_event_detect(
      channel,
      GPIO.RISING,
      callback=gpio_callback,
      bouncetime=200
    )

# put that somehwere: GPIO.cleanup()

def gpio_callback(channel):
  key = Key.from_gpio(channel)
  if key:
    if _key_press_callback:
      _key_press_callback(key)
  else:
    # Log bad gpio

_key_press_callback = None

def on_key_press(callback):
  _key_press_callback = callback
