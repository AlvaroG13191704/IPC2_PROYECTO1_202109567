#Patient class
class Patient:

    #Constructor
    def __init__(self,name,age,period,matrix) -> None:
        self.__name = name,
        self.__age = age,
        self.__period = period,
        self.__matrix = matrix
    
    #Getters and setters
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @property
    def period(self):
        return self.__period
    @property
    def period(self):
        return self.__matrix


