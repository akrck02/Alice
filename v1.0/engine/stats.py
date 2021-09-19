class stats :
    def __init__(self) :
        self.love = 0
        self.happyness = 0
        self.anger = 0

    def add_love(self, value) :
        self.love += value
    
    def add_happyness(self, value) :
        self.happyness += value
    
    def add_anger(self, value) :
        self.anger += value
