import math
import random
import numpy as np

class Map:
    
    def __init__(self, width, height, firstclick, bombcount):
        self.width = width
        self.height = height
        self.first_click = firstclick
        self.safezone = {self.first_click}
        self.bombcount = bombcount
        self.playermap = np.zeros((width, height))
        self.bombmap = np.zeros((width, height))
        self.visiblemap = np.empty((width, height), dtype=str)
        self.state = 'Continue'

    def generate_safezone(self):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self.first_click[0] + i < 0 or self.first_click[0] + i >= self.width:
                    continue
                if self.first_click[1] + j < 0 or self.first_click[1] + j >= self.height:
                    continue
                self.safezone.add((self.first_click[0] + i, self.first_click[1] + j))

    def generate_bombmap(self):
        num_bombs = self.bombcount
        bomb_list = set()
        while len(bomb_list) < num_bombs:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.safezone:
                bomb_list.add((x, y))
        for x in range(self.width):
            for y in range(self.height):
                if (x, y) in bomb_list:
                    self.bombmap[x, y] = 1
                else:
                    self.bombmap[x, y] = 0

    def check_around(self, x, y):
        total = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if x + i < 0 or x + i >= self.width:
                    continue
                if y + j < 0 or y + j >= self.height:
                    continue
                total += self.bombmap[x + i, y + j]
        return total

    def generate_playermap(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.bombmap[x, y] == 1:
                    self.playermap[x, y] = -1
                else:
                    self.playermap[x, y] = self.check_around(x, y)

    def generate_visiblemap(self):
        for x in range(self.width):
            for y in range(self.height):
                self.visiblemap[x, y] = ' '

    def show_visiblemap(self):
        print(self.visiblemap)

    def show_playermap(self):
        print(self.playermap)
    
    def show_bombmap(self):
        print(self.bombmap)
        
    def click(self, x, y):
        if self.visiblemap[x, y] == ' ':
            if self.playermap[x, y] == 0:
                self.visiblemap[x, y] = 'O'
                self.reveal_adjacent_zeroes(x, y)
            elif self.playermap[x, y] == -1:
                self.visiblemap[x, y] = 'X'
                self.state = 'Loss'
                print("You Lose.")
            else:
                self.visiblemap[x, y] = str(self.playermap[x, y])
            self.show_visiblemap()
        else:
            print('You have already clicked here!')
    
    def reveal_adjacent_zeroes(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if x + i < 0 or x + i >= self.width:
                    continue
                if y + j < 0 or y + j >= self.height:
                    continue
                if self.visiblemap[x + i, y + j] == ' ':
                    if self.playermap[x + i, y + j] == 0:
                        self.visiblemap[x + i, y + j] = 'O'
                        self.reveal_adjacent_zeroes(x + i, y + j)
                    elif self.playermap[x + i, y + j] == -1:
                        self.visiblemap[x + i, y + j] = 'X'
                    else:
                        self.visiblemap[x + i, y + j] = str(self.playermap[x + i, y + j])

    def check_win(self):
        if np.count_nonzero(self.visiblemap == ' ') == self.bombcount and self.state == 'Continue':
            self.state = 'Win'
            print('You win!')

    def play(self):
        if self.width > 3:
            self.generate_safezone()
        self.generate_bombmap()
        self.generate_playermap()
        self.generate_visiblemap()
        self.click(self.first_click[1], self.first_click[0])
        while self.state == 'Continue':
            print('-------------------------------------------------------------')
            x = int(input('Enter x coordinate: '))
            y = int(input('Enter y coordinate: '))
            self.click(y, x)
            self.check_win()


if __name__ == '__main__':
    mapsize = int(input("Enter map size: "))
    bombcount = int(input("Enter bomb count: "))
    print(np.empty((mapsize, mapsize), dtype=str))
    x = int(input('Enter x coordinate: '))
    y = int(input('Enter y coordinate: '))
    firstclick = (x, y)
    game = Map(mapsize, mapsize, firstclick, bombcount)
    game.play()
    a = input('Enter anything to exit: ')
