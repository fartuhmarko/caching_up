from pygame import*

window = display.set_mode((700,500))
display.set_caption("Доганялки")
background = transform.scale(image.load("background.png"),(700,500))
x1 = 100
y1 = 100
window.blit(background,(0, 0))
game = True
sprite1 = transform.scale(
    image.load("sprite1.png"),(100,100))
window.blit(sprite1, (x1, y1))

x2 = 100
y2 = 100

sprite2 = transform.scale(
    image.load("sprite1.png"),(100,100))
window.blit(sprite1, (x2, y2))
clock = time.Clock
while game:
    window.blit(background,(0, 0))
    window.blit(sprite1, (100, 100))
    window.blit(sprite2, (100, 100))

    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP]:
        

    display.update()
    clock.tick(60)





