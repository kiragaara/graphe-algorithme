class Node():
    
    def __init__(self , name ,label=None ,color=None, fill=None):
        self.name = name 
        self.label
        self.printcolor = color
        self.fill = fill 
        self.outneighbors = []
        self.inneighbors = []
        self.color = "W"


    def addneighbor(self,neighbor):
        self.outneighbors.append(neighbor)
        neighbor.inneighbors.append(self)
        
    def copy(self) :
        newnode = None(self.name ,self.label ,self.color, self.fill)
        newnode.outneighbors = self.outneighbors.copy()
        newnode.inneighbors  = self.inneighbors.copy()
    return newnode

    
