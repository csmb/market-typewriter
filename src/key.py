import yaml
from track import Track


KEYS_PATH = "config/keys.yml"


def load_keys():
  stream = open(KEYS_PATH, 'r')
  objs = yaml.safe_load(stream)
  def load_key(obj):
    return Key(obj["gpio"], obj["track"])
  return map(load_key, objs)


class Key(object):
  """docstring for Key"""
  def __init__(self, gpio, track):
    super(Key, self).__init__()
    self.gpio = gpio
    self.track = Track(track)

  def from_gpio(self, channel):
    pass
    # for key in keys:
    #   self.gpio_to_keys[key.channel] = key

  keys = []

  @classmethod
  def all(cls):
    print 'foo'
    if not cls.keys:
      cls.keys = load_keys()
    return cls.keys