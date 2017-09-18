# Duh
# We have access to pygame, because we did:
# $ pip install pygame
# it is NOT part of core. This is a 3rd party module.
import pygame
from pygame.sprite import Group, groupcollide

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
background_image = pygame.image.load('white_woods.png')

the_player = Player('LiuKang.png',50,30,screen)
# Make a bad_guy
bad_guy = Bad_guy(screen)
# make a group for the bad_guys
bad_guys = Group()
# add our bad_guy to the bad_guys group
bad_guys.add(bad_guy)
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
				new_bullet = Bullet(screen, the_player, 1)
				bullets.add(new_bullet)
				new_bullet = Bullet(screen, the_player, 3)
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

	# # Must be after fill, or we won't be able to see the hero
	# screen.blit(the_player.image, [the_player.x,the_player.y])
	the_player.draw_me()

	for bullet in bullets:
		# update teh bullet location
		bullet.update()
		# draw the bullet on the screen
		bullet.draw_bullet()

	# Check for collions...
	bullet_hit = groupcollide(bullets,bad_guys,True,True)
	# print bullet_hit

	# flip the screen, i.e.clear it so we can draw again... and again... and again
	pygame.display.flip()
