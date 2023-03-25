import pygame
pygame.init()
from pygame import mixer

win = pygame.display.set_mode((1248, 702))
icon = pygame.image.load('ico.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("bong")

wid = 10
hei = 100
xa = 50
ya = 300
xb = 1198
yb = 300
posx = 625
posy = 351
vel = 5
bounce = 0
angle = 2
loop = 0
check = 0
speed = 10
set = 0
sca = 0
laccl = 0
scb = 0

font = pygame.font.SysFont('Arial.ttf', 45)

run = True
while run:
    pygame.time.delay(speed)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    text = font.render('Score: ' + str(sca), 1, (200, 200, 200))
    win.blit(text,(220, 10))
    text = font.render('Score: ' + str(scb), 1, (200, 200, 200))
    win.blit(text,(890, 10))
    pygame.draw.rect(win, (150, 150, 150), (xa, ya, wid, hei,))
    pygame.draw.rect(win, (80, 80, 80), (624, 0, 5, 702,))
    pygame.draw.circle(win, (200, 200, 200), (posx, posy), 5)
    pygame.draw.rect(win, (150, 150, 150), (xb, yb, wid, hei,))
    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and yb > 0:
     yb = yb - vel - 3

    if keys[pygame.K_HOME]:
     posx = 625
     posy = 351 

    if keys[pygame.K_DOWN] and yb < 702 - hei:
     yb = yb + vel + 3
     laccl = -1.2

    if keys[pygame.K_w] and ya > 0:
     ya = ya - vel - 3
     laccl = 1.2

    if keys[pygame.K_s] and ya < 702 - hei:
     ya = ya + vel + 3

    print(angle)

    if posx >= 55 and bounce == 0:
      posx = posx - vel
      posy = posy - angle
      
      if posx == 55 and posy >= ya and posy <= ya + 100:
        check = check + 1
        bounce = 1
        mixer.music.load('beep.mp3')
        mixer.music.play()
        if angle >= 0:
         angle = angle * -1 * laccl
        else:
         angle = angle * -1 * laccl
      if posx < 55:
       scb = scb + 1
        
        


    if posx <= 1200 and bounce == 1:
      posx = posx + vel
      posy = posy + angle
      if posx == 1200 and posy >= yb and posy <= yb + 100:
        check = check + 1
        bounce = 0 
        mixer.music.play()
        if angle >= 0:
         angle = angle * -1
        else:
         angle = angle * -1
      if posx > 1200:
       sca = sca + 1   

    if posy <= 1:
      angle = angle * -1

    if angle == 0:
      loop = loop + 1
      if loop == 3:
        angle = 2
        loop = 0

    if posy >= 694:
      angle = angle * -1   

    if check == 10 and set == 0:
      angle = angle + 1
      speed = speed - 1 
      set = 1 
    if check == 20 and set == 1:
      angle = angle + 1
      speed = speed - 2 
      set = 2

      laccl = 0

    if angle > 6:
      angle = 2
    if angle < -6:
      angle -2     


      
 


    