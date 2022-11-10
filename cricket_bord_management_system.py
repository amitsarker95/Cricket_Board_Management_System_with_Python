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
        self.sixs = 0
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
        self.currentBatsmanOrder = 2
        self.currentBattingList = [battingTeam.playersName[0],battingTeam.playersName[1]]
        self.striker = battingTeam.playersName[0]
        self.currentBowler = None
        self.currentOverStatus = []
        self.allOverstatus = []
        self.target = None
    def show_score_board(self):
        print(f"*{self.currentBattingList[0].playerName} - {self.currentBattingList[0].runBat} ({self.currentBattingList[0].usedBall})", end="\t")
        print(f"{self.currentBattingList[1].playerName} - {self.currentBattingList[1].runBat} ({self.currentBattingList[1].usedBall})")
        print(f"{self.battingTeam.teamName[:3].upper()} Total Run : ({self.totalRun}-{self.totalWickets})W")
        print(f"Overs:({self.totalOver}.{self.currentBall})Ball")
        if self.currentBowler != None:
            print(f"Bowler Name : {self.currentBowler.playerName}  Give runs : {self.currentBowler.runBall} Bowl : {self.currentBowler.ballBowld}")
        if self.currentBall > 0:
            print("Current Over - ",end="")
            for i in self.currentOverStatus:
                print(i,end=" ")
            print("\n")
        if self.currentBall == 0 and self.totalOver > 0:
            print("Last Over - ",end="")
            for i in self.allOverstatus[-1]:
                print(i,end=" ")
            print("\n")
        if self.target is not None:
            print(f"Target : {self.target}")
            if self.target > self.totalRun:
                print(f"Need {self.target - self.totalRun}'runs from {12-self.totalOver*6 + self.currentBall} balls.")
    def entry_bowler(self,bowlerNameObj):
        self.currentBowler = bowlerNameObj

    def playBowl(self,status):
        run = 0
        extraRun = 0
        isNoBall = False
        isWide = False
        willStrikeChange = False
        isWicket = False
        if status[0] >= '0' and status[0] <= '9':
            run = int(status)
            if run%2 != 0:
                willStrikeChange = True
        else:
            if status[0] == 'W' and len(status) == 1:
                isWicket = True
            elif status[0] == 'N':
                isNoBall = True
                extraRun = 1
                run = int(status[1])
                if run%2 !=0:
                    willStrikeChange = True
            elif status[0] == 'W':
                isWide = True
                extraRun = 1+int(status[1])
                if int(status[1]) % 2 == 1:
                    willStrikeChange = True

        self.totalRun += run + extraRun
        self.striker.runBat += run
        if run == 4:
            self.striker.fours+=1
        if run == 6:
            self.striker.sixs += 1
        if isWide == False:
            self.striker.usedBall +=1
        self.currentBowler.runBall += run + extraRun
        self.currentOverStatus.append(status)
        if isWide == False and isNoBall == False:
            self.currentBowler.ballBowld += 1
            self.currentBall += 1
            if self.currentBall == 6:
                self.currentBall = 0
                self.totalOver += 1
                willStrikeChange = True
                self.allOverstatus.append(self.currentOverStatus)
                self.currentOverStatus = []
        

        if isWicket == True:
            if self.totalWickets > 9:
                return "end"
            print()
            print(f"Last wicket : {self.striker.playerName}\t Runs : {self.striker.runBat}\tPlayed {self.striker.usedBall}'Balls\tWicket taken by {self.currentBowler.playerName}")
            print(f"Strike rate : {self.striker.runBat*100/self.striker.usedBall}")
            print(f"Fours : {self.striker.fours}\tSix's : {self.striker.sixs}")
            self.currentBattingList[0] = self.battingTeam.playersName[self.currentBatsmanOrder]
            self.currentBatsmanOrder += 1
            self.striker = self.currentBattingList[0]
            self.totalWickets += 1
            self.currentBowler.wicketsTaken += 1
            print()

        if willStrikeChange == True:
            self.currentBattingList[0],self.currentBattingList[1] = self.currentBattingList[1],self.currentBattingList[0]
            self.striker = self.currentBattingList[0]
        
        return "0"
        



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
Ms = Player("Mahindra Singh Donni",india)

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

    # Fast ininngs start
    fastInnings = Innings(teamOneObj,teamTwoObj,battingTeamNameObj,bowlingTeamNameObj)
    fastInnings.show_score_board()
    print()
    over = 0
    while over < 2:
        isOff = False
        print("Choice a bowler : ")
        for index , name in enumerate(bowlingTeamNameObj.playersName):
            print(f"{index+1}. {name.playerName}")
        bowlerIndex = int(input("Enter player index : "))
        bowlerIndex -= 1
        bowlerNameObj = bowlingTeamNameObj.playersName[bowlerIndex]
        fastInnings.entry_bowler(bowlerNameObj)
        print("\n")

        while True:
            status = input("Enter status : ")
            recive = fastInnings.playBowl(status)
            if recive == "end":
                isOff = True
                break
            fastInnings.show_score_board()
            if (fastInnings.totalOver*6 + fastInnings.currentBall) % 6 == 0:
                break 
        print("\n")
        over += 1
        if isOff == True:
            break
    print(f"Target is {fastInnings.totalRun+1}")
    # Second ininngs start
    battingTeamNameObj,bowlingTeamNameObj = bowlingTeamNameObj,battingTeamNameObj
    secondInnings = Innings(teamOneObj,teamTwoObj,battingTeamNameObj,bowlingTeamNameObj)
    secondInnings.target = fastInnings.totalRun + 1
    over = 0
    while over < 2:
        isOff = False
        print("Choice a bowler : ")
        for index , name in enumerate(bowlingTeamNameObj.playersName):
            print(f"{index+1}. {name.playerName}")
        bowlerIndex = int(input("Enter player index : "))
        bowlerIndex -= 1
        bowlerNameObj = bowlingTeamNameObj.playersName[bowlerIndex]
        secondInnings.entry_bowler(bowlerNameObj)
        print("\n")

        while True:
            status = input("Enter status : ")
            recive = secondInnings.playBowl(status)
            if recive == "end":
                isOff = True
                break
            secondInnings.show_score_board()
            if (secondInnings.totalOver*6 + secondInnings.currentBall) % 6 == 0:
                break 
        over += 1
        if isOff == True:
            break
    if secondInnings.totalRun >= secondInnings.target:
        print(f"{secondInnings.battingTeam.teamName} wins.")
    else:
        print(f"{secondInnings.BowlingTeam.teamName} wins.")
    break
            


