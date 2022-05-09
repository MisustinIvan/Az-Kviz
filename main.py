import pygame, sys, math

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

WIDTH, HEIGHT = screen.get_size()

print(WIDTH, HEIGHT)

clock = pygame.time.Clock()

hexes = []

class Hex():
    def __init__(self, position, status, radius, question, type, answers, right_answer, number):
        self.position = position
        self.status = status
        self.radius = radius
        self.question = question
        self.type = type
        self.answers = answers
        self.right_answer = right_answer
        self.nuber = number

def draw_hexagon(surface, color, radius, position, width):
    n = 6
    r = radius
    x, y = position
    pygame.draw.polygon(surface, color, [(x + r * math.cos((2 * math.pi * i / n) + 11), y + r * math.sin((2 * math.pi * i / n) + 11)) for i in range(n)], width)

def init():
    #initialize the list of hexes and assign them a position, default status and setup for the main loop
    #MAIN THING ----- SET THE QUESTIONS AND ANSWERS

    for index in range(28):
       hex = Hex((0,0), 0, 10, 10, 10, 10, 10, index + 1)
       hexes.append(hex)    # debug shit
    print(len(hexes))       # debug shit

init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))
    draw_hexagon(screen, (255,255,255), 40, (WIDTH/2,HEIGHT/2), 4)
    draw_hexagon(screen, (255,255,255), 40, ((WIDTH/2)+80,(HEIGHT/2)), 4)
    pygame.display.flip()
    clock.tick(60)
