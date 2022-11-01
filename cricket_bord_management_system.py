import random

class T2CUP:
    allTeams = []
    def entry_team(self,teamName):
        self.allTeams.append(teamName)

        

class Team(T2CUP):
    def __init__(self, name) -> None:
        self.teamName = name
        self.playersName = []
        super().entry_team(self)
    def entry_players(self, player):
        self.playersName.append(player)
    def __repr__(self) -> str:
        return f"Team Name {self.teamName}"

class Player:
    def __init__(self,name, teamNameObj) -> None:
        self.playerName = name
        self.strikeRate = 0.0
        self.runBat = 0
        self.usedBall = 0
        self.fours = 0
        self.six = 0
        self.runBall = 0
        self.wicketsTaken = 0
        self.ballBowld = 0
        teamNameObj.playersName.append(self)
    def __repr__(self) -> str:
        return f"Form player Obj : {self.playerName}"

class Innings:
    def __init__(self,teamOne,teamTwo,battingTeam,bowlingTeam) -> None:
        self.teamOne = teamOne
        self.teamOne = teamTwo
        self.battingTeam = battingTeam
        self.BowlingTeam = bowlingTeam
        self.totalRun = 0
        self.totalWickets = 0
        self.totalOver = 0
        self.currentBall = 0
        self.currentBattingList = [battingTeam.playersName[0],battingTeam.playersName[1]]
        self.striker = battingTeam.playersName[0]
        self.currentBowler = None
        self.currentOverStatus = []
        self.allOverstatus = []
    def show_score_board(self):
        print(f"*{self.currentBattingList[0].playerName} - {self.currentBattingList[0].runBat} ({self.currentBattingList[0].usedBall})", end="\t")
        print(f"{self.currentBattingList[1].playerName} - {self.currentBattingList[1].runBat} ({self.currentBattingList[1].usedBall})")
        print(f"{self.battingTeam.teamName[:3].upper()} Total Run : ({self.totalRun}-{self.totalWickets})W")
        print(f"Overs:({self.totalOver}.{self.currentBall})Ball")
        if self.currentBowler != None:
            print(f"Bowler Name : {self.currentBowler.playerName}  Give runs : {self.currentBowler.runBall} Bowl : {self.currentBowler.ballBowld} Current Over : {self.currentOverStatus}")
    def entry_bowler(self,bowlerNameObj):
        self.currentBowler = bowlerNameObj

    def playBowl(self,status):
        self.totalRun += status
        self.striker.runBat += status
        self.striker.usedBall +=1
        self.currentBowler.runBall += status
        self.currentBowler.ballBowld += 1
        self.currentBall += 1
        if self.currentBall == 6:
            self.currentBall = 0
            self.totalOver+=1



cup = T2CUP()
# Team Bangladesh
bangladesh = Team("Bangladesh")
Tamim = Player("Tamim Iqbal", bangladesh)
Sakib = Player("Sakib Al Hasan",bangladesh)
Mushfiq = Player("Mushfiqur Rahim",bangladesh) 
Mustafiz = Player("Mustafizur Rahman",bangladesh) 
Liton = Player("Liton Das",bangladesh) 
Mahmudullah = Player("Mahmudullah",bangladesh)
Rubel = Player("Rubel Hossain",bangladesh)
Imrul = Player("Imrul Kayes",bangladesh)
Soumya = Player("Soumya Sarker",bangladesh)
Afif = Player("Afif Hossain",bangladesh)
Taskin = Player("Taskin Ahmed",bangladesh)

# print(bangladesh.teamName)
# print(bangladesh.playersName)

# Team India
india = Team("India") 
Kohli = Player("Virat Kohli",india) 
Rohit = Player("Rohit Sharma",india)
Dinesh = Player("Dinesh Kartik",india)
Rishabh = Player("Rishabh Pant",india)
Ravichandran = Player("Ravichandran Ashwin",india)
Kl = Player("KL Rahul",india)
Hardik = Player("Hardik Pandya",india)
Shami = Player("Mohammad Shami",india)
Ravindra = Player("Ravindra Jadeja",india)
Bumrah = Player("Jasprith Bumrah",india)

# match = Innings(bangladesh,india,bangladesh,india)
# match.show_score_board()


while True:
    print("Select two teams to played")
    for index, name in enumerate(cup.allTeams):
        print(f"{index+1}. {name.teamName}")
    teamOne,teamTwo = map(int,input("Enter two teams index : ").split(" "))
    teamOne-=1
    teamTwo-=1
    teamOneObj = cup.allTeams[teamOne]
    teamTwoObj = cup.allTeams[teamTwo]
    tossWinTeam = random.choice([teamOne,teamTwo])
    print(f"{cup.allTeams[tossWinTeam].teamName} Win the toss.")
    if tossWinTeam == teamOne:
        tossLoseTeam = teamTwo
    else:
        tossLoseTeam = teamOne
    rand = random.choice([0,1])
    if rand == 0:
        print(f"{cup.allTeams[tossWinTeam]} choice bowling fast.")
        battingTeamNameObj = cup.allTeams[tossLoseTeam]
        bowlingTeamNameObj = cup.allTeams[tossWinTeam]
    else:
        print(f"{cup.allTeams[tossWinTeam]} choice batting fast.")
        battingTeamNameObj = cup.allTeams[tossWinTeam]
        bowlingTeamNameObj = cup.allTeams[tossLoseTeam]
    fastInnings = Innings(teamOneObj,teamTwoObj,battingTeamNameObj,bowlingTeamNameObj)
    fastInnings.show_score_board()
    print()
    print("Choice a bowler : ")
    for index , name in enumerate(bowlingTeamNameObj.playersName):
        print(f"{index+1}. {name.playerName}")
    bowlerIndex = int(input("Enter player index : "))
    bowlerIndex -= 1
    bowlerNameObj = bowlingTeamNameObj.playersName[bowlerIndex]
    fastInnings.entry_bowler(bowlerNameObj)
    print("\n")
    totalBall = int(input("Enter total Ball : "))
    for i in range(totalBall):
        runStatus = int(input("Current ball status : "))
        fastInnings.playBowl(runStatus)
        fastInnings.currentOverStatus.append(runStatus)
    print("\n")
    fastInnings.show_score_board()
    print("\n")
    break


