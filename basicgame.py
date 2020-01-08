import pygame, random
#cd C:\Users\Anton\Desktop\pro

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

done = False

x = 10
y = 10
vx = 20
vy = 0
len = 2

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				vy = -20
				vx = 0
			if event.key == pygame.K_DOWN:
				vy = 20
				vx = 0
			if event.key == pygame.K_LEFT:
				vx = -20
				vy = 0
			if event.key == pygame.K_RIGHT:
				vx = 20
				vy = 0
	xs[len] = xs
	
	pygame.display.flip()
		
	pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(x+1, y+1, 18, 18))
	x = x + vx
	y = y + vy
	clock.tick(6)
	
	