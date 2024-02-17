from pygame import*


class GameSprite():
    def __init__(self, img, speed, x, y):
        self.img = transform.scale(image.load(img), (65,65))
        self.rect = self.img.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y

        self.move_left = False

    def reset(self):
        
        if self.move_left == True:
            self.rect.x += self.speed

        window.blit(self.img, (self.rect.x, self.rect.y))

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

hero = GameSprite("hero.png", 10, 50, 50)
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

kick = mixer.Sound("kick.ogg")

game = True

while game:
    window.blit(background,(0, 0))
    
    hero.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_1:
                kick.play()
            if e.key == K_d:
                hero.move_left = False
            
    keys_pressed = key.get_pressed()
        

    display.update()

    clock.tick(60)





