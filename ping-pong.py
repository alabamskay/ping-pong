from pygame import*

window = display.set_mode((600,500))
window.fill((250, 187, 220))

clock=time.Clock()

finish = False
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 340:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 340:
            self.rect.y += self.speed

speed_x = 3
speed_y = 3

pl1 = Player('platforma.png',550,100,4,(25,150))
pl2 = Player('platforma.png',5,100,4,(25,150))
ball = GameSprite('shar.png',100,100,30,(30,30))

font.init()
font1 = font.Font(None,35)
lose1 = font1.render('Игрок 1 проиграл',True,(139,0,0))
font2 = font.Font(None,35)
lose2 = font2.render('Игрок 2 проиграл',True,(139,0,0))



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill((250, 187, 220))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        pl1.reset()
        pl1.update_l()
        pl2.reset()
        pl2.update_r()
        ball.reset()
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(pl1,ball) or sprite.collide_rect(pl2,ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1,(200,200))
    if ball.rect.x > 550:
        finish = True
        window.blit(lose2,(200,200))
    
        

    display.update()
    clock.tick(60)
