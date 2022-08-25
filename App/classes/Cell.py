
# This class represent a cell infected or not in the matrix
class Cell:
    def __init__(self,x,y,infected,pos=0) -> None:
        self.x = x
        self.y = y
        self.infected = infected
        self.pos = pos
        self.next = None
        
    def getSymbol(self):
        if self.infected == False:
            return '█'
        else:
            return '▒'
    


    
    