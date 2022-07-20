class Colors:
    """To store the colors for the cube."""
    def __init__(self):
        self.colors:dict[str, tuple[int, int, int]] = {
            "black": (0, 0, 0),
            "white": (255, 255, 255),
            "red": (255, 0, 0),
            "blue": (0, 0, 255),
            "green": (0, 128, 0),
            "yellow": (255, 255, 0),
            "orange": (255, 165, 0),
        }