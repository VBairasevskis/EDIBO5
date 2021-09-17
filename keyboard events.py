# Connecting the PyGame library
import pygame

# Initializing PyGame
pygame.init()
# Game window: size, position
W = 400
H = 300

screen = pygame.display.set_mode((W, H))
# Give window title
pygame.display.set_caption("Valerijs")

WHITE = (255, 255, 255)  # Screen color
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60
fpsClock = pygame.time.Clock()  # frame rate in the main loop of the Game

x = W // 2
y = H // 2
speed = 5

# flLeft = flRight = flUp = flDown = False
# Game loop
done = False  # Flag to exit the game loop
while not done:
    fpsClock.tick(FPS)  # frame rate
    # Tracking event: "close window"
    for event in pygame.event.get():  # Referring to the event queue
        if event.type == pygame.QUIT:  # Checking the event pygame.QUIT
            done = True
        # elif event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_LEFT:
        #        flLeft = True
        #    if event.key == pygame.K_RIGHT:
        #        flRight = True
        #    if event.key == pygame.K_UP:
        #        flUp = True
        #    elif event.key == pygame.K_DOWN:
        #        flDown = True
        # elif event.type == pygame.KEYUP:
        #    if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
        #        flLeft = ftRight = flUp = flDown = False

    # if flLeft:
    #    x -= speed
    # elif flRight:
        #x += speed
    #if flUp:
        #y -= speed
    #elif flDown:
        #y += speed
    # drawing

    # essy write code we change pygame.key to pygame.key.get_pressed()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill(WHITE)  # background color white
    pygame.draw.rect(screen, BLUE, (x, y, 10, 20))  # drawing a rectangular (screen, COLOR, (x, y, wight, height))
    pygame.display.update()  # flip == update, but update more flexible
