import pygame
from Particle import Particle
from random import randint
from sys import exit
from functions_geometrics import euclidean_distance



def main():
    pygame.init()
    WIDTH, HEIGHT = 1450,900
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Particle Collider")
    clock = pygame.time.Clock()

    #background surface
    bg  = pygame.Surface((WIDTH , HEIGHT))
    bg.fill((20,20,20))
    frames =[]
    particles = []
    for i in range (0,80):
        pos = (randint(620,660) , randint(310,340))
        speed = randint(4,6)
        radius = 3
        particles.append(Particle(pos , (1,1),speed,radius,(255, 215 , 0)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                exit()
        screen.blit(bg,(0,0))

        #Draw Lines between particles
        for particle in particles:
            for point in particles:
                distance = euclidean_distance(particle.pos , point.pos)
                if distance <255:
                    color = (max(0, 255 - distance), max(0, 215 - distance), max(0, 0 - distance))
                    pygame.draw.aaline(screen , color , particle.pos , point.pos , 3)

        #draw the particle
        for particle in particles:
            pygame.draw.circle(screen , particle.color, particle.pos , particle.radius)
        #draw guidance
        for particle in particles:
            particle.guidance([0,WIDTH , 0,HEIGHT],particles)

        #update position        
        for particle in particles:
            particle.update_pos()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
	main()


