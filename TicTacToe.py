#Tic Tac Toe - Init
import math
#Create box class
class box:
    def __init__(self,length = 1, width = 1, height = 1):
        self.length = length
        self.width = width
        self.height = height
    #Method to calculate volume
    def get_volume(self):
        return self.length * self.width * self.height
class sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_volume(self):
        return round((4/3)*math.pi**3,2)

#Begin Program
newBox = box(height = 5)
newSphere = sphere(3)
print(newSphere.get_volume())