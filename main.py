# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

from player import Player


def main():
   print("Starting Asteroids!")
   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")

   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

   clock = pygame.time.Clock()
   dt = 0

   updatable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   
   Player.containers = (updatable, drawable)

   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


   running = True
   while running:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return
   
      screen.fill((0,0,0))
      dt = clock.tick(60.0) / 1000

      updatable.update(dt)

      for obj in drawable:
         obj.draw(screen)

      pygame.display.flip()

       

if __name__ == "__main__":
    main()
