
from .Nodo import Nodo


class LinkedList:

    def __init__(self) -> None:
        self.primero = None
        self.tamaño = 0

    """
    - Primero creamos un nodo el cual toma el valor que le pasamos
    - Verifica el tamaño de la lista
        - Si esta vacía entonces el primero toma el valor del nodo que creamos
        - Sino entonces creamos una variable aux la cual le damos el valor del primero, 
          mientras el nodo siguiente sea diferente de None entonces   
    """
    def agregar(self,valor):
        mi_nodo = Nodo(valor)
        if self.tamaño == 0:
            self.primero = mi_nodo
        else:
            aux = self.primero
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = mi_nodo
        self.tamaño += 1
        
        return mi_nodo
    