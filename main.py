import pygame, sys, math

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

WIDTH, HEIGHT = screen.get_size()

clock = pygame.time.Clock()

hexes = []

questions_list = []

class Hex():
    def __init__(self, position, status, radius, question, number):
        self.position = position
        self.status = status
        self.radius = radius
        self.question = question
        self.nuber = number

    def draw_hexes(self, screen, width):
        radius = self.radius
        draw_hexagon(screen, (255,255,255), radius, self.position, width)

def draw_hexagon(surface, color, radius, position, width):
    n = 6
    r = radius
    x, y = position
    pygame.draw.polygon(surface, color, [(x + r * math.cos((2 * math.pi * i / n) + 11), y + r * math.sin((2 * math.pi * i / n) + 11)) for i in range(n)], width)


def init(questions):

    with open('questions.txt') as f:
        questions = f.readlines()

    #initialize the list of hexes and assign them a position, default status and setup for the main loop
    #MAIN THING ----- SET THE QUESTIONS AND ANSWERS

    index = 0

    for y in range(7):
        for x in range(y):
            hex = Hex((((WIDTH/2)-(140 * x) + (70 * y)) - 70, 120 * y), 0, 70, str(questions[index]), index)
            hexes.append(hex)
            index += 1


init(questions_list)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))
    for hex in hexes:
        hex.draw_hexes(screen, 4)
    pygame.display.flip()
    clock.tick(60)
