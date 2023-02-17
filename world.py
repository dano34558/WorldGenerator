import numpy as np
import math

class World:
    def __init__(self, size):
        self.size = size
        self.heightmap = np.zeros((size, size))

    def generate(self):
        # Generate semi-random island shape
        center = (self.size // 2, self.size // 2)
        radius = self.size // 4
        angle = 0
        neighbor_threshold = 0.25 * radius
        distance_threshold = 0.75 * radius
        current_point = center
        num_points = 500

        for i in range(num_points):
            angle += np.random.uniform(2, 4)
            distance = np.random.uniform(radius / 2, radius)

            new_point = (int(current_point[0] + distance * math.cos(math.radians(angle))), 
                        int(current_point[1] + distance * math.sin(math.radians(angle))))

            if np.linalg.norm(np.array(new_point) - np.array(center)) < distance_threshold:
                x, y = new_point
                for j in range(x-5, x+5):
                    for k in range(y-5, y+5):
                        if j >= 0 and j < self.size and k >= 0 and k < self.size:
                            self.heightmap[k, j] = 1


        

    def get_heightmap(self):
        # Return the heightmap array
        return self.heightmap
    


import pygame

class Visualize:
    def __init__(self, heightmap):
        self.heightmap = heightmap
        self.width = len(heightmap[0])
        self.height = len(heightmap)

    def visualize(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for i in range(self.width):
                for j in range(self.height):
                    height = self.heightmap[j][i]
                    if height < 0.5:
                        color = (0, 0, 255)
                    else:
                        color = (0, 255, 0)
                    pygame.draw.rect(screen, color, (i, j, 1, 1))

            pygame.display.flip()

        pygame.quit()


world = World(500)
world.generate()


v = Visualize(world.heightmap)
v.visualize()