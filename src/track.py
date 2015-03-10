class Track(object):
  """docstring for Track"""
  def __init__(self, path):
    super(Track, self).__init__()
    self.path = path

  def __eq__(self, other):
    return self.path == other.path
