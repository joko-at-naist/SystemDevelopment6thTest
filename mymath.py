
x = 0
class Math:
  def absolute(self,x):
    if x < 0:
      return -x
    else:
      return x

  def sign(self, x):
    if x < 0:
      return -1
    elif x > 0:
      return 1
    else:
      return 0
