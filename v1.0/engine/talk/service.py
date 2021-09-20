import abc

class Italk (abc.ABC) : 
    @abc.abstractclassmethod
    def talk(self,message):
        pass

class TalkingService:
    
    def __init__(self):
        self.talkingSys = []

    def addTalkingSystem(self, sys):
        self.talkingSys.append(sys)
    
    def talk (self, text) :
        for sys in self.talkingSys : 
            sys.talk(text)