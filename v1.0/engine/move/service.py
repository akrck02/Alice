from enum import Enum
import abc

class Directon(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
 
class Imove (abc.ABC) :
    @abc.abstractclassmethod
    def move(x,y): 
        pass

    @abc.abstractclassmethod
    def turn(grades):
        pass

    @abc.abstractclassmethod
    def grab():
        pass


class Service : 
    def __init__(self):
        self.systems = []

    def add_system(self,sys):
        slef.systems.append(sys)
