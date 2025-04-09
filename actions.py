from playeraction import PlayerActionScreen
class Action:
    def __init__(self, hitID, shooterID, redIDList, greenIDList, redScoreList, greenScoreList, master):
        self.hitID = hitID
        self.shooterID = shooterID
        self.redshooter = False
        self.redhit = False
        self.greenshooter = False
        self.greenhit = False
        self.redIDList = redIDList
        self.greenIDList = greenIDList
        self.redScoreList = redScoreList
        self.greenScoreList = greenScoreList
        self.redBasecounter = {}
        self.greenBasecounter = {}
        self.master = master
        self.team_or_enemy(self.hitID, self.shooterID)
    def team_or_enemy(self, hit, shoot):
        for ID in self.redIDList:
            if shoot == ID:
                self.redshooter = True
            if hit == ID:
                self.redhit = True
        if(self.redshooter == False):
            self.greenshooter = True
        if(self.redhit == False):
            self.greenhit = True
        
        if hit == 43:
            self.greenBaseHit(shoot)
        elif hit == 53:
            self.redBaseHit(shoot)
        elif(self.greenhit and self.greenshooter or self.redhit and self.redshooter):
            self.teamHit(self.shooterID)
        else:
            self.enemyHit(self.shooterID)

    def teamHit(self, shoot):
        if(self.greenshooter == True):
            for i in range(len(self.greenIDList)):
                if(shoot == self.greenIDList[i]):
                    self.greenScoreList[i] -= 10
        else:
            for i in range(len(self.redIDList)):
                if(shoot == self.redIDList[i]):
                    self.redScoreList[i] -= 10

    def enemyHit(self, shoot):
        if(self.greenshooter == True):
            for i in range(len(self.greenIDList)):
                if(shoot == self.greenIDList[i]):
                    self.greenScoreList[i] += 10

                    
        else:
            for i in range(len(self.redIDList)):
                if(shoot == self.redIDList[i]):
                    self.redScoreList[i] += 10
    def greenBaseHit(self, shooter):
        if(self.redshooter):
            if shooter in self.greenBasecounter:
                self.greenBasecounter[shooter] += 1
                if(self.greenBasecounter[shooter] > 3):
                    pass
                if(self.greenBasecounter[shooter] == 3):
                    for i in range(len(self.redIDList)):
                        if(shooter == self.redIDList[i]):
                            self.redScoreList[i] += 100

            else:
                self.greenBasecounter[shooter] = 1
        else:
            pass

    def redBaseHit(self, shooter):
        if(self.greenshooter):
            if shooter in self.redBasecounter:
                self.redBasecounter[shooter] += 1
                if(self.redBasecounter[shooter] > 3):
                    pass
                print(self.redBasecounter)
                if(self.redBasecounter[shooter] == 3):
                    for i in range(len(self.greenIDList)):
                        if(shooter == self.greenIDList[i]):
                            self.greenScoreList[i] += 100
            else:
                self.redBasecounter[shooter] = 1
        else:
            pass
