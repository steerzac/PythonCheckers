class CheckerPiece():
    idVal = 0
    row = 0
    column = 0
    color = ""
    king = False
    neNeighbor = []
    nwNeighbor = []
    seNeighhbor = []
    swNeighbor = []
    
    def __init__(self, row_, column_, color_, king_, idVal_):
        self.row = row_
        self.column = column_
        self.king = king_
        self.color = color_
        self.idVal = idVal_
        self.assignNeighbors()
        
    def getRow(self):
        return self.row
    
    def getColumn(self):
        return self.column
    
    def getColor(self):
        return self.color
    
    def isKing(self):
        return self.king
    
    def getIDVal(self):
        return self.idVal
    
    def setToKing(self):
        self.king = True
    
    def getNEneighbor(self):
        return self.neNeighbor
    
    def getNWneighbor(self):
        return self.nwNeighbor
    
    def getSEneighbor(self):
        return self.seNeighhbor
    
    def getSWneighbor(self):
        return self.swNeighbor
        
    #Description: assign the checker's neighbors tiles. If a neighbor tile does not exist, either its row or column will equal 100 
    def assignNeighbors(self):
        #Declare default values for function variables
        northRow = 100
        southRow = 100
        eastCol = 100
        westCol = 100
        
        #Check if the neighboring row or column exists
        #If it does exists, save it to a variable
        if (self.row - 1) >= 0:
            northRow = self.row - 1
        if (self.row + 1) <= 7:
            southRow =  self.row + 1
        if (self.column - 1) >= 0:
            westCol = self.column - 1
        if (self.column + 1) <= 7:
            eastCol = self.column + 1
        
        #Assign all neighbors with variable values
        self.neNeighbor = (northRow, eastCol)
        self.nwNeighbor = (northRow, westCol)
        self.seNeighhbor = (southRow, eastCol)
        self.swNeighbor = (southRow, westCol)
    
    #Description: updates checker's location. reassigns neighbors, sets self to king if checker became a king
    def updateLocation(self, row_, column_):
        self.row = row_
        self.column = column_
        self.assignNeighbors()
        if row_ == 0 and self.color == "red":
            if not self.isKing():
                self.setToKing()
        if row_ == 7 and self.color == "grey":
            if not self.isKing():
                self.setToKing()
    
    def printLocation(self):
        print "Location: (%s, %s)" % (self.column, self.row)
    
    def printInfo(self):
        print "Location: (%s, %s)" % (self.column, self.row),
        print ("King: %s" % self.king)