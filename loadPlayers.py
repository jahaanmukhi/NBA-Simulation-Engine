from NBAConstructs import *
import csv

ppg = "ppg.csv"

rosters = "2017-2018.csv"

players = {}

teams = {}

def read(file):
    with open(file, 'rb') as f:
        rdr = csv.reader(f, delimiter='\n')
        rdr.next()
        for row in rdr:
            ss = str.split(row[0], ',')
            name = ss[1]
            name = name.split("\\")[0]
            p = Player(name, ss[12], ss[13], ss[15], ss[16], ss[19], ss[20])
            players[name] = p

def readRosters(file):
    with open(file, 'rb') as f:
        rdr = csv.reader(f, delimiter='\n')
        rdr.next()
        for row in rdr:
            ss = str.split(row[0], ',')
            name = ss[1]
            name = name.split("\\")[0]
            if name not in players.keys():
                p = Player(name, ss[12], ss[13], ss[15], ss[16], ss[19], ss[20])
                players[name] = p
            team = ss[4]
            if team in teams:
                (teams[team]).addPlayer(players.get(name))
            else:
                t = Team(team, {})
                teams[team] = t
                (teams[team]).addPlayer(players.get(name))

    teams["SAS"].addPlayer(players.get("Kawhi Leonard"))
    teams["CLE"].addPlayer(players.get("Isaiah Thomas"))
read(ppg)
readRosters(rosters)
print teams.keys()

print "GSW = {} vs OKC = {}".format(teams['GSW'].play() ,teams['OKC'].play(_stats=True))





