from asciimatics.effects import Effect
from asciimatics.screen import Screen

COMPUTER_SHAPE = [
    "       .----------------------------.",
    "      /                           / |",
    "     /_  __ _____________________/  |",
    "    |                            |  |",
    "    |    _____________________   |  |",
    "    |   |                     |  |  |",
    "    .---|                     |--.  |",
    "    |   |                     |  |  |",
    "    |   |                     |  |  |",
    "    |   |_____________________|  |  |",
    "    |     (O)            :::     |  |",
    "    |____________________________|/",
    "               |       |",
    "    .----------|       |----------.",
    "   /   [=][=][=][=][=][=][=][=]   /|",
    "  /   [=][=][=][=][=][=][=][=]   / /",
    " /   [==================][=]    / /",
    "/______________________________/ /",
    "|______________________________|/",
]


class Computer(Effect):
    """Draw computer ASCII art at given fixed position."""

    def __init__(self, screen, x, y, label="", **kwargs):
        super().__init__(screen, **kwargs)
        self._x = x
        self._y = y
        self._label = label

    def reset(self):
        pass

    def _update(self, frame_no):
        for i, line in enumerate(COMPUTER_SHAPE):
            self._screen.print_at(
                line, self._x, self._y + i, Screen.COLOUR_GREEN, attr=Screen.A_BOLD
            )
        if self._label:
            label_x = self._x + (len(COMPUTER_SHAPE[0]) - len(self._label)) // 2
            self._screen.print_at(
                self._label, label_x, self._y - 1, Screen.COLOUR_WHITE
            )

    @property
    def stop_frame(self):
        return 0


class CenterText(Effect):
    """Pulsing center text effect."""

    def __init__(self, screen, text, y, **kwargs):
        super().__init__(screen, **kwargs)
        self._text = text
        self._y = y
        self._spinner_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

    @property
    def stop_frame(self):
        return 0

    def reset(self):
        pass

    def _update(self, frame_no):
        colour = Screen.COLOUR_GREEN
        current_spinner_char = self._spinner_chars[
            (frame_no // 5) % len(self._spinner_chars)
        ]
        x = (self._screen.width - len(self._text)) // 2

        # TODO: convert text to figlet? but needs render per-line not just print, and prob split into words for width
        self._screen.print_at(
            f"{current_spinner_char} {self._text} {current_spinner_char}",
            x,
            self._y,
            colour,
            attr=Screen.A_BOLD,
        )
