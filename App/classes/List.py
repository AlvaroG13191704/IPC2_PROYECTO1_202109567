


from classes.Node import Node


class List_for_cells:
    #constructor
    def __init__(self,) -> None:
        self.size = 0
        self.head: Node  = None
    
    #Insert a Node 
    def append(self,value):
        if self.head == None:
            self.head = Node(self.size,value)
        else:
            aux = self.head
            while aux.next != None:
                aux = aux.next
            aux.next = Node(self.size,value)
        
        self.size += 1

    #for convert a a linkedlist to matrix we need to use row mayor
    def row_mayor(self,x,y,m):
        return x + y*m
    
    #Then we create a matrix 
    def create_matrix(self,size):
        for i in range(size):
            self.append(None)
    
    #Options to get and set the value

    def get_pos(self,x,y,m):
        pos = self.row_mayor(y,x,m)
        aux = self.head

        while aux != None:
            if aux.pos == pos:
                return  aux.value #f'({aux.value.x},{aux.value.y} - {aux.value.getSymbol()})'
            aux = aux.next
        return 'No object was found'
    
    def edit_pos(self,value,x,y,m):
        pos = self.row_mayor(y,x,m)
        aux = self.head
        
        while aux != None:
            if aux.pos == pos:
                aux.value = value
                break
            aux = aux.next
    

