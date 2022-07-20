import sys

import pygame

class Cube:
    """A simulation of a rubik's cube."""

    def __init__(self):
        """Initialize the cube."""
        pygame.init()
        self.screen = pygame.display.set_mode((1300, 700))

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

    def _update_screen(self):
        """Update the screen and flip to the new screen."""
        self.screen.fill((200, 200, 200))
        pygame.display.flip()

if __name__ == "__main__":
    # Make an instance of the cube and run it
    c = Cube()
    c.run_game()