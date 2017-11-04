import random
import math

class Player:
    def __init__(self, name, thPA, thPE, twPA, twPE, ftPA, ftPE):
        self.name = name
        self.score = 0
        self.shooting = [thPA, thPE, twPA, twPE, ftPA, ftPE]

    def ppg(self):
        score = 0
        for a in range(0, 5, 2):
            PA = float(self.shooting[a])
            global PE
            try:
                PE = float(self.shooting[a+1])
            except ValueError:
                PE = 0.0

            #round PA
            b = math.floor(PA)
            prob = PA - b
            r = random.random()
            if r < prob:
                PA = int(b)
            else:
                PA = int(b + 1)
            #shoot!
            for a in range(PA):
                rand = random.random()
                if rand<PE:
                    if(a > 1):
                        score += 2
                    else:
                        score += 1
        self.score = score
        return score

    def show(self):
        print self.name + " : " + str(self.score)

    def stats(self):
        print "3P% = " + self.shooting[1]+ " "+"2P% = " + self.shooting[3]+ " " + "FT% = " + self.shooting[5]


class Team:
    def __init__(self, name, players={}):
        self.name = name
        self.players = players
        self.score = 0

    def play(self, _stats = False):
        score = 0
        for player in self.players.values():
            sc = player.ppg()
            score = score + sc
            if _stats == True:
                player.show()
        self.score = score
        return score

    def addPlayer(self, player):
            self.players[player.name] = player

    def roster(self):
        for player in self.players:
            print player.name



