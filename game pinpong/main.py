from pygame import *


wind_wid = 700
wind_hei = 500
window = display.set_mode((wind_wid, wind_hei))

black = (255,251,51)

game = True
finish = False
clock = time.Clock()
FPS = 60



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed, player_width, player_haight):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_haight))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < wind_wid - 89:
            self.rect.x += self.speed       
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < wind_wid - 89:
            self.rect.x += self.speed 


raket1 = Player('20240208_183457.jpg', 30,200,4,20,150)
raket2 = Player('20240208_183457.jpg', 520,200,4,20,150)

ball = GameSprite('20240208_183338.jpg',200,200,4,50,50)

font.init()
font = font.Font(None, 25)
los1 = font.render(" Player 1 lose",True,(123,76,12))
los2 = font.render(" Player 2 lose",True,(123,76,12))

speed_x = 4
speed_y = 4

while game:
    for event in event.get():
        if event.type == QUIT:
            game = False
    if finish != True:
        window.fill(black)
        raket1.update()
        raket2.update_1()
        ball.rect.x += speed_x            
        ball.rect.y += speed_y 

        if sprite.collide_rect(raket1,ball) or  sprite.collide_rect(raket2,ball):
            speed_x *= -1
            speed_y *= 1
        
        if ball.rect.y > wind_hei-50 or ball.rect.y<0:
            speed_y*= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(los1,(200,200))
            game_over = True

        if ball.rect.x > wind_wid:
            finish = True
            window.blit(los2,(200,200))
            game_over = True

        raket1.reset()
        raket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)