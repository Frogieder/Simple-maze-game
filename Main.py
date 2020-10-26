from Maze import *
from Player import *
import tkinter as tk

root = tk.Tk()
root.title = "Maze game"

scale = 20
Canvas = {"x": 1900,
          "y": 1020,
          "bg": "green"}

# create canvas for the game to take place on
canvas = tk.Canvas(root, bg=Canvas["bg"], width=Canvas["x"], height=Canvas["y"])
canvas.pack()

# create player
player = Circle(canvas, 25, 25, r=scale *.4, fill="red",
                outline="white", width=scale*0.07, speed=scale)
player.create()

# generate maze
maze = Maze(player, canvas, 48, 26)
maze.generate()
maze.build(player, scale)

# initialize controls
playerCtl = Buttons(player, maze)
canvas.bind_all("<w>", playerCtl.up)
canvas.bind_all("<s>", playerCtl.down)
canvas.bind_all("<a>", playerCtl.left)
canvas.bind_all("<d>", playerCtl.right)
canvas.bind_all("<Up>", playerCtl.up)
canvas.bind_all("<Down>", playerCtl.down)
canvas.bind_all("<Left>", playerCtl.left)
canvas.bind_all("<Right>", playerCtl.right)

root.mainloop()
