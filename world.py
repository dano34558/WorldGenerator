import numpy as np
import math

class World_Creator:
    def __init__(self, width, height, scale_x, scale_y, initial_shape_randomness, smoothing, height_map_modifier_intencity, height_map_smoothing):
        self.width = width
        self.height = height
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.initial_shape_randomness = initial_shape_randomness
        self.smoothing = smoothing
        self.height_map_modifier_intencity = height_map_modifier_intencity
        self.height_map_smoothing = height_map_smoothing
        self.tile_map = np.zeros((self.height, self.width))

    def generate_circle_island(self):
        center = (self.width // 2, self.height // 2)
        radius = self.width // 4

        for i in range(self.width):
            for j in range(self.height):
                distance = np.linalg.norm(np.array((i, j)) - np.array(center))
                if distance < radius:
                    self.tile_map[i][j] = 255

    def add_randomness(self):
        for i in range(self.width):
            for j in range(self.height):
                distance_to_center = np.linalg.norm(np.array((i, j)) - np.array((self.width // 2, self.height // 2)))
                randomness = self.initial_shape_randomness * (distance_to_center / (self.width // 2))
                randomness *= math.pi / 2
                randomness = np.random.normal(0, randomness)
                self.tile_map[i][j] += randomness
                self.tile_map[i][j] = max(min(self.tile_map[i][j], 255), 0)
