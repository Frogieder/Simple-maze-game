from collections import deque
from random import *


class Maze():
    def __init__(self, player, canvas, y, x):
        self.player = player
        self.canvas = canvas
        self.size = {"x": 2 * x - 1,
                     "y": 2 * y - 1}

    # 0 = air, 1 = wall, 2 = player. 3 = target
    def generate(self):
        
        def UnvisitedNeighbours(cell):
            neighbours = []
            if cell[0] + 2 < self.size["x"]:
                if maze[cell[0] + 2][cell[1]]:
                    neighbours.append("r")
            if cell[0] - 2 >= 0:
                if maze[cell[0] - 2][cell[1]]:
                    neighbours.append("l")
            if cell[1] + 2 < self.size["y"]:
                if maze[cell[0]][cell[1] + 2]:
                    neighbours.append("u")
            if cell[1] - 2 >= 0:
                if maze[cell[0]][cell[1] - 2]:
                    neighbours.append("d")
            return neighbours

        stack = deque()
        maze = []
        for i in range(self.size["x"]):
            maze.append([True] * (self.size["y"]))
        
        # Choose the initial cell, mark it as visited and push it to the stack
        current_cell = [randrange(2, self.size["x"], 2), randrange(2, self.size["y"], 2)]
        maze[current_cell[0]][current_cell[1]] = False
        stack.append(current_cell)
        # While the stack is not empty
        while(len(stack) > 0):
            # Pop a cell from the stack and make it a current cell
            current_cell = stack.pop()
            # maze[current_cell[0]][current_cell[1]] = False
            # If the current cell has any neighbours which have not been visited
            if len(neighbours := UnvisitedNeighbours(current_cell)):
                # Push the current cell to the stack
                stack.append(current_cell)
                # Choose one of the unvisited neighbours
                direction = choice(neighbours)
                # Remove the wall between the current cell and the chosen cell
                if direction == "u":
                    maze[current_cell[0]][current_cell[1] + 1] = False
                    maze[current_cell[0]][current_cell[1] + 2] = False
                    stack.append([current_cell[0], current_cell[1] + 2])
                elif direction == "d":
                    maze[current_cell[0]][current_cell[1] - 1] = False
                    maze[current_cell[0]][current_cell[1] - 2] = False
                    stack.append([current_cell[0], current_cell[1] - 2])
                elif direction == "l":
                    maze[current_cell[0] - 1][current_cell[1]] = False
                    maze[current_cell[0] - 2][current_cell[1]] = False
                    stack.append([current_cell[0] - 2, current_cell[1]])
                elif direction == "r":
                    maze[current_cell[0] + 1][current_cell[1]] = False
                    maze[current_cell[0] + 2][current_cell[1]] = False
                    stack.append([current_cell[0] + 2, current_cell[1]])
        
        maze[0][0] = 2

        self.maze = maze

        """
            Choose the initial cell, mark it as visited and push it to the stack
            While the stack is not empty
            Pop a cell from the stack and make it a current cell
            If the current cell has any neighbours which have not been visited
            Push the current cell to the stack
            Choose one of the unvisited neighbours
            Remove the wall between the current cell and the chosen cell
            Mark the chosen cell as visited and push it to the stack
        """

    def build(self, player, scale):
        self.scale = scale
        self.obstacles = []
        self.player = player
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                if self.maze[y][x] == 1:
                    self.obstacles.append(self.canvas.create_rectangle(
                        x * self.scale, y * self.scale,
                        x * self.scale + self.scale, y * self.scale + self.scale,
                        fill="black"))
                elif self.maze[y][x] == 2:
                    player.setCoords((x + 0.5) * scale, (y + 0.5) * scale)
                    self.playerCoords = {"x": x, "y": y}

    def canMove(self, _direction, move=False):
        newPos = []
        direction = _direction.lower()
        if direction == "up":
            newPos = [self.playerCoords["x"], self.playerCoords["y"] - 1]
        elif direction == "down":
            newPos = [self.playerCoords["x"], self.playerCoords["y"] + 1]
        elif direction == "left":
            newPos = [self.playerCoords["x"] - 1, self.playerCoords["y"]]
        elif direction == "right":
            newPos = [self.playerCoords["x"] + 1, self.playerCoords["y"]]
        else:
            raise ValueError("Unknown direction: " + direction +
                             ". Direction must be one of these: up, down, left, right (ignore case).")

        # out of maze bounds
        if newPos[0] < 0 or newPos[1] < 0:
            return False
        if newPos[1] > len(self.maze) - 1:
            return False
        if newPos[0] > len(self.maze[newPos[1]]) - 1:
            return False
        # obstacle
        if self.maze[newPos[1]][newPos[0]] == 1:
            return False

        if move:
            self.playerCoords["x"] = newPos[0]
            self.playerCoords["y"] = newPos[1]

        return True
