import scipy.io
import pygame
import time
import math
import sys

(WIDTH, HEIGHT) = (900, 900)
BGCOLOR = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
R = 0.25
RSCREEN = 0.5*math.sqrt(WIDTH**2 + HEIGHT**2)
ZOOM = 1


def world_to_screen(x, y):
    return x * WIDTH / 9 * ZOOM + WIDTH / 2, - y * HEIGHT / 9 * ZOOM + HEIGHT / 2


def main():
    try:
        mat = scipy.io.loadmat('sim.mat')
    except FileNotFoundError:
        print("Error: file 'sim.mat' not found!", file=sys.stderr)
        exit(1)

    timedata = tuple(p[0] for p in mat['data'][0][0])
    statedata = mat['data'][0][1]

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Ball And Beam')
    pygame.display.flip()
    running = True
    start_time = time.time()
    current_index = 0

    COLOR_GRID = (100, 100, 100)

    while running:

        # handle pygame events

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # get state at this time instance

        animation_time = time.time() - start_time
        while timedata[current_index] < animation_time:
            current_index += 1
            if current_index >= len(timedata):
                current_index -= 1
                break
        state = statedata[current_index][0:2]
        x = state[0]
        theta = state[1]
        (ballx, bally) = (x*math.cos(theta)-R*math.sin(theta),
                          x*math.sin(theta)+R*math.cos(theta))
        (ballxs, ballys) = world_to_screen(ballx, bally)

        # draw frame

        screen.fill(BGCOLOR)

        # beam
        dely = math.sin(theta)*RSCREEN
        delx = math.cos(theta)*RSCREEN
        pygame.draw.line(screen, COLOR_BLACK,
                         (WIDTH*0.5-delx, HEIGHT*0.5+dely),
                         (WIDTH*0.5+delx, HEIGHT*0.5-dely),
                         width=2)
        pygame.draw.circle(screen, COLOR_BLACK, (ballxs, ballys), R*100*ZOOM)

        pygame.display.update()


if __name__ == '__main__':
    main()
