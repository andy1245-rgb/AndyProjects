import pygame
from time import sleep

pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
black = (0, 0, 0)
grey = (100,100,100)
white = (200,200,200)
pop = 2

pop1 = f"{pop}"

nextbutton = pygame.image.load('nextbutton.png')

fontname = 'freesansbold.ttf'
fontsize = 30
font = pygame.font.Font(fontname, fontsize)
population = 'population : ' + pop1
antialias = True
colour = 0,0,0
populationtext = font.render(population, antialias, colour)

# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error

# render text
year = 1
year1 = f'{year}'

dead = False
while not dead:
	gameDisplay.blit(nextbutton,(100,100))
	pop1 = f"{pop}"
	for event in pygame.event.get():
		x = 1
	pos = pygame.mouse.get_pos()
	if event.type == pygame.MOUSEBUTTONDOWN: #and pos[0] >=
		#fdsfsdf
		x = 2 
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_SPACE or pygame.K_UP:
			year += 1
			sleep(0.35)
			if pop <= 5000:
				startgame = True
				midgame = False
				endgame = False
			elif pop <= 50000:
				midgame = True
				startgame = False
				endgame = False
			else:
				endgame = True
				startgame = False
				midgame = False
			if year/18 == round(year/18):
				pop -= round(pop/10)
			elif pop <= 8:
				pop += 1
			elif startgame == True:
				pop = round((pop/5) + pop) 
			elif midgame == True:
				pop = round((pop/18) + pop)
			elif endgame == True:
				pop = round((pop/35) + pop)
	year1 = f'{year}'
	gameDisplay.fill(white)
	fontname = 'freesansbold.ttf'
	fontsize = 30
	font = pygame.font.Font(fontname, fontsize)
	population = 'Population : ' + pop1
	yr = 'year ' + year1
	antialias = True
	colour = 0,0,0
	yeartext = font.render(yr, antialias, colour)
	populationtext = font.render(population, antialias, colour)
	gameDisplay.blit(populationtext,(0,0))
	gameDisplay.blit(yeartext,(600,0))

	

	pygame.display.update()

pygame.quit()
quit()
