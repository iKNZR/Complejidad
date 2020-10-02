import pygame #importación de la librería Pygame
from pygame.locals import *
from sys import exit
import random

class Barra(pygame.sprite.Sprite): #se crea una función barra
   def __init__(self, width, height,cuadro,columna):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface((width,height)).convert()     #propiedades de imagen de la barra
      self.image.fill((0,0,0))
      self.rect = self.image.get_rect()
      self.columna = columna
      self.cuadro = cuadro
   def update(self,mouse): #se define la actualización de los eventos 
       #análisis de eventos de click
      if num_barra_clicked == 0: #barra no colocada
         if self.rect.collidepoint(mouse): 
            self.image.fill((255,0,0))
            if self.rect.width > self.rect.height:
               hor_redbarra_list.add(self)
            elif self.rect.height > self.rect.width:
               vert_redbarra_list.add(self)
      elif num_barra_clicked == 1:  #se especifica la aparición de una barra cuando se haga click en un determinado punto
         if self.rect.collidepoint(mouse) and self.rect.width > self.rect.height:
            for barra in hor_redbarra_list: #en caso de haberse hecho click en un espacio "vacío" este se tornará de color rojo y adquiere otra propiedad
               if barra.cuadro == self.cuadro and abs(barra.columna - self.columna) == 1:
                  self.image.fill((255,0,0))
         elif self.rect.collidepoint(mouse) and self.rect.width < self.rect.height:
            for barra in vert_redbarra_list:
               if barra.columna == self.columna and abs(barra.cuadro - self.columna) == 1:
                  self.image.fill((255,0,0))

class Player(pygame.sprite.Sprite): #creación de la función jugador o player
   def __init__(self,image,cuadro,columna):
      pygame.sprite.Sprite.__init__(self)   #uso de la funcion "self" para especificar que el uso de las funciones está sobre el objeto Player
      self.image = pygame.image.load(image) #carga de sprites del jugador
      self.rect = self.image.get_rect()
      self.columna = columna
      self.cuadro = cuadro
      self.update_position() 
   def update_position(self): #actualización de la posición en que se encuentre la pieza
      self.rect.y = self.cuadro*50 + 20
      self.rect.x = self.columna*50 + 23
 
   def update(self,mouse): #actualización de los eventos del mouse
      move_blocked = 0
      if self.rect.collidepoint(mouse):
          #eventos de movimiento de las piezas manteniendo click sobre la pieza
         if event.key == K_RIGHT:  #derecha
            for barra in vert_redbarra_list:
               if barra.cuadro == self.cuadro and barra.columna == self.columna:
                  move_blocked = 1
            if move_blocked == 0: self.columna += 1
            if self.columna >= 8: self.columna = 8
         elif event.key == K_UP: #arriba
            for barra in hor_redbarra_list:
               if barra.cuadro == self.cuadro - 1 and barra.columna == self.columna:
                  move_blocked = 1
            if move_blocked == 0: self.cuadro -= 1
            if self.cuadro < 0: self.cuadro = 0
         elif event.key == K_DOWN: #abajo
            for barra in hor_redbarra_list:
               if barra.cuadro == self.cuadro and barra.columna == self.columna:
                  move_blocked = 1
            if move_blocked == 0: self.cuadro += 1
            if self.cuadro >= 8: self.cuadro = 8
         elif event.key == K_LEFT: #izquierda
            for barra in vert_redbarra_list:
               if barra.cuadro == self.cuadro and barra.columna == self.columna - 1:
                  move_blocked = 1
            if move_blocked == 0: self.columna -= 1
            if self.columna <= 0: self.rect.x = 0
      self.update_position()

pygame.init() #Se inicia el juego apoyado de la librería pygame
screen = pygame.display.set_mode([470,470]) #Se define el tamaño de la ventana
pygame.display.set_caption("Trabajo Parcial") #Se especifica el nombre de la ventana
 

back = pygame.Surface((470,470)) #Se pinta la superficie
background = back.convert()
background.fill((255,255,255)) #Se rellena la superficie de color blanco = (255, 255, 255)

#se llama a los componentes
barra_list = pygame.sprite.Group()
hor_barra_list = pygame.sprite.Group() #barra horizontal sin pintar
vert_barra_list = pygame.sprite.Group() #barra vertical sin pintar
hor_redbarra_list = pygame.sprite.Group() #barra horizontal pintada
vert_redbarra_list = pygame.sprite.Group() #barra vertical pintada
player1_group = pygame.sprite.Group()   #Primer player o jugador 
player2_group = pygame.sprite.Group()   #Segundo jugador
player_list = pygame.sprite.Group() 
all_sprites_list = pygame.sprite.Group() 

#se especifican las coordenadas para la barra en x e y
barra_coord_x = [60,110,160,210,260,310,360,410] 
barra_coord = barra_coord_x
barra_coord_y = [10,60,110,160,210,260,310,360,410]

#Creación de la cuadrícula especificando dejar los espacios vacíos para los cuadros del tablero
for cuadro in range(0,9):
   for columna in range(0,8):
      barra_vert = Barra(5, 50, cuadro, columna)
      barra_vert.rect.x = barra_coord_x[columna]
      barra_vert.rect.y = barra_coord_y[cuadro]
      vert_barra_list.add(barra_vert)
      barra_list.add(barra_vert)
      all_sprites_list.add(barra_vert)

for cuadro in range(0,8):
   for columna in range(0,9):
      barra_hor = Barra(50,5, cuadro, columna)
      barra_hor.rect.x = barra_coord_y[columna]
      barra_hor.rect.y = barra_coord_x[cuadro]
      hor_barra_list.add(barra_hor)
      barra_list.add(barra_hor)
      all_sprites_list.add(barra_hor)

#importación de los datos del jugador 1, sprite, grupo
player1 = Player('piece1.png',0,4)
player1_group.add(player1)
player_list.add(player1)
all_sprites_list.add(player1)

#importación de los datos del jugador 2, sprite, grupo
player2 = Player('piece2.png',8,4)
player2_group.add(player2)
player_list.add(player2)
all_sprites_list.add(player2) 

num_barra_clicked= 0 #se inicia con 0 barras pintadas de rojo
p1_turn = 1 #el turno inicia con el jugador 1 ubicado en la parte inferior de la pantalla
num_moves = 0 #movimientos en 0 al inicio

#creación de un ciclo while en que estará ejecutándose el juego
while 1:
   mouse = pygame.mouse.get_pos()
   for event in pygame.event.get():
      if event.type == QUIT:
         exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
         barra_list.update(mouse)
         if num_barra_clicked == 0: 
            num_moves +=1
            num_barra_clicked = 1
         else: num_barra_clicked = 0
      if event.type == pygame.KEYDOWN:
         if p1_turn == 1:
            player1_group.update(mouse)
            p1_turn = 0
            num_moves += 1 
         elif p1_turn == 0:
            player2_group.update(mouse)
            p1_turn = 1
            num_moves += 1
   screen.blit(background,(0,0))
   pygame.draw.rect(screen,(0,0,0),Rect((10,10),(450,450)),5)
   all_sprites_list.draw(screen)
   pygame.display.update()


