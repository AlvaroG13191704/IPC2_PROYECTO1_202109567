
# This is part of the EDD 
class Node: 
    def __init__(self,pos=0,value=None) -> None:
        self.pos = pos
        self.value = value
        self.next = None