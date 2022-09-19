import random
import time
import pygame as pg
from pygame.locals import *
import sys


pg.init()

font = pg.font.SysFont('timesnewroman.ttf', 72)

class Game:
    def __init__(self, size, speed, fac):
        self.width = size
        self.height = size
        self.fac = fac
        self.screen = pg.display.set_mode((size * self.fac, size * self.fac))
        self.foods = [] # list of positions of food on the screen
        self.snake = Snake((size//2,size//2))
        self.score = 0 # increments with each food eaten
        self.status = "Alive" # Alive, Loss, Win
        self.gamespeed = speed # seconds between each frame

        self.opening = pg.image.load("Opening.png")
        self.lost = pg.image.load("Lost.png")
        self.won = pg.image.load("Won.png")
        self.opening = pg.transform.scale(self.opening, (self.width*fac, self.height*fac))
        self.won = pg.transform.scale(self.won, (self.width*fac, self.height*fac))
        self.lost = pg.transform.scale(self.lost, (self.width*fac, self.height*fac))

    def foodupdate(self):
        while len(self.foods) == 0:
            pos = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if pos not in self.snake.snakebody and pos != self.snake.snakehead:
                self.foods.append(pos)

    def update(self):
        self.snake.snakebody.insert(0, self.snake.snakehead)
        self.snake.move()
        if len(self.snake.snakebody) > self.snake.snakesize:
            self.snake.snakebody.pop()
        if self.snake.snakehead in self.snake.snakebody[1:] or self.snake.snakehead[0] < 0 or self.snake.snakehead[0] >= self.width or self.snake.snakehead[1] < 0 or self.snake.snakehead[1] >= self.height:
            self.status = "Loss"
        if self.snake.snakehead in self.foods:
            self.foods.remove(self.snake.snakehead)
            self.foodupdate()
            self.snake.snakesize += 1
            self.score += 1
        if self.snake.snakesize == self.width * self.height - 1:
            self.status = "Win"

    def draw(self):
        self.screen.fill((0,0,0))
        for food in self.foods:
            pg.draw.rect(self.screen, (255, 75, 0), (food[0] * self.fac, food[1] * self.fac, self.fac*0.8, self.fac*0.8))
        for body in self.snake.snakebody:
            pg.draw.circle(self.screen, (0,200,0), (body[0] * self.fac + self.fac//2, body[1] * self.fac + self.fac//2), self.fac*0.40)
        pg.draw.circle(self.screen, (0,255,0), (self.snake.snakehead[0] * self.fac + self.fac//2, self.snake.snakehead[1] * self.fac + self.fac//2), self.fac*0.45)

    def input(self):
        for event in pg.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_w or event.key == K_UP and self.snake.direction != "S" and self.snake.lastdirection != "S":
                    self.snake.direction = "W"
                elif event.key == K_a or event.key == K_LEFT and self.snake.direction != "D" and self.snake.lastdirection != "D":
                    self.snake.direction = "A"
                elif event.key == K_s or event.key == K_DOWN and self.snake.direction != "W" and self.snake.lastdirection != "W":
                    self.snake.direction = "S"
                elif event.key == K_d or event.key == K_RIGHT and self.snake.direction != "A" and self.snake.lastdirection != "A":
                    self.snake.direction = "D"
                
    def run(self):
        self.opening_screen()
        self.foodupdate()
        self.draw()
        pg.display.update()
        while self.snake.direction == "":
            self.input()
        while self.status == "Alive":
            self.input()
            self.update()
            self.draw()
            pg.display.update()
            time.sleep(self.gamespeed)
        self.end_screen()
        if self.status == "Loss":
            self.lose_screen()
        elif self.status == "Win":
            self.win_screen()

    def win_screen(self):
        start = time.time()
        self.screen.blit(self.won, (0, 0))
        pg.display.update()
        while time.time() - start < 10:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pg.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE or event.key == K_RETURN:
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
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE or event.key == K_RETURN:
                        return None

    def end_screen(self):
        start = time.time()
        pg.display.update()
        while time.time() - start < 10:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pg.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE or event.key == K_RETURN:
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
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE or event.key == K_RETURN:
                        return None

class Settings:
    def __init__(self):
        self.gamespeed = 0
        self.gamesize = 0
        self.fac = 0
        self.screen = pg.display.set_mode((500, 500))

    def settings_screen(self):
        self.screen.fill((200,200,200))
        self.choosespeed()
        self.screen.fill((200,200,200))
        self.choosesize()
        self.screen.fill((200,200,200))
        self.choosefac()
        
    def choosespeed(self):
        img1 = font.render('Choose game speed', True, (75, 75, 150))
        self.screen.blit(img1, (10, 0))
        imgfast = font.render('Fast', True, (75, 75, 150))
        imgmedium = font.render('Medium', True, (75, 75, 150))
        imgslow = font.render('Slow', True, (75, 75, 150))
        self.screen.blit(imgfast, (0,250))
        self.screen.blit(imgmedium, (150,250))
        self.screen.blit(imgslow, (350,250))
        pg.display.update()
        while self.gamespeed == 0:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    x, y = pg.mouse.get_pos()
                    if y >= 200 and y <= 300:
                        if x >= 0 and x < 150:
                            self.gamespeed = 0.1
                        elif x >= 150 and x < 350:
                            self.gamespeed = 0.2
                        elif x >= 350 and x < 500:  
                            self.gamespeed = 0.3

    def choosesize(self):
        img2 = font.render('Choose game size', True, (75, 75, 150))
        self.screen.blit(img2, (10, 0))
        imgsmall = font.render('Small', True, (75, 75, 150))
        imgmedium = font.render('Medium', True, (75, 75, 150))
        imglarge = font.render('Large', True, (75, 75, 150))
        self.screen.blit(imgsmall, (0,250))
        self.screen.blit(imgmedium, (150,250))
        self.screen.blit(imglarge, (350,250))
        pg.display.update()
        while self.gamesize == 0:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    x, y = pg.mouse.get_pos()
                    if y >= 200 and y <= 300:
                        if x >= 0 and x < 150:
                            self.gamesize = 5
                        elif x >= 150 and x < 350:
                            self.gamesize = 10
                        elif x >= 350 and x < 500:  
                            self.gamesize = 20

    def choosefac(self):
        img3 = font.render('Choose screen size', True, (75, 75, 150))
        self.screen.blit(img3, (10, 0))
        imgsmall = font.render('Small', True, (75, 75, 150))
        imgmedium = font.render('Medium', True, (75, 75, 150))
        imglarge = font.render('Large', True, (75, 75, 150))
        self.screen.blit(imgsmall, (0,250))
        self.screen.blit(imgmedium, (150,250))
        self.screen.blit(imglarge, (350,250))
        pg.display.update()
        while self.fac == 0:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    x, y = pg.mouse.get_pos()
                    if y >= 200 and y <= 300:
                        if x >= 0 and x < 150:
                            self.fac = 300 // self.gamesize
                        elif x >= 150 and x < 350:
                            self.fac = 600 // self.gamesize
                        elif x >= 350 and x < 500:  
                            self.fac = 1000 // self.gamesize


class Snake:
    def __init__(self, position):
        self.snakehead = position # position of snakes head, (x,y), this is where the game registers the player
        self.snakesize = 1 # increments with each food eaten
        self.snakebody = [] # positions of each snake body part, len(self.snakebody) = snakesize - 1, function as walls that follow the head around
        self.direction = "" # Right (D), Left (A), Up (W), Down (S)
        self.lastdirection = "" # last direction the snake was moving in, used to prevent the snake from moving backwards

    def move(self):
        if self.direction == "D":
            self.snakehead = (self.snakehead[0] + 1, self.snakehead[1])
            self.lastdirection = "D"
        elif self.direction == "A":
            self.snakehead = (self.snakehead[0] - 1, self.snakehead[1])
            self.lastdirection = "A"
        elif self.direction == "W":
            self.snakehead = (self.snakehead[0], self.snakehead[1] - 1)
            self.lastdirection = "W"
        elif self.direction == "S":
            self.snakehead = (self.snakehead[0], self.snakehead[1] + 1)
            self.lastdirection = "S"

def __main__():
    settings = Settings()
    settings.settings_screen()
    game = Game(settings.gamesize, settings.gamespeed, settings.fac)
    game.run()

while True:
    __main__()
