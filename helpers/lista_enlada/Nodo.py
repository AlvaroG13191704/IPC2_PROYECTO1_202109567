class Nodo:
    def __init__(self,valor) -> None:
        self.__valor = valor
        self.__siguiente = None
    
    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self,valor):
        self.__valor = valor
    @property 
    def siguiente(self):
        return self.__siguiente
    @siguiente.setter
    def siguiente(self,sig):
        self.__siguiente = sig
    
    def __str__(self) -> str:
        return f'{self.__valor}'

#Creamos nuestro Nodo