class TheThing(object):
  def __init__(self):
    self.number = 0

  def some(self):
    print "I got called"

  def add(self, more):
    self.number += more
    return self.number

a = TheThing()
b = TheThing()

a.some()
b.some()

print a.add(20)
print b.add(30)

print a.number
print b.number

class TheMultiplier(object):
  def __init__(self, base):
    self.base = base

  def do_it(self, m):
    return m * self.base

x = TheMultiplier(a.number)
print x.do_it(b.number)

