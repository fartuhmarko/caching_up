from pygame import*


class GameSprite():
    def __init__(self, img, speed, x, y):
        self.img = transform.scale(image.load(img), (65,65))
        self.rect = self.img.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
        self.direction = "right"
        self.move_left = False

    def reset(self):
        window.blit(self.img, (self.rect.x, self.rect.y))

class Hero(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys [K_d]:
            if self.rect.x < 640:
                self.rect.x +=self.speed
        if keys [K_a]:
            if self.rect.x > 5:
                self.rect.x -= self.speed
                
        if keys [K_w]:
            if self.rect.y > 5:
                self.rect.y -= self.speed
        if keys [K_s]:
            if self.rect.y < 440:
                self.rect.y += self.speed
            
class Enemy(GameSprite):
    def move(self, start, end):
        if self.direction == "right":
            self.rect.x += 5
        if self.direction == "left":
            self.rect.x -= 5
        if self.rect.x >= end:
            self.direction = "left"
        if self.rect.x <= start:
            self.direction = "left"
        
    

window = display.set_mode((700,500))
display.set_caption("Доганялки")
background = transform.scale(image.load("background.png"))
x1 = 100
y1 = 100
window.blit(background,(0, 0))
mixer.music.load("jungles.ogg")

sprite1 = transform.scale(
    image.load(""),(100,100))
window.blit(sprite1, (x1, y1))

x2 = 100
y2 = 100

sprite2 = transform.scale(
    image.load(""),(100,100))
window.blit(sprite1, (x2, y2))
clock = time.Clock

enemy = Enemy("cyborg.png", 10, 50, 50)
hero = GameSprite("hero.png", 10, 50, 50)
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

kick = mixer.Sound("kick.ogg")

game = True

while game:
    window.blit(background,(0, 0))
    
    hero.reset()
    hero.move()
    enemy.reset()
    enemy.move(300, 600)
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    keys_pressed = key.get_pressed()
        

    display.update()

    clock.tick(60)





