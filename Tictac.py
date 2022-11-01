import pygame

pygame.init()

win=pygame.display.set_mode((550, 550))

pygame.display.set_caption('Tic Tac uyini')

first = pygame.draw.rect(win,(255,255,255),(25,25,150,150))
second = pygame.draw.rect(win,(255,255,255),(200,25,150,150))
third=pygame.draw.rect(win,(255,255,255),(375,25,150,150))

fourth = pygame.draw.rect(win,(255,255,255),(25,200,150,150))
fifth = pygame.draw.rect(win,(255,255,255),(200,200,150,150))
sixth=pygame.draw.rect(win,(255,255,255),(375,200,150,150))

seventh = pygame.draw.rect(win,(255,255,255),(25,375,150,150))
eighth = pygame.draw.rect(win,(255,255,255),(200,375,150,150))
ninth = pygame.draw.rect(win,(255,255,255),(375,375,150,150))

run=True
draw_obj='rect'
fi=True
se=True
th=True
fo=True
fif=True
si=True
sev=True
eg=True
ni=True


while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                fi=True
                se=True
                th=True
                fo=True
                fif=True
                si=True
                sev=True
                eg=True
                ni=True
                first = pygame.draw.rect(win,(255,255,255),(25,25,150,150))
                second = pygame.draw.rect(win,(255,255,255),(200,25,150,150))
                third=pygame.draw.rect(win,(255,255,255),(375,25,150,150))

                fourth = pygame.draw.rect(win,(255,255,255),(25,200,150,150))
                fifth = pygame.draw.rect(win,(255,255,255),(200,200,150,150))
                sixth=pygame.draw.rect(win,(255,255,255),(375,200,150,150))

                seventh = pygame.draw.rect(win,(255,255,255),(25,375,150,150))
                eighth = pygame.draw.rect(win,(255,255,255),(200,375,150,150))
                ninth = pygame.draw.rect(win,(255,255,255),(375,375,150,150))

        if event.type==pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()

            if first.collidepoint(pos) and fi:
                if draw_obj=='rect':
                    pygame.draw.rect(win,(255,0,0),(50,50,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win,(0,255,0),(100,100), 50)
                    draw_obj='rect'
                fi=False
            if second.collidepoint(pos) and se:
                if draw_obj=='rect':
                    pygame.draw.rect(win,(255,0,0),(225,50,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win,(0,255,0),(275,100), 50)
                    draw_obj='rect'
                se=False
            if third.collidepoint(pos) and th:
                if draw_obj=='rect':
                    pygame.draw.rect(win,(255,0,0),(400,50,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win,(0,255,0),(450,100), 50)
                    draw_obj='rect'
                th=False

            if fourth.collidepoint(pos) and fo:
                if draw_obj=='rect':
                    pygame.draw.rect(win,(255,0,0),(50,225,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win,(0,255,0),(100,275), 50)
                    draw_obj='rect'
                fo=False
            if fifth.collidepoint(pos) and fif:
                if draw_obj=='rect':
                    pygame.draw.rect(win,(255,0,0),(225,225,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win,(0,255,0),(275,275), 50)
                    draw_obj='rect'
                fif=False
            if sixth.collidepoint(pos) and si:
                if draw_obj=='rect':
                    pygame.draw.rect(win,(255,0,0),(400,225,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win,(0,255,0),(450,275), 50)
                    draw_obj='rect'
                si=False
            
            
            if seventh.collidepoint(pos) and sev:
                if draw_obj=='rect':
                    pygame.draw.rect(win,(255,0,0),(50,400,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win,(0,255,0),(100,450), 50)
                    draw_obj='rect'
                sev=False
            if eighth.collidepoint(pos) and eg:
                if draw_obj=='rect':
                    pygame.draw.rect(win,(255,0,0),(225,400,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win,(0,255,0),(275,450), 50)
                    draw_obj='rect'
                eg=False
            if ninth.collidepoint(pos) and ni:
                if draw_obj=='rect':
                    pygame.draw.rect(win,(255,0,0),(400,400,100,100))
                    draw_obj = 'circle'
                else:
                    pygame.draw.circle(win,(0,255,0),(450,450), 50)
                    draw_obj='rect'
                ni=False

    pygame.display.update()
pygame.quit()