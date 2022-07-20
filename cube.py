import sys
import random

import pygame

from colors import Colors

class Cube:
    """A simulation of a rubik's cube."""

    def __init__(self):
        """Initialize the cube."""
        pygame.init()
        self.screen = pygame.display.set_mode((1300, 700))
        self.screen_rect = self.screen.get_rect()

        self.colors = Colors()

        self.face1 = [
            ["white", "yellow", "blue"],
            ["red", "green", "orange"],
            ["blue", "blue", "white"]
        ]

    def run_game(self):
        """Start the window and keep it running."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_cube(self):
        """Create cube."""
        pos_i, pos_j = 0, 0
        for i in range(50, 200, 50):
            for j in range(50, 200, 50):
                cube = pygame.Rect(i, j, 49, 49)
                now = self.face1[pos_j][pos_i]
                color_now = self.colors.colors[now]
                pygame.draw.rect(self.screen, color_now, cube)
                pos_j += 1
            pos_i += 1
            pos_j = 0

    def _update_screen(self):
        """Update the screen and flip to the new screen."""
        self.screen.fill((200, 200, 200))
        self._create_cube()
        pygame.display.flip()

if __name__ == "__main__":
    # Make an instance of the cube and run it
    c = Cube()
    c.run_game()