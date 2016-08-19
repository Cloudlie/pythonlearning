class Song(object):
  def __init__(self, lyrics):
    self.lyrics = lyrics

  def sing_me_a_song(self):
    for line in self.lyrics:
      print line

happy = Song(['H','I','S'])

bulls = Song(['T','W'])

happy.sing_me_a_song()

bulls.sing_me_a_song()
