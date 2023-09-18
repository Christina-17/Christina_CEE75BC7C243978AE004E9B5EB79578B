'''Implement a class player that represent a cricket player.The p;ayer class should have a method .called calledplay() which prints "The player is playing cricket".Derive two classes Batsman and Bowler ,from the player class ,Override the play mathod in each derived class to print "The btsman is batting" and "The bowler is bowling" respectively.
Write a program to create the object of the both batsman and the bowler classes andcallthe play() methode for each object.'''


#Define the bae class Player
class Player:

  def play(self):
    print("The player is playing Cricket")


#Define the derived class Batsman
class Batsman(Player):

  def play(self):
    print("The batsman is Batting")


#Define the derived class Bowler
class Bowler(Player):

  def play(self):
    print("The bowler is Bowling")


#Create the Objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#Call the play() mathod for each objects
batsman.play()
bowler.play()
