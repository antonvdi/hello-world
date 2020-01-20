import pygame, random
#cd C:\Users\Anton\Desktop\pro
#cd C:\Users\anton_mc03yx6\Documents\GitHub\hello-world
#cd C:\Users\Anton\Documents\GitHub\hello-world

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 32) 

def draw_snake(snake_list):
	for i in snake_list:
		pygame.draw.rect(screen, blue, [i[0], i[1], 18, 18])

def this_snake(snake_list, game_over):
	if game_over is False:
		for i in snake_list:
			pygame.draw.rect(screen, blue, [i[0], i[1], 18, 18])
	elif game_over is True:
		screen.fill(black)
		text = font.render('Game Over', True, white) 
		textRect = text.get_rect()  
		textRect.center = (400, 32)
		screen.blit(text, textRect) 
	return

def gameLoop():
	done = False
	game_over = False
	score = 0

	x = 800/2
	y = 600/2
	x_ch = 20
	y_ch = 0

	snake_list = []
	length_of_snake = 1
	score = 0

	length_of_snake = 3
	pressed = False

	foodx = random.randint(0, 39) * 20.0
	foody = random.randint(0, 29) * 20.0

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_UP or event.key == pygame.K_w) and pressed == False and y_ch == 0:
					y_ch = -20
					x_ch = 0
					pressed = True
				if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and pressed == False and y_ch == 0:
					y_ch = 20
					x_ch = 0
					pressed = True
				if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and pressed == False and x_ch == 0:
					x_ch = -20
					y_ch = 0
					pressed = True
				if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and pressed == False and x_ch == 0:
					x_ch = 20
					y_ch = 0
					pressed = True
				if (event.key == pygame.K_r):
					game_over = False
					screen.fill(black) 
					gameLoop()
		
		if x < 0 or x + 20 > 800 or y < 0 or y + 20 > 600:
			game_over = True

		x += x_ch
		y += y_ch

		snake = []
		snake.append(x)
		snake.append(y)
		snake_list.append(snake)

		if len(snake_list) > length_of_snake:
			del snake_list[0]

		for j in snake_list[:-1]:
			if j == snake:
				game_over = True

		draw_snake(snake_list)
		this_snake(snake_list, game_over)

		pygame.display.flip()	
		screen.fill(black)

		pygame.draw.rect(screen, red, pygame.Rect(foodx, foody, 18, 18))
		if x == foodx and y == foody:
			foodx = random.randint(0, 39) * 20.0
			foody = random.randint(0, 29) * 20.0
			length_of_snake += 1
			score += 1
			print(score)

		text = font.render('Score: ' + str(score), True, white) 
		textRect = text.get_rect()  
		textRect.center = (400, 32)
		screen.blit(text, textRect)

		pressed = False
		clock.tick(10)

gameLoop()