#Tic Tac Toe - Init
#Create box class
class box:
    def __init__(self,length = 1, width = 1, height = 1):
        self.length = length
        self.width = width
        self.height = height
    #Method to calculate volume
    def get_volume(self):
        return self.length * self.width * self.height

#Begin Program
newBox = box(height = 5)
print(newBox.length)

#This stuff isn't in the branch
