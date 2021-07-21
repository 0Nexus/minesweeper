class Piece():
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False

    def getHasBomb (self):
        return self.hasBomb
    def getClicked  (self):
        return self.clicked
    def getFlagged(self):
        return self.flagged
    def setNeighbhors(self, neighbhors):
        self.neighbhors = neighbhors
        self.setNumAround()
    def setNumAround(self):
        self.numAround = 0
        for piece in self.neighbhors:
            if (piece.getHasBomb()):
                self.numAround += 1
    def getNumAround(self):
        return self.numAround

    def toggleFlag(self):
        self.flagged = not self.flagged

    def click(self):
        self.clicked = True
    def getNeighbors(self):
        return self.neighbhors