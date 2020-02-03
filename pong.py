import pygame, random, time

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 32) 

class player:
	def __init__(player, name, xpos, ypos, pwidth, pheight, speed, score):
		player.name = name
		player.xpos = xpos
		player.ypos = ypos
		player.pwidth = pwidth
		player.pheight = pheight
		player.speed = speed
		player.score = score

	def update(player):
		if (player.ypos >= 0) and (player.ypos <= height - player.pheight): 
			player.ypos += player.speed
		elif (player.ypos >= 0) and (player.speed < 0):
			player.ypos += player.speed
		elif (player.ypos <= height - player.pheight) and (player.speed > 0):
			player.ypos += player.speed
		pygame.draw.rect(screen, red, pygame.Rect(player.xpos, player.ypos, player.pwidth, player.pheight))

class ball:
	def __init__(ball, xpos, ypos, bwidth, bheight, xspeed, yspeed):
		ball.xpos = xpos
		ball.ypos = ypos
		ball.bwidth = bwidth
		ball.bheight = bheight
		ball.xspeed = xspeed
		ball.yspeed = yspeed

	def updateball(ball, player1, player2):
		ball.xpos += ball.xspeed
		ball.ypos += ball.yspeed
		pygame.draw.rect(screen, blue, pygame.Rect(ball.xpos, ball.ypos, ball.bwidth, ball.bheight))

		if (ball.xpos <= 0):
			ball.xspeed *= -1
			player1.score += 1
			print(str(player1.name) + ": " + str(player1.score))
			serve(ball)
		if (ball.xpos + ball.bwidth >= width):
			ball.xspeed *= -1
			player2.score += 1
			print(str(player2.name) + ": " + str(player2.score))
			serve(ball)
		if (ball.xpos + ball.bwidth >= player1.xpos) and ((ball.ypos + ball.bheight >= player1.ypos) and (ball.ypos <= player1.ypos + player1.pheight)):
			ball.xspeed *= -1
		if (ball.xpos <= player2.xpos + player2.pwidth) and ((ball.ypos + ball.bheight >= player2.ypos) and (ball.ypos <= player2.ypos + player2.pheight)):
			ball.xspeed *= -1
		if (ball.ypos <= 0) or (ball.ypos + ball.bheight >= height):
			ball.yspeed *= -1

xspeed = random.uniform(0.5, 1)
yspeed = 1-xspeed
ball1 = ball(width/2, height/2, 10, 10, xspeed, yspeed)

def gameLoop():
	player1 = player("Player 1", width-30, height/2, 10, 100, 0, 0)
	player2 = player("Player 2", 20, height/2, 10, 100, 0, 0)
	serve(ball1)
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_UP):
					player1.speed = -0.5
				if (event.key == pygame.K_DOWN):
					player1.speed = 0.5
				if (event.key == pygame.K_w):
					player2.speed = -0.5
				if (event.key == pygame.K_s):
					player2.speed = 0.5
			if event.type == pygame.KEYUP:
				if (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
					player1.speed = 0
				if (event.key == pygame.K_w) or (event.key == pygame.K_s):
					player2.speed = 0

		screen.fill(white)
		player.update(player1)
		player.update(player2)

		ball.updateball(ball1, player1, player2)

		text = font.render('Player 2: ' + str(player2.score) + ' / Player 1: ' + str(player1.score), True, black) 
		textRect = text.get_rect()  
		textRect.center = (400, 32)
		screen.blit(text, textRect)

		clock.tick(1000)
		pygame.display.flip()
		
def serve(ball1):
	ball1.xspeed = random.uniform(0.5, 1.0)
	ball1.yspeed = 1-ball1.xspeed
	ball1.xpos = width/2
	ball1.ypos = height/2
	time.sleep(1)
	return (ball1)

gameLoop()