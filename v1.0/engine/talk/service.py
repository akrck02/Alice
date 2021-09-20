import abc

class Italk (abc.ABC) : 
    @abc.abstractclassmethod
    def talk(self,message):
        pass

class Service:
    
    def __init__(self):
        self.systems = []

    def addTalkingSystem(self, sys):
        self.systems.append(sys)
    
    def talk (self, text) :
        for sys in self.systems : 
            sys.talk(text)