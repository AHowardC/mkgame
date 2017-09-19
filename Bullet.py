import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,screen,the_player,direction,image):
		super(Bullet, self).__init__()
		self.screen = screen

		self.rect = pygame.Rect(0,0,5,5) #changes painted bullet size (not the image)
		self.color = (255,255,255)	#255 is white 0 is black
		self.rect.centerx = the_player.x
		self.rect.top = the_player.y
		self.speed = 15
		self.direction = direction
		self.x = self.rect.x
		self.y = self.rect.y
		self.image = pygame.image.load(image) #this is to load the fireball variable image



	def update(self): #commented out in order to shoot in only one direction(right)
		if self.direction == 1: #up
			self.x += self.speed #change the y, each time update is run, by bullet speed
			self.rect.x = self.x #update rect position
		# elif self.direction == 2: #right
		# 	self.x += self.speed #change the y, each time update is run, by bullet speed
		# 	self.rect.x = self.x #update rect position
		# elif self.direction == 3: #down
		# 	self.y -= self.speed #change the y, each time update is run, by bullet speed
		# 	self.rect.y = self.y #update rect position
		else: #left
			self.x += self.speed #change the y, each time update is run, by bullet speed
			self.rect.x = self.x #update rect position


	def draw_bullet(self):
		#this is to make the fireball 	
		self.screen.blit(self.image, [self.x,self.y])


	def bullet_offscreen(self):
		if self.x >= 1050:
			return True
		else:
			return False