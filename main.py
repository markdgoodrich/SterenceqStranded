import pygame
import os
import time

from PIL import Image #Needed to get dimensions of map assets

pygame.init()

resolution_X = 800
resolution_Y = 600

screen = pygame.display.set_mode((resolution_X,resolution_Y))

pygame.display.set_caption("Sterenceq Stranded!")


# Create player and initial position
player = pygame.image.load("player1.png")
playerX = 400
playerY = 350
# Movement for player
deltaX = 0
deltaY = 0

def draw_player(x,y, eyex, eyey):
    screen.blit(player, (x,y)) #Draw player at specific inputs

    #draws eyes
    #pygame.draw.circle(screen, (0,0,0), (x+40, y+55), 3)
    #pygame.draw.circle(screen, (0,0,0), (x+55, y+55), 3)

    if eyey == 0 and eyex == 0:
        pygame.draw.circle(screen, (0,0,0), (x+40, y+55), 3)
        pygame.draw.circle(screen, (0,0,0), (x+55, y+55), 3)

    elif eyex < 0:
        pygame.draw.circle(screen, (0,0,0), (x+37, y+55), 3)
        pygame.draw.circle(screen, (0,0,0), (x+52, y+55), 3)

    elif eyex > 0:
        pygame.draw.circle(screen, (0,0,0), (x+43, y+55), 3)
        pygame.draw.circle(screen, (0,0,0), (x+58, y+55), 3)

    elif eyey < 0:
        pygame.draw.circle(screen, (0,0,0), (x+40, y+52), 3)
        pygame.draw.circle(screen, (0,0,0), (x+55, y+52), 3)
    elif eyey > 0:
        pygame.draw.circle(screen, (0,0,0), (x+40, y+58), 3)
        pygame.draw.circle(screen, (0,0,0), (x+55, y+58), 3)


message = "This is a large string to test the wrap-around capabilities of the function"
font = pygame.font.Font('./fonts/neo_scifi.ttf', 32)
messageX = 30
messageY = 30
is_message = True

def display_message(message, font, messageX, messageY):
    message_display = font.render(message, True, (255, 255, 255))
    screen.blit(message_display, (messageX, messageY))


#Displays letters in a message one at a time
def message_appearing_letters(message, font, x, y):
    for i in message:
        screen.blit(font.render(i, True, (255, 255, 255)), (x, y))
        x += 20
        pygame.display.update()
        time.sleep(0.05)

        #when the edge of the screen is met, move it down and back over
        if x >= resolution_X - 30:
            y += 30
            x = 30

    is_message = False #to only display it once
    #time.sleep(len(message))

'''
def level_one():        #probably uneccessary
    #load level assests
    ship1 = pygame.image.load("./level_assets/lvl1/ship1.png")
    trashcan = pygame.image.load("./level_assets/lvl1/trashcan.png")

    #draw background
    screen.blit(pygame.image.load("./backgrounds/lvl1/1.png"), [0, 0])

    screen.blit(ship1, (200, 200))
    screen.blit(trashcan, (500, 300))

    intro = "Priority 1: Put out that fire!"
    message_appearing_letters(intro, font, 10, 20)
'''

current_level = 1
current_background = 1
# Draws the backgrounds
def draw_background(level, image_num):
    background_file = "backgrounds/lvl"+str(level)+"/"+str(image_num) + ".png"
     #   Check to see if it exists
    if os.path.isfile(background_file):
         screen.blit(pygame.image.load(background_file), [0, 0])

    #how to draw elements for specific image_num on levels?

def draw_level_assets(level, sub_level):
    map_assets = "./level_assets/lvl"+str(level)+"/map"+str(sub_level)+"/"
    for image in os.listdir(map_assets):
        image_asset = pygame.image.load(str(map_assets) + str(image))

        #Generates interactable rectangle
        image_size = Image.open(str(map_assets) + str(image)).size #returns (x, y) size of image
        size_x, size_y = str(image_size).split(",")
        size_x = size_x.replace('(','')
        size_y = size_y.replace(')','')
        image_rect = image_asset.get_rect(x=int(size_x), y=int(size_y))

        #Draws the asset in the area specified in the level dictionary
        screen.blit(image_asset, level_1[image])

#   Click and Drag
# https://github.com/furas/python-examples/blob/master/pygame/drag-many-images/example-1-drag-two_images.py

#dictionary for lvl 1
#asset: location (x-y)
#PNGs MUST be present in the level_asset directory AND in the dictionary.
#Maybe keep dictionary file in the level_asset?
level_1 = {
'ship1.png':(64,64),
'trashcan.png':(500,300),
'cactus_pointy.png': (450,450),
'cactus.png': (450,450)
    }

drag = 0


# --------------------------------------------------------------------------------------------
#
#                               The Primary Gameplay Loop
#
# --------------------------------------------------------------------------------------------
game_running = True
while game_running:
    for event in pygame.event.get():  # Captures all of the events in pygame.
        if event.type == pygame.QUIT:  # If the event type is 'qutting the game', AKA the 'close' button
            running = False  # Only stops when close button is pressed

    #if event.type ==pygame.MOUSEBUTTONDOWN:     #If mouse button is clicked


    draw_background(current_level, current_background)
    draw_level_assets(current_level, current_background)

    #message_appearing_letters(message, font, messageX, messageY)

    # Click and Drag
    if event.type == pygame.MOUSEBUTTONDOWN:
        drag = 1
    elif event.type == pygame.MOUSEBUTTONUP:
        drag = 0
    elif event.type == pygame.MOUSEMOTION:
        if drag:
            ship1_rect.move_ip(event.rel)   #BROKEN with dynamic asset loading.

    #if trashcan_rect.colliderect(ship1_rect) and drag == 0: #Once it is in the location and mouse button up
    #    display_message("Ship destroyed.  Good luck now.", font, 150, 200)




    #   -------------------------
    #       Player Movement
    #   -------------------------
    if event.type == pygame.KEYDOWN:  # KEYDOWN = when tehkey is pressed
        if event.key == pygame.K_LEFT:  # K_LEFT = left arrow key
            deltaX = -6  # Increment player left by 5 values

        if event.key == pygame.K_RIGHT:  # K_RIGHT = right arrow key
            deltaX = 6  # Increment player left by 5 values

        if event.key == pygame.K_UP:  # K_LEFT = left arrow key
            deltaY = -6  # Increment player left by 5 values

        if event.key == pygame.K_DOWN:  # K_RIGHT = right arrow key
            deltaY = 6  # Increment player left by 5  values

    # If keys are released
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            deltaX = 0  # When key is not pressed, we stop movement
            deltaY = 0  # Stop movement when key si released

    # Update player's position
    playerY += deltaY
    playerX += deltaX

    #   Player Movement - Out Of Frame
    # A little tricky, since we want to stop the player when they are out of background space
    # background files must be named accordingly
    if playerX <= 0 :
        if current_background == 0: #if there are no more files present
            playerX = 0             #stays at edge of location
        else:
            current_background -= 1     #goes to next background
            playerX = 600
    elif playerX > 700:
        if current_background >= len(os.listdir('./backgrounds/lvl'+ str(current_level)))-1:    #if there are no more background filea
            playerX = 700
        else:
            current_background += 1     #goes to next background
            playerX = 0
    #Currently, player cannot move to different y screens
    if playerY >= 500:
        playerY = 500
    elif playerY <= 0:
        playerY = 0

    draw_player(playerX, playerY, deltaX, deltaY)

    pygame.display.update()
