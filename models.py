class Bottle:
  def __init__(self, volume, initial_weight, current_weight, density=0.84):
    self.initial_volume = volume
    self.initial_weight = initial_weight
    self.current_weight = current_weight
    self.density = density
    self._volume_used = (self.initial_weight - self.current_weight) / self.density
    self._current_volume = self.initial_volume - self._volume_used


  def get_initial_volume(self):
    return self.initial_volume

  @property
  def new(self):
    return self.get_initial_volume
    
  def get_volume_used(self):
    return self._volume_used

  @property
  def used(self):
    return self.get_volume_used
    
  def get_current_volume(self):
    return self._current_volume

  @property
  def left(self):
    return self.get_current_volume

  @staticmethod
  def calculate_current_volume(initial_volume, initial_weight, current_weight, density=0.84):
    return initial_volume - ((initial_weight - current_weight) / density)