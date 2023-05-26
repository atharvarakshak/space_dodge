#    Space dodging game

import pygame  # libraby to implement basic functionalities in a python game
import time
import random
pygame.font.init()  # requirement for py program game text

WIDTH,HEIGTH = 1000,600
WIN = pygame.display.set_mode((WIDTH,HEIGTH)) #passing tuple through your set_mode
pygame.display.set_caption("SpaceDodge")   # setiing caption for your window


BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH,HEIGTH))
 # to display image in python(pygame.image.load(".jpeg"))
# scaling image to width and height of the screen
#SHIP =pygame.image.load("ship.png","10 40")
#SHIP_rect= SHIP.get_rect(centre=(0,0))

PlAYER_HEIGHT=60
PLAYER_WIDTH=40
PLAYER_VEL=5
STAR_WIDTH=10
STAR_HEIGHT=20
STAR_VEL=3
FONT = pygame.font.SysFont("TimesNewRoman",30)  # ("font",size)

def draw(player,elapsed_time,stars):
    WIN.blit(BG ,(0,0))  # (0,0) initialises the start and end
    time_text = FONT.render(f"Time:{round(elapsed_time)}s",3,"yellow")
    WIN.blit(time_text,(10,10))
    pygame.draw.rect(WIN , "orange" , player)
    
    #pygame.image.load("ship.png")
    
    
    for star in stars:
        pygame.draw.rect(WIN,"white", star)
    pygame.display.update()


def main():
    run = True
    player = pygame.Rect(500,HEIGTH - PlAYER_HEIGHT,PLAYER_WIDTH,PlAYER_HEIGHT)
    clock = pygame.time.Clock()

    start_time = time.time()  # initializing the start time for player
    elapsed_time = 0
    star_add_increment = 2000
    star_count = 0
    stars =[]
    hit = False


    while run:   # loop to keep the window running
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time # elapsed time after activity
        if star_count >= star_add_increment:
            for _ in range(3):
                star_x = random.randint(0,WIDTH - STAR_WIDTH) # pic a random integer in range
                star = pygame.Rect(star_x,-STAR_HEIGHT,STAR_WIDTH,STAR_HEIGHT) # star to start  at screen and y: little above the top of the screen 
                stars.append(star)
            
            star_add_increment = max(200,star_add_increment - 50)
            star_count=0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed() # event listner for key press
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >=0:  # k_game is key code to move left in pygame lib documentation
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:  # creating a copy of stars to delete stars that
                               # touch the top of player and bottom of screen so that we would mutate original list
            star.y += STAR_VEL
            if star.y > HEIGTH:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player): # colliderect tells if two rect will collide
                stars.remove(star)
                hit = True
                break
        
        if hit:
            lost_text = FONT.render(f"You Lost . Your score{round(elapsed_time)}points",1,"White")
            WIN.blit(lost_text,(WIDTH/2 - lost_text.get_width()/2 ,HEIGTH/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player,elapsed_time,stars)  # for every single frame draw function is called    
    
    pygame.quit()

if __name__ == "__main__":
    main()



