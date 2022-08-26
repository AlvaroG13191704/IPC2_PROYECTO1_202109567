
# This class represent a cell infected or not in the matrix
class Cell:
    def __init__(self,x,y,infected,n_infected,pos=0) -> None:
        self.x = x
        self.y = y
        self.infected = infected
        self.post_infected =n_infected
        self.pos = pos
        self.next = None
        
    def getSymbol(self):
        if self.infected == False:
            return '█'
        else:
            return '▒'
    
    def get_num(self):
        return self.post_infected


    
    