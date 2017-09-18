# Duh
# We have access to pygame, because we did:
# $ pip install pygame
# it is NOT part of core. This is a 3rd party module.
import pygame
from pygame.sprite import Group, groupcollide
from random import randint
# -----CUSTOM CLASSES HERE-----
from Player import Player
from Bad_guy import Bad_guy
from Bullet import Bullet

# Have to init the pygame object so we can use it
pygame.init()

# Screen size is a tuple
screen_size = (1000,800)


# Because we are going to paint the background, we need a tuple for the color
#background_color = (82,111,53)

# Create a screen for pygame to use to draw on
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("An epic fighter made with python")
imagebg = '1theKove.png'
background_image = pygame.image.load(imagebg)

the_player = Player('LiuKang.png',10,550,screen)
# Make a bad_guy
sonyablade = Bad_guy(screen,"sonyablade.png")
reptile = Bad_guy(screen,"reptile.png")
jade = Bad_guy(screen,"jade.png")
johnnyCage = Bad_guy(screen,"johnnycage.png")
kitana = Bad_guy(screen,"kitana.png")
jax = Bad_guy(screen,"jax.png")
jaxx = Bad_guy(screen,"jaxx.png")
sonyablade2 = Bad_guy(screen,"sonyablade2.png")
mileena = Bad_guy(screen,"mileena.png")
subzero = Bad_guy(screen,"subzero.png")
raiden = Bad_guy(screen,"raiden.png")
scorpion = Bad_guy(screen,"scorpion.png")
goro = Bad_guy(screen,"Goro.png")
imageList = [
'sonyablade.png',
'reptile.png',
'jade.png',
'johnnycage.png',
'kitana.png',
'jax.png',
'jaxx.png',
'sonyablade2.png',
'mileena.png',
'subzero.png',
'raiden.png',
'scorpion.png',
'goro.png'
]
levelcounter = 0
imagebg = [
		'1theKove.png',
		'2lin_kuei_temple.png',
		'3raiden_chamber.png',
		'4mkxbg.png',
		'5gorobg.png',
		'6white_woods.png'
		]

# make a group for the bad_guys
bad_guys = Group()
# add our bad_guy to the bad_guys group
bad_guys.add(reptile)
# Make a new Group called bullets. Group is a pygame "list"
bullets = Group()

# the_player_image = pygame.image.load('batman.png')
# player = {
# 	"x": 100,
# 	"y": 100
# }

game_on = True
# Set up the main game loop
while game_on: #will run forever (until break)
	# Loop through all the pygame events.
	# This is pygames escape hatch. (Quit)
	for event in pygame.event.get():
		# print event
		if event.type == pygame.QUIT:
			game_on = False
		elif event.type == pygame.KEYDOWN:
			print event.key
			# print "User pressed a key!!!"
			if event.key == 273:
				# user pressed up!
				# the_player.y -= the_player.speed
				the_player.should_move("up",True)
			elif event.key == 274:
				# the_player.y += the_player.speed
				the_player.should_move("down",True)
			if event.key == 275:
				# the_player.x += the_player.speed
				the_player.should_move("right",True)
			elif event.key == 276:
				# the_player.x -= the_player.speed
				the_player.should_move("left",True)
			elif event.key == 32:
				# 32 = SPACE BAR... FIRE!!!!
				new_bullet = Bullet(screen, the_player, 1,'haduken.png')
				bullets.add(new_bullet)
		elif event.type == pygame.KEYUP:
			if event.key == 273:
				the_player.should_move("up",False)
			elif event.key == 274:
				the_player.should_move("down",False)
			if event.key == 275:
				the_player.should_move("right",False)
			elif event.key == 276:
				the_player.should_move("left",False)

	# print bullets

	# paint the screen
	#screen.fill(background_color)
	screen.blit(background_image, [0,0])

	for bad_guy in bad_guys:
		# update the bad guy (based on where the player is)
		bad_guy.update_me(the_player)
		# draw the bad guy
		bad_guy.draw_me()

	# Must be after fill, or we won't be able to see the hero
	# screen.blit(the_player.image, [the_player.x,the_player.y])
	moveoffRight = the_player.draw_me()
	if moveoffRight:
		
		levelcounter += 1
		#randBg = randint(0,len(imagebg) - 1)
		if levelcounter > (len(imagebg) - 1):
			levelcounter = 0 
		background_image = pygame.image.load(imagebg[levelcounter])

	for bullet in bullets:
		# update teh bullet location
		bullet.update()
		# draw the bullet on the screen
		bullet.draw_bullet()

	# Check for collions...
	bullet_hit = groupcollide(bullets,bad_guys,True,True)
	# make new badguy characters appear
	if bullet_hit:
		randNum = randint(0,len(imageList) - 1 )
		bad_guys.add(Bad_guy(screen,imageList[randNum]))
	# print bullet_hit

	# flip the screen, i.e.clear it so we can draw again... and again... and again
	pygame.display.flip()
