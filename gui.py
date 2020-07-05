# GUI.py
import pygame
from main import solve, valid
import time
pygame.font.init()


class Grid:
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self. cols = cols
        self.width = width
        self.height = height
        self.cubes = [[Cube(self.board[j][i], j, i, width, height) for i in range(cols)] for j in range(rows)]
        self.model = None
        self.selected = None

    def update_model(self):
        self.model = [[self.cubes[j][i].value for i in range(self.cols)] for j in range(self.rows)]

    def place(self, val):
        row, col = self.selected
        if self.cubes[col][row].value = 0:
            self.cubes[col][row].set(val)
            self.update_model()

            if valid(self.model, val, (col, row)) and solve(self.model):
                return True
            else:
                self.cubes[col][row].set(0)
                self.cubes[col][row].set_temp(0)
                self.update_model()
                return False

    def sketch(self, val):
        col, row = self.selected
        self.cubes[col][row].set_temp(val)

    def draw(self, win):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0, 0, 0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i*gap, 0), (i*gap, self.height), thick)

        # Draw cubes
        for j in range(self.rows):
            for i in range(self.cols):
                self.cubes[j][i].draw(win)

    def select(self, col, row):
        # Reset all other
        for j in range(self.rows):
            for i in range(self.cols):
                self.cubes[j][i].selected = False

        self.cubes[col][row].selected = True
        self.selected = (col, row)

    def clear(self):
        col, row = self.selected
        if self.cubes[col][row].value == 0:
            self.cubes[col][row].set_temp(0)

    def click(self, pos):
        '''
        :param pos:
        :return:
        '''
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            y = pos[0] // gap
            x = pos[1] // gap
            return (int(y), int(x))
        else:
            return None

    def is_finished(self):
        for j in range(self.rows):
            for i in range(self.cols):
                if self.cubes[j][i].value == 0:
                    return False
        return True


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, col, row, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.Sysfont("comicsans", 40)

        gap = self.width / 9
        y = self.row * gap
        x = self.col * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128, 128, 128))
            win.blit(text, (x+5, y+5))
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))
