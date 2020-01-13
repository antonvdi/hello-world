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

def draw_snake(snake_list):
	for i in snake_list:
		pygame.draw.rect(screen, blue, [i[0], i[1], 18, 18])
	return

def gameLoop():
	done = False

	x = 800/2
	y = 600/2
	x_ch = 20
	y_ch = 0

	snake_list = []
	length_of_snake = 1
	score = 0

	foodx = random.randint(0, 39) * 20.0
	foody = random.randint(0, 29) * 20.0

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					y_ch = -20
					x_ch = 0
				elif event.key == pygame.K_DOWN:
					y_ch = 20
					x_ch = 0
				elif event.key == pygame.K_LEFT:
					x_ch = -20
					y_ch = 0
				elif event.key == pygame.K_RIGHT:
					x_ch = 20
					y_ch = 0
		
		if x < 0 or x + 20 > 800 or y < 0 or y + 20 > 600:
			done = True

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
				done = True

		draw_snake(snake_list)

		pygame.display.flip()	
		screen.fill(black)

		pygame.draw.rect(screen, red, pygame.Rect(foodx, foody, 18, 18))
		if x == foodx and y == foody:
			foodx = random.randint(0, 39) * 20.0
			foody = random.randint(0, 29) * 20.0
			length_of_snake += 1
			score += 1
			print(score)

		clock.tick(10)

gameLoop()