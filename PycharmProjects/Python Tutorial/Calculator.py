class Numbers:
    MULTIPLIER = 3.5
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    @classmethod
    def multiply(cls,a):
        return a*cls.MULTIPLIER
    @staticmethod
    def substract(b,c):
        return b - c
    @property
    def value(self):
        return (self.x,self.y)
    @value.setter
    def value(self,xy_tuple):
        self.x , self.y = xy_tuple
    @value.deleter
    def value(self):
        print('Deleted values')
        del self.x
        del self.y
print("This is an imported file !!")
test = 100

