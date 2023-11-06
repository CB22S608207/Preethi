# define the base class player
class player:
  def play(self):
    print("The player is playing cricket.")

# Define the derived class Batsman
class Batsman (player):
  def play(self):
    print("The batsman is batting.")

#Define the derived class Bowler
class Bowler (player):
  def play(self):
    print("The bowler is bowling.")

# create objects for Batsman and Bowler classes
batsman=Batsman()
bowler=Bowler()

#call the play() method for each object
batsman.play()
bowler.play()

