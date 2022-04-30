from pygame import *
from sys import *
from random import randint

player = "Assets/car1.png"
limit60 = "Assets/60 limit speed.png"
bus1 = "Assets/bus1.png"
car1 = "car1.png"
battery_light = "Assets/Car_Battery_Indicator_Light.png"
check_engine = "Assets/check engine.png"
police_kar = "Assets/police car1.png"
road = "road.png"
transmission = "transmission.png"

win_width = 400
win_height = 800

class GameSprite(sprite.Sprite):
    def __init__(self):
        pass
class player():
    def __init__():
        pass
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= win_height:
            self.rect.x = randint(80, -80)
            self.rect.y = 0

display.set_caption("Race")
window = display.set_mode((win_width, win_height))
backgroung = transform.scale(image.load(road),(win_width,win_height))
carI = transform.scale(image.load(car1),(100,180))
transmission = transform.scale(image.load(transmission), (40,100))

x1=258
y1=550
speed = 10
run = 1
finish = 0
carsGroup = sprite.Group()
for i in range(1,6):
    car = Enemy(car1, randint(80,-80), -40, 80, 50, randint(1,5))
    carsGroup.add(car)
while run:
    window.blit(backgroung,(0,0))
    window.blit(carI,(x1,y1))
    window.blit(transmission,(340,650))
    for e in event.get():
        if e.type == QUIT:
            run = 0
    display.update()

    key_pressed = key.get_pressed()

    if key_pressed[K_LEFT] and x1 > 17:
        x1 = x1 - speed

    if key_pressed[K_RIGHT] and x1 < 280:
        x1 = x1 + speed
    if key_pressed[K_UP] and y1 > 10:
        y1 = y1 - speed

    if key_presses[K_1]:
        pass
    
         










        



    
    



