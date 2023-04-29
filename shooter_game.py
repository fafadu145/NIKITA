from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Спидран по Никите")
background = transform.scale(image. load("galaxy.jpg"), (700, 500)) 
hero = transform.scale(image.load('rocket.png'), (100, 100)) 
cyborg = transform.scale(image.load('bullet.png'),((100, 100)))
treasure = transform.scale(image.load('asteroid.png'),(75, 75))

x1 = 100
y1 = 50

х2 = 200
у2 = 200

х3 = 500
уз = 200

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super ().__init__()
        self.image = transform.scale(image. load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Woll(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_haigth):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.haigth = wall_haigth
        self.image = Surface((self.width, self.haigth))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_woll(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
                  
class   Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 2:
            self.rect.x -= 5
        if keys_pressed[K_b] and self.rect.x < 620:
            self.rect.x += 5
    def fire(self):
        self.sprite_center = self.rect.center
        self.sprite_top = self.rect.sprite_top
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE]:
            Bullet.add(Bullet('bullet.png', self.rect.centerx, self.rect.top,15.20,-15))

class Enemy(GameSprite):
    def __init__(self, player_image, player_X, player_y, size_x, size_y, player_speed):
        super ().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)

        def update(self):
            global lost
            self.rect.y += self.speed
            if self.rect.y > 500:
                self.rect.y = 0
                self.rect.x = randint (30,640)
                lost +=1


game = True
while game:
    keys_pressed = key.get_pressed() 
    if keys_pressed[K_LEFT] and x1 >5:
        x1 -= 5
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += 5
    if keys_pressed [K_UP] and y1 > 5:
        y1 -= 5
    if keys_pressed [K_DOWN] and y1 < 395:
        y1 += 5 
    window.blit(background, (0, 0))
    window.blit(hero, (x1, y1)) 
    window.blit(cyborg, (х2, у2)) 
    window.blit(treasure, (х3, уз))
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock = time.Clock()
    FPS = 60
    display.update()


