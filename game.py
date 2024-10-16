import pygame
import random
from constants import SNAKE_BLOCK, SNAKE_SPEED, SNAKE_COLOR, FOOD_COLOR
from display import your_score, message, fill_background, init_fonts

# Function to run the game loop
def gameLoop():
    init_fonts()  # Initialize fonts after pygame is initialized
    dis_width = 800
    dis_height = 600
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game')

    #clock = pygame.time.Clock()

    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    length_of_snake = 1

    # Spawn the food - random position for food
    foodx = round(random.randrange(0, dis_width - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - SNAKE_BLOCK) / 10.0) * 10.0

    game_over = False
    game_close = False

    while not game_over:
        while game_close:   # When you lose the game
            fill_background(dis)
            message(dis, "You Lost! Press Q-Quit or C-Play Again")
            your_score(dis, length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: # quit game 
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c: # restart game
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:  # Snake Movements - arrow games
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True  #Gameover - boundaries
        x1 += x1_change
        y1 += y1_change

        fill_background(dis)
        # Food draw on random position
        pygame.draw.circle(dis, FOOD_COLOR, (int(foodx + SNAKE_BLOCK / 2), int(foody + SNAKE_BLOCK / 2)), SNAKE_BLOCK // 2)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake: # Making sure snake length with it's position
            del snake_List[0]
   

        for x in snake_List[:-1]: # Reverse - gameover
            if x == snake_Head:
                game_close = True
        
        for i, x in enumerate(snake_List):
            if i == len(snake_List) - 1:   #head
                pygame.draw.circle(dis, SNAKE_COLOR, (int(x[0] + SNAKE_BLOCK / 2), int(y1 + SNAKE_BLOCK / 2)), SNAKE_BLOCK // 2 + 1) 
            elif i == 0:  # tail part
                pygame.draw.circle(dis, SNAKE_COLOR, (int(x[0] + SNAKE_BLOCK / 2), int(x[1] + SNAKE_BLOCK / 2)), SNAKE_BLOCK // 2 - 0.5)  
            else:    # Regular body part
                pygame.draw.circle(dis, SNAKE_COLOR, (int(x[0] + SNAKE_BLOCK / 2), int(x[1] + SNAKE_BLOCK / 2)), SNAKE_BLOCK // 2)  
 
            # Eye parameters
            eye_radius = 1  # Radius of the inner black circle (pupil)
            outer_eye_radius = 3  # Radius of the outer white circle
            eye_offset_x = 4  # Horizontal offset for the eyes
            eye_offset_y = 2  # Vertical offset for the eyes

            # Left eye (white outer circle)
            pygame.draw.circle(dis, (255, 255, 255), (int(x1 + SNAKE_BLOCK / 2 - eye_offset_x), int(y1 + SNAKE_BLOCK / 2 - eye_offset_y)), outer_eye_radius)
            # Left eye (black inner circle)
            pygame.draw.circle(dis, (0, 0, 0), (int(x1 + SNAKE_BLOCK / 2 - eye_offset_x), int(y1 + SNAKE_BLOCK / 2 - eye_offset_y)), eye_radius)

            # Right eye (white outer circle)
            pygame.draw.circle(dis, (255, 255, 255), (int(x1 + SNAKE_BLOCK / 2 + eye_offset_x), int(y1 + SNAKE_BLOCK / 2 - eye_offset_y)), outer_eye_radius)
            # Right eye (black inner circle)
            pygame.draw.circle(dis, (0, 0, 0), (int(x1 + SNAKE_BLOCK / 2 + eye_offset_x), int(y1 + SNAKE_BLOCK / 2 - eye_offset_y)), eye_radius)

        your_score(dis, length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:            # When snake eats food
            foodx = round(random.randrange(0, dis_width - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - SNAKE_BLOCK) / 10.0) * 10.0
            length_of_snake += 1 

        pygame.time.Clock().tick(SNAKE_SPEED)

    pygame.quit()
    quit()
