class Circle():
    def __init__(self, canvas, x=0, y=0, r=10,
                 fill="", outline="black", width=1,
                 speed=2):
        self.x = x
        self.y = y
        self.r = r
        self.fill = fill
        self.outline = outline
        self.width = width
        self.speed = speed
        self.canvas = canvas

    def create(self):
        self.id = self.canvas.create_oval(self.x - self.r,
                                     self.y - self.r,
                                     self.x + self.r,
                                     self.y + self.r,
                                     fill=self.fill,
                                     outline=self.outline,
                                     width=self.width)

    def moveUp(self):
        self.y -= self.speed
        self.updatePos()

    def moveDown(self):
        self.y += self.speed
        self.updatePos()

    def moveLeft(self):
        self.x -= self.speed
        self.updatePos()

    def moveRight(self):
        self.x += self.speed
        self.updatePos()

    def setCoords(self, x, y, r = "don't change"):
        self.x = x
        self.y = y
        if not r == "don't change":
            self.r = r
        self.updatePos()

    def setCoordsList(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.r = coords[2]

    def changeParams(self):
        pass
    def updatePos(self):
        self.canvas.coords(self.id, self.x - self.r, self.y -self.r,
                           self.x + self.r, self.y + self.r,)


class Buttons():
    def __init__(self, player, maze):
        self.player = player
        self.maze = maze
    def up(self, event):
        if self.maze.canMove("up", move=True):
            self.player.moveUp()

    def down(self, event):
        if self.maze.canMove("down", move=True):
            self.player.moveDown()

    def left(self, event):
        if self.maze.canMove("left", move=True):
            self.player.moveLeft()

    def right(self, event):
        if self.maze.canMove("right", move = True):
            self.player.moveRight()

