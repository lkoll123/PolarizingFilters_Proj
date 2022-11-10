# Import and initialize pygame library
import pygame
pygame.init()

# Set up drawing window
screen = pygame.display.set_mode([120,120])
pygame.display.set_caption('FilterSim')
clock = pygame.time.Clock()

#create test arrs that indicate the color the pixels start at and what color they should turn to
#Representative of circle filter colors
pixInput = [[100 for i in range(10)] for j in range(10)]

pixAlter = [[100 for i in range(10)] for j in range(10)]

pixOutput = [[0,0,0,0,0,0,0,0,0,0],
            [0,200,0,0,200,0,200,200,200,10],
            [0,200,0,0,200,0,0,200,10,40],
            [0,200,200,200,200,0,0,200,40,70],
            [0,200,0,0,200,0,10,200,70,100],
            [0,200,0,0,200,10,200,200,200,130],
            [0,0,0,0,10,40,70,100,130,160],
            [0,0,0,10,40,70,100,130,160,190],
            [0,0,10,40,70,100,130,160,190,220],
            [0,10,40,70,100,130,160,190,220,250]]


def game_loop():
    exit = False
    time = 0
    stop = True
    while not exit:
        clock.tick(60)
        if not stop and time <= 100000:
            time += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())
            elif event.type == pygame.KEYUP:
                if pygame.key.key_code("space") == pygame.K_SPACE:
                    stop = not stop
                    print("time:", time)
        screen.fill((0,0,0))

######### draw stuff ##########
        #setup variables to be used later
        if time == 0:
            i = 0
            j = 0
            totalDif = 0

        if i < 10:
            #find the total amount the color needs to change for first circle(index)
            startDif = pixOutput[i][j] - pixInput[i][j]
            #find how much further the color needs to change
            runDif = pixOutput[i][j] - pixAlter[i][j]

            #if the color still needs to change, either add or subtract until it is equal to the wanted color
            if runDif > 0:
                pixAlter[i][j]=pixInput[i][j] + time-totalDif
            elif runDif < 0:
                pixAlter[i][j]=pixInput[i][j] - (time-totalDif)

            #if the color is right, move to the next circle (index in the array)
            elif j < 10:
                if startDif > 0:
                    totalDif+=startDif
                elif startDif < 0:
                    totalDif-=startDif
                j+=1

            #if all colors have been changed in row, move to the next row
            if j == 10:
                j=0
                i+=1

        #draw the circles on the screen
        for x in range(10):
            for y in range(10):
                color = pixAlter[y][x]
                pygame.draw.circle(screen,(color,color,color),(5+x*10,5+y*10),5)


        pygame.display.update()

game_loop()
pygame.quit()
quit()
