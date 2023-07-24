import pygame
import random

from game.components.power_ups.shield import Shield

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)
        self.duration = random.randint(3000, 5000)

    def update(self, game ):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up(game.game_speed, self.power_ups )

        for power_up in self.power_ups:
            power_up.update()

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self):
        power_up = Shield()
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)