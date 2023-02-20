import scipy.io
import pygame
import time
import math
import sys
    
(width, height) = (900, 900)

def world_to_screen(x, y):
    return x*width/6 + width/2, - y*height/6 + height/2

def main():
    try:
        mat = scipy.io.loadmat('sim.mat')
    except FileNotFoundError:
        print("Error: file 'sim.mat' not found!", file=sys.stderr)
        exit(1)
    
    timedata = tuple(p[0] for p in mat['data'][0][0])
    statedata = mat['data'][0][1]
    
    background_colour = (255,255,255)
    L = 1
    
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Double pendulum')
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
        state = statedata[current_index]
    
        x = state[0]
        theta1 = state[1]
        theta2 = state[2]
        fx = x
        x = 0
        p1 = (x + L*math.sin(theta1), -L*math.cos(theta1))
        p2 = (p1[0] + L*math.sin(theta2), p1[1] + -L*math.cos(theta2))
        p1s = world_to_screen(*p1)
        p2s = world_to_screen(*p2)
        p0s = world_to_screen(x, 0)
    
        # draw frame
    
        center_x, center_y = world_to_screen(0, 0)
    
        screen.fill(background_colour)
    
        xv = fx%1
        for offset in range(-3,3+1):
            lines, _ = world_to_screen(-xv + offset, 0)
            pygame.draw.line(screen, COLOR_GRID, (lines,0), (lines, height))
        for y in range(0, height, height//6):
            pygame.draw.line(screen, COLOR_GRID, (0,y), (width, y), width = 1 if y != height/2 else 3)
    
    
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(-50+p0s[0], center_y-100, 100, 100))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(-50+p0s[0], center_y-100, 100, 100), width = 2)
        pygame.draw.circle(screen, (0, 0, 0), p1s, 20)
        pygame.draw.circle(screen, (0, 0, 0), p2s, 20)
        pygame.draw.line(screen, (0, 0, 0), p0s, p1s)
        pygame.draw.line(screen, (0, 0, 0), p1s, p2s)
    
        pygame.display.update()

if __name__ == '__main__':
    main()
