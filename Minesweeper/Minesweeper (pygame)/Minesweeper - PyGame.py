import random
import numpy as np
import time
import pygame as pg
from pygame.locals import *
import sys


pg.init()

class Minesweeper:
    def __init__(self, width = 10, height = 10, bombcount = 10, winwidth = 1000, winheight = 1000):
        self.screen = pg.display.set_mode((winwidth, winheight))
        self.width = width
        self.height = height
        self.screenwidth = winwidth
        self.screenheight = winheight
        self.tilesize = min(self.screenwidth, self.screenheight) // max(self.width, self.height) // 5 * 4
        self.opening = pg.image.load('opening.png')
        self.won = pg.image.load('won.png')
        self.lost = pg.image.load('lost.png')
        self.pressed_img = pg.image.load('pressed.png')
        self.unpressed_img = pg.image.load('unpressed.png')
        self.one_img = pg.image.load('1.png')
        self.two_img = pg.image.load('2.png')
        self.three_img = pg.image.load('3.png')
        self.four_img = pg.image.load('4.png')
        self.five_img = pg.image.load('5.png')
        self.six_img = pg.image.load('6.png')
        self.seven_img = pg.image.load('7.png')
        self.eight_img = pg.image.load('8.png')
        self.mine_img = pg.image.load('mine.png')
        self.flag_img = pg.image.load('flag.png')
        self.tilestart = (self.screenwidth - self.tilesize * self.width) // self.width // 2
        self.bombcount = bombcount
        self.safezone = set()
        self.bombmap = np.zeros((self.height, self.width)) # 0 = no bomb, 1 = bomb
        self.gamemap = np.zeros((self.height, self.width)) # 0 = empty, num = num, -1 = bomb
        self.visiblemap = np.zeros((self.height, self.width)) # 0 = not visible, 1 = visible, 2 = flagged
        self.state = 'First' #becomes 'Continue', then 'Win' or 'Loss'

    def transform_imgs(self):
        self.opening = pg.transform.scale(self.opening, (self.screenwidth, self.screenheight))
        self.won = pg.transform.scale(self.won, (self.screenwidth, self.screenheight))
        self.lost = pg.transform.scale(self.lost, (self.screenwidth, self.screenheight))
        self.pressed_img = pg.transform.scale(self.pressed_img, (self.tilesize,self.tilesize))
        self.unpressed_img = pg.transform.scale(self.unpressed_img, (self.tilesize,self.tilesize))
        self.one_img = pg.transform.scale(self.one_img, (self.tilesize,self.tilesize))
        self.two_img = pg.transform.scale(self.two_img, (self.tilesize,self.tilesize))
        self.three_img = pg.transform.scale(self.three_img, (self.tilesize,self.tilesize))
        self.four_img = pg.transform.scale(self.four_img, (self.tilesize,self.tilesize))
        self.five_img = pg.transform.scale(self.five_img, (self.tilesize,self.tilesize))
        self.six_img = pg.transform.scale(self.six_img, (self.tilesize,self.tilesize))
        self.seven_img = pg.transform.scale(self.seven_img, (self.tilesize,self.tilesize))
        self.eight_img = pg.transform.scale(self.eight_img, (self.tilesize,self.tilesize))
        self.mine_img = pg.transform.scale(self.mine_img, (self.tilesize,self.tilesize))
        self.flag_img = pg.transform.scale(self.flag_img, (self.tilesize,self.tilesize))

    def generate_safezone(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.safezone.add((x + i, y + j))

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
                    self.bombmap[y, x] = 1

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
                    self.gamemap[x, y] = -1
                else:
                    self.gamemap[x, y] = self.check_around(x, y)

    def generate_grid(self):
        for x in range(self.width):
            for y in range(self.height):
                self.screen.blit(self.unpressed_img, (self.tilestart + x * self.tilesize, self.tilestart + y * self.tilesize))
        pg.display.update()
    
    def update_grid(self):
        self.screen.fill((240,240,240))
        self.generate_grid()
        for x in range(self.width):
            for y in range(self.height):
                if self.visiblemap[y, x] == 1:
                    self.screen.blit(self.pressed_img, (self.tilestart + x * self.tilesize, self.tilestart + y * self.tilesize))
                    if self.gamemap[y, x] == -1:
                        self.screen.blit(self.mine_img, (self.tilestart + x * self.tilesize, self.tilestart + y * self.tilesize))
                    elif self.gamemap[y, x] == 1:
                        self.screen.blit(self.one_img, (self.tilestart + x * self.tilesize, self.tilestart + y * self.tilesize))
                    elif self.gamemap[y, x] == 2:
                        self.screen.blit(self.two_img, (self.tilestart + x * self.tilesize, self.tilestart + y * self.tilesize))
                    elif self.gamemap[y, x] == 3:
                        self.screen.blit(self.three_img, (self.tilestart + x * self.tilesize, self.tilestart + y * self.tilesize))
                    elif self.gamemap[y, x] == 4:
                        self.screen.blit(self.four_img, (self.tilestart + x * self.tilesize, self.tilestart + y * self.tilesize))
                    elif self.gamemap[y, x] == 5:
                        self.screen.blit(self.five_img, (self.tilestart + x * self.tilesize, self.tilestart + y * self.tilesize))
                    elif self.gamemap[y, x] == 6:
                        self.screen.blit(self.six_img, (self.tilestart + x * self.tilesize, self.tilestart + y * self.tilesize))
                    elif self.gamemap[y, x] == 7:
                        self.screen.blit(self.seven_img, (self.tilestart + x * self.tilesize, self.tilestart + y * self.tilesize))
                    elif self.gamemap[y, x] == 8:
                        self.screen.blit(self.eight_img, (self.tilestart + x * self.tilesize, self.tilestart + y * self.tilesize))
                elif self.visiblemap[y, x] == 2:
                    self.screen.blit(self.flag_img, (self.tilestart + x * self.tilesize, self.tilestart + y * self.tilesize))
        pg.display.update()

    def reveal_around(self, x, y):
        self.visiblemap[y, x] = 1
        if self.gamemap[y, x] == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if x + i < 0 or x + i >= self.width:
                        continue
                    if y + j < 0 or y + j >= self.height:
                        continue
                    if self.visiblemap[y + j, x + i] == 0:
                        if self.bombmap[y + j, x + i] != 1:
                            self.visiblemap[y + j, x + i] = 1
                            if self.gamemap[y + j, x + i] == 0:
                                self.reveal_around(x + i, y + j)
                    
    def win_screen(self):
        start = time.time()
        self.screen.blit(self.won, (0, 0))
        pg.display.update()
        while time.time() - start < 10:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN or event.type == KEYDOWN:
                    return None

    def lose_screen(self):
        start = time.time()
        self.screen.blit(self.lost, (0, 0))
        pg.display.update()
        while time.time() - start < 10:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN or event.type == KEYDOWN:
                    return None

    def opening_screen(self):
        start = time.time()
        self.screen.blit(self.opening, (0, 0))
        pg.display.update()
        while time.time() - start < 10:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN or event.type == KEYDOWN:
                    return None

    def userclick(self):
        for event in pg.event.get():
            if event == QUIT or (event.type == KEYDOWN):
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pg.mouse.get_pos()
                    if self.state == 'Continue':
                        if x < self.tilestart or x > self.screenwidth//self.width * self.tilesize + self.tilestart:
                            continue
                        for i in range(self.width):
                            if x < self.tilestart + self.tilesize*(i+1):
                                x = i
                                break
                            
                        if y < self.tilestart or y > self.screenheight//self.height * self.tilesize + self.tilestart:
                            continue
                        for j in range(self.height):
                            if y < self.tilestart + self.tilesize*(j+1):
                                y = j
                                break
                        
                        try:
                            self.visiblemap[y, x] = 1
                            if self.bombmap[y, x] == 1:
                                self.state = 'Loss'
                                self.update_grid()
                            elif self.bombcount == np.count_nonzero(self.visiblemap == 2) + np.count_nonzero(self.visiblemap == 0):
                                self.state = 'Win'
                                self.update_grid()
                            else:
                                self.reveal_around(x, y)
                                self.update_grid()
                        except IndexError:
                            pass
                        
                    elif self.state == 'First':
                        if x < self.tilestart or x > self.screenwidth - self.tilestart:
                            continue
                        for i in range(self.width):
                            if x < self.tilestart + self.tilesize*(i+1):
                                x = i
                                break
                            
                        if y < self.tilestart or y > self.screenheight - self.tilestart:
                            continue
                        for j in range(self.height):
                            if y < self.tilestart + self.tilesize*(j+1):
                                y = j
                                break

                        try:
                            self.generate_safezone(x, y)
                            self.generate_bombmap()
                            self.generate_playermap()
                            self.visiblemap[y, x] = 1
                            self.reveal_around(x, y)
                            self.update_grid()
                            self.state = 'Continue'
                        except IndexError:
                            pass
                elif event.button == 3:
                    x, y = pg.mouse.get_pos()
                    if self.state == 'Continue' or self.state == 'First':
                        if x < self.tilestart or x > self.screenwidth//self.width * self.tilesize + self.tilestart:
                            continue
                        for i in range(self.width):
                            if x < self.tilestart + self.tilesize*(i+1):
                                x = i
                                break
                            
                        if y < self.tilestart or y > self.screenheight//self.height * self.tilesize + self.tilestart:
                            continue
                        for j in range(self.height):
                            if y < self.tilestart + self.tilesize*(j+1):
                                y = j
                                break
                        
                        try:
                            if self.visiblemap[y, x] == 0:
                                if self.bombcount == np.count_nonzero(self.visiblemap == 2) + np.count_nonzero(self.visiblemap == 0):
                                    self.state = 'Win'
                                    print('You win')
                                    self.update_grid()
                                else:
                                    self.visiblemap[y, x] = 2
                                    self.update_grid()
                            elif self.visiblemap[y, x] == 2:
                                if not self.bombcount == np.count_nonzero(self.visiblemap == 2) + np.count_nonzero(self.visiblemap == 0):
                                    self.visiblemap[y, x] = 0
                                    self.update_grid()
                        except IndexError:
                            pass
            
    def play(self):
        self.transform_imgs()
        self.opening_screen()
        self.screen.fill((240,240,240))
        self.generate_grid()
        while self.state == 'Continue' or self.state == 'First':
            self.userclick()
        if self.state == 'Loss':
            self.lose_screen()
        elif self.state == 'Win':
            self.win_screen()

while True:
    game = Minesweeper(7,7,7)
    game.play()