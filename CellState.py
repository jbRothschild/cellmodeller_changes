
class CellState:
    # Don't show these attributes in gui
    excludeAttr = ['id', 'divideFlag', 'ends','cellAdh']
    #Can add different states of the cell here.

    def __init__(self, cid):
        self.id = cid
        self.growthRate = 1.0
        self.color = [0.5,0.5,0.5]
        self.divideFlag = False
        self.deathFlag = False
        self.cellAge = 0
        self.neighbours = []
        self.effGrowth = 0.0
