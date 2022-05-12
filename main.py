import pygame, sys, math

pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.display.set_caption('Az Kvíz')

WIDTH, HEIGHT = screen.get_size()

clock = pygame.time.Clock()

hexes = []

questions_list = []

with open('config.txt') as config_file:
    config = config_file.readlines()

font_file = str(config[0].replace('\n', ''))

font = pygame.font.Font(font_file, 60)

class Hex():
    def __init__(self, position, status, radius, question, number):
        self.position = position
        self.status = status
        self.radius = radius
        self.question = question
        self.nuber = number
        self.selected = False
        self.rect = pygame.Rect((self.position), ((self.radius * 1.6), (self.radius * 1.6)))
        self.rect.center = self.position
        self.outline_color = (255,255,255)

    def draw_hexes(self, screen, width):
        radius = self.radius
        draw_hexagon(screen, (self.outline_color), (255,0,0),radius, self.position, width)

    def debug_rect(self, rect):
        pygame.draw.rect(screen, (0,255,0), self.rect, 4)

def draw_hexagon(surface, color, color_inner,radius, position, width):
    n = 6
    r = radius
    x, y = position
    pygame.draw.polygon(surface, color_inner, [(x + r * math.cos((2 * math.pi * i / n) + 11), y + r * math.sin((2 * math.pi * i / n) + 11)) for i in range(n)])   # draws the background of the hexagon
    pygame.draw.polygon(surface, color, [(x + r * math.cos((2 * math.pi * i / n) + 11), y + r * math.sin((2 * math.pi * i / n) + 11)) for i in range(n)], width)  # draws the outline of the hexagon



def print_question(screen, question, font):
    text = font.render(question, False, (100,100,100), (170,170,170))
    text_rect = text.get_rect()
    text_rect.center = ((WIDTH / 2), 1000)
    screen.blit(text, text_rect)


def init(questions):

    with open('questions.txt') as f:
        questions = f.readlines()

    #initialize the list of hexes and assign them a position, default status and setup for the main loop
    #MAIN THING ----- SET THE QUESTIONS AND ANSWERS

    index = 0

    for y in range(8):
        for x in range(y):
            hex = Hex(((((WIDTH/2)+(140 * x) + (70 * y))) - ((y * 140) - 70), 120 * y), 0, 70, str(questions[index]), index + 1)
            hexes.append(hex)
            index += 1


init(questions_list)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for hex in hexes:
                if hex.rect.collidepoint(mouse_pos):
                    hex.selected = True
                    print(hex.question)
                    print(hex.nuber)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                for hex in hexes:
                    if hex.selected == True:
                        hex.selected = False

    screen.fill((50,50,50))
    for hex in hexes:
        mouse_pos = pygame.mouse.get_pos()
        if hex.rect.collidepoint(mouse_pos):
            hex.outline_color = (100,100,100)
        else:
            hex.outline_color = (255,255,255)
        hex.draw_hexes(screen, 4)
        if hex.selected == True:
            print_question(screen, hex.question.replace('\n', ''), font)
   #     hex.debug_rect(hex.rect)
    pygame.display.flip()
    clock.tick(60)
