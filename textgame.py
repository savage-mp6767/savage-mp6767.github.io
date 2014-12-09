def ReverseDirection(di):
    if di == "up":
        return "down"
    if di == "left":
        return "right"
    if di == "right":
        return "left"
    if di == "down":
        return "up"

class MapCell():
    def __init__(self,name,parent):
        self.name = name
        self.parent = parent
        self.id = parent.GetCellID()
        self.neighbors = []
        self.sides = {}
        self.sides['left'] = ""
        self.sides['right'] = ""
        self.sides['up'] = ""
        self.sides['down'] = ""
    
    def SetNeighbor(self,side,cell):
        self.sides[side] = cell
        self.sides[ReverseDirection(side)] = cell
        cell.SetNeighbor(ReverseDirection(side)) = self
        print(self.name + '.sides[' + str(side) + '] = ' + str(cell.name))
    
    def GetNeighbor(self,side): #up down left right
        return self.sides[side]

class Map():
    def __init__(self):
        self.cells = []
        self.currcell = ""
    
    def AddCell(self,cell):
        if len(self.cells) == 0:
            self.currcell = cell
            
        self.cells.append(cell)
    
    def GetCellID(self):
        return len(self.cells) + 1
        
    def GetCellByID(self,i):
        for c in self.cells:
            if c.id == i:
                return c
        
class Game():
    def __init__(self):
        self.map = Map()

    def MainLoop(self):
        print(self.map.currcell.name)
        print('left or right?')
        inp = input()
        if inp == 'left':
            self.map.currcell = self.map.currcell.GetNeighbor('left')
        elif inp == 'right':
            self.map.currcell = self.map.currcell.GetNeighbor('right')
        elif inp == 'up':
            self.map.currcell = self.map.currcell.GetNeighbor('up')
        elif inp == 'down':
            self.map.currcell = self.map.currcell.GetNeighbor('down')
        elif inp == 'listcells':
            for cell in self.map.cells:
                print(cell.name)
        elif inp == 'addcell':
            print('Direction')
            di = input()
            self.map.AddCell(MapCell(self.map.currcell.name + str(di),self.map))
            self.map.currcell.SetNeighbor(str(di),self.map.cells[len(self.map.cells) - 1])
        elif inp == 'listneighbors':
            print(self.map.curcell.sides)
        self.MainLoop()

game = Game()
center = MapCell("center (0,0)",game.map)
left = MapCell("leftofcenter (-1,0)",game.map)
right = MapCell("rightofcenter (1,0)",game.map)
up = MapCell("abovecenter (0,1)",game.map)
down = MapCell("belowcenter (0,-1)",game.map)

center.SetNeighbor('left',left)
center.SetNeighbor('right',right)
center.SetNeighbor('up',up)
center.SetNeighbor('down',down)

game.map.AddCell(center)
game.map.AddCell(left)
game.map.AddCell(up)
game.map.AddCell(down)
game.MainLoop()
