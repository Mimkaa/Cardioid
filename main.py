import pygame as pg
import sys
from settings import *
from objects import *
from os import path
import math
vec = pg.Vector2
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        self.font=path.join("PixelatedRegular-aLKm.ttf")
    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)
        return text_rect

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.radius = 250
        self.points_num = 150
        self.angle =(math.pi*2)/self.points_num
        self.scale = 0


    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

        self.scale +=0.003
        # self.scale = self.scale%(math.pi*2)



    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)

        # draw a circle and points
        color = pg.Color(0,0,0,0)
        color.hsla = (int(math.degrees(self.scale % math.pi*2)), 100,50, 100)
        pg.draw.circle(self.screen,color,(WIDTH//2,HEIGHT//2), self.radius, 1)
        # for i in range(self.points_num):
        #     pg.draw.circle(self.screen,color,vec(WIDTH//2,HEIGHT//2)+vec(math.cos(self.angle*i),math.sin(self.angle*i))*self.radius,10)

        # drawing lines
        for i in range(self.points_num):
            pg.draw.line(self.screen,color,vec(WIDTH//2,HEIGHT//2)-vec(math.cos(self.angle*i ),math.sin(self.angle*i))*self.radius,
                         vec(WIDTH//2,HEIGHT//2)-vec(math.cos(self.angle*(i*self.scale)%self.points_num),math.sin(self.angle*(i*self.scale)%self.points_num))*self.radius)

        # fps
        self.draw_text(str(int(self.clock.get_fps())), self.font, 40, WHITE, 50, 50, align="center")
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                



# create the game object
g = Game()
g.new()
g.run()
