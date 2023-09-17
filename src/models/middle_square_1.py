import secrets
class Middle_square:

    def __init__(self, min, max):
        self.max = max
        self.min = min
        self.seed = secrets.randbits(64) 
        
    def middle_square(self):
        print(self.seed)
        squared = self.seed * self.seed
        squared_str = str(squared)
        print(f"{len(squared_str)}     j")
        print(f"{len(squared_str)}     j22")
        print(squared_str)
        middle = squared_str[int((len(squared_str)/2))-2:int((len(squared_str)/2))+2]
        print(f"{middle}  {int((len(squared_str)/2))-2}  {int((len(squared_str)/2))+2}    {len(squared_str)}")   
        new_seed = int(middle)/10000.0
        middle = middle.zfill(8)
        self.seed = int (middle)

        return new_seed
    def generateNi(self):
        number = self.min + (self.max - self.min) * self.middle_square()
        print(number)
        return number
    
m = Middle_square(0,1)
print(m.generateNi())









