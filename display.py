import pygame
from constants import TEXT_COLOR, GAME_OVER_COLOR, BACKGROUND_COLOR

# Fonts will be initialized after pygame is initialized in main.py
def init_fonts():
    global font_style, score_font
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display score
def your_score(dis, score):
    value = score_font.render("Your Score: " + str(score), True, TEXT_COLOR)
    dis.blit(value, [0, 0])

# Function to display a message
def message(dis, msg):
    mesg = font_style.render(msg, True, GAME_OVER_COLOR)
    dis.blit(mesg, [dis.get_width() / 6, dis.get_height() / 3]) 
    # To draw the msg surface onto the dis surface
    # Coordinates for the position on the screen where the top-left corner of the message will be placed.

# Function to fill the background color
def fill_background(dis):
    dis.fill(BACKGROUND_COLOR)
