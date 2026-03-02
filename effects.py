from asciimatics.effects import Effect
from asciimatics.screen import Screen


class CenterText(Effect):
    """Pulsing center text effect."""

    def __init__(self, screen, text, y, **kwargs):
        super().__init__(screen, **kwargs)
        self._text = text
        self._y = y
        self._colours = [
            Screen.COLOUR_WHITE,
            Screen.COLOUR_CYAN,
            Screen.COLOUR_MAGENTA,
            Screen.COLOUR_YELLOW,
        ]

    def stop_frame(self):
        pass

    def reset(self):
        pass

    def _update(self, frame_no):
        colour = self._colours[(frame_no // 5) % len(self._colours)]
        x = (self._screen.width - len(self._text)) // 2

        # Draw a box around the text
        box_width = len(self._text) + 4
        box_x = x - 2

        self._screen.print_at(
            "╔" + "═" * (box_width - 2) + "╗", box_x, self._y - 1, colour
        )
        self._screen.print_at(
            "║ " + self._text + " ║", box_x, self._y, colour, attr=Screen.A_BOLD
        )
        self._screen.print_at(
            "╚" + "═" * (box_width - 2) + "╝", box_x, self._y + 1, colour
        )
