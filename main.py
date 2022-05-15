import pygame, sys, math, random

#player1_name = input('Player 1 name > ')
#player2_name = input('Player 2 name > ')

pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.display.set_caption('Az Kvíz')

WIDTH, HEIGHT = screen.get_size()

clock = pygame.time.Clock()

hexes = []

questions_list = []

letters_list = []

yn_questions_list = []

with open('config.txt') as config_file:
    config = config_file.readlines()

font_file = str(config[0].replace('\n', ''))

font = pygame.font.Font(font_file, 90)

font_big = pygame.font.Font(font_file, 100)


yn_selected = False

random_question = ''

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
        self.outline_color = (150,150,150)
        self.bg_color = (220,220,220)


    def draw_hexes(self, screen, width):
        radius = self.radius
        draw_hexagon(screen, self.outline_color, self.bg_color,radius, self.position, width)

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


def init(questions, letters, yn_questions):

    with open('questions.txt') as f:
        for i in f.readlines():
            questions.append(i)

    with open('letters.txt') as f:
        for i in f.readlines():
            letters.append(i)

    with open('yn_questions.txt') as f:
        for i in f.readlines():
            yn_questions.append(i)
    #initialize the list of hexes and assign them a position, default status and setup for the main loop
    #MAIN THING ----- SET THE QUESTIONS AND ANSWERS

    index = 0

    for y in range(8):
        for x in range(y):
            hex = Hex(((((WIDTH/2)+(140 * x) + (70 * y))) - ((y * 140) - 70), 120 * y), 0, 70, str(questions[index]), index + 1)
            hexes.append(hex)
            index += 1


def draw_letters(screen, hexes, font, letters):
    for hex in hexes:
        text = font.render(str(letters[hex.nuber - 1].replace("\n", "")), False, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = hex.rect.center
        screen.blit(text, text_rect)


def show_yn(screen, question, font):
   text = font.render(question.replace('\n', ''), False, (255,255,255))
   text_rect = text.get_rect()
   text_rect.center = (WIDTH/2,HEIGHT/2)
   screen.blit(text, text_rect)

init(questions_list, letters_list, yn_questions_list)

#print(len(hexes))
#print(len(questions_list))                 DEBUG
#print(letters_list)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for hex in hexes:
                hex.selected = False
                if hex.rect.collidepoint(mouse_pos):

                    hex.selected = True
                   # print(hex.question)
                   # print(hex.nuber)           DEBUG


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                for hex in hexes:
                    if hex.selected:
                        hex.bg_color = (0,0,0)

            if event.key == pygame.K_e:
                for hex in hexes:
                    if hex.selected:
                        hex.bg_color = (87,195,219)

            if event.key == pygame.K_r:
                for hex in hexes:
                    if hex.selected:
                        hex.bg_color = (250,156,4)

            if event.key == pygame.K_q:
                if len(yn_questions_list) >= 1:
                    yn_selected = True
                    random_question = random.choice(yn_questions_list)

            if event.key == pygame.K_a:
                yn_selected = False
                if len(yn_questions_list) >= 1:
                    yn_questions_list.remove(random_question)


    screen.fill((220,220,220))
    if yn_selected == False:
        for hex in hexes:
            mouse_pos = pygame.mouse.get_pos()
            if hex.selected == True and hex.rect.collidepoint(mouse_pos) == True:
                hex.outline_color = (100,100,100)
            elif hex.rect.collidepoint(mouse_pos) and hex.selected != True:
                hex.outline_color = (125,125,125)
            elif hex.selected == True and hex.rect.collidepoint(mouse_pos) == False:
                hex.outline_color = (100,100,100)
            else:
                hex.outline_color = (150,150,150)
            hex.draw_hexes(screen, 4)

            if hex.selected == True:
                print_question(screen, hex.question.replace('\n', ''), font)
        draw_letters(screen, hexes, font_big, letters_list)
    else:
        if len(yn_questions_list) >= 1:
            show_yn(screen, random_question, font)
   #     hex.debug_rect(hex.rect)
    pygame.display.flip()
    clock.tick(360)



# git commit test
