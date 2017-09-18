import pygame
from pygame.sprite import Sprite

class Player(Sprite):
	# Classes always contain 2 parts:
	# 1. the __init__ section where you define all attributes. 
	# Init, only runs once. When the object is instantiated
	# Because this is a subclass, we need to call the parent's (Sprite) __init__
	def __init__(self,image,start_x,start_y,screen):
		super(Player,self).__init__()
		self.image = pygame.image.load('LiuKang.png')
		# self.image = pygame.transform.scale(self.image,(200,200))
		self.x = start_x
		self.y = start_y
		self.speed = 10
		self.screen = screen
		self.should_move_up = False
		self.should_move_down = False
		self.should_move_left = False
		self.should_move_right = False
	# 2. The methods where you define all the class functions (methods)

	def draw_me(self):
		#for the player to movesoff screen to right
		moveoffRight = False
		if(self.should_move_up):
			self.y -= self.speed
			if self.y <= 0:		#this if conditional makes the character come back on screen
				self.y = 800
		elif(self.should_move_down):
			self.y += self.speed
			if self.y >= 800:		#same as line 26
				self.y = 0
		if(self.should_move_left):
			self.x -= self.speed
			if self.x <= 0:			#this if condition makes the character come back on the other side of the screen
				self.x = 1000
		elif(self.should_move_right):
			self.x += self.speed
			if self.x >= 1000:		#same as line 30
				self.x = 0 
				# switch moveoffright to true
				moveoffRight = True
		self.screen.blit(self.image, [self.x,self.y])
		return moveoffRight
	def should_move(self,direction,yes_or_no):
		if(direction == "up"):
			# the up key is down. update self.
			self.should_move_up = yes_or_no
		if(direction == "down"):
			# the up key is down. update self.
			self.should_move_down = yes_or_no
		if(direction == "left"):
			# the up key is down. update self.
			self.should_move_left = yes_or_no
		if(direction == "right"):
			# the up key is down. update self.
			self.should_move_right = yes_or_no
