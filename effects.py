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


class GitLine(Effect):
    """Line representing the path that git takes"""

    def __init__(self, screen, x, y, **kwargs):
        super().__init__(screen, **kwargs)
        self._x = x
        self._y = y
        self._top_direction = 1
        self._bottom_direction = -1
        self._line = (
            "--------------------------------------------------------------------"
        )
        self._arrow_pos_top = 0
        self._arrow_pos_bottom = len(self._line) - 1

    def reset(self):
        pass

    def _update(self, frame_no):
        # control movement speed by frame number
        if frame_no % 2 == 0:
            self._arrow_pos_top += self._top_direction
            self._arrow_pos_bottom += self._bottom_direction
        # ensure arrow index within line bounds
        self._arrow_pos_top = max(0, min(len(self._line) - 1, self._arrow_pos_top))
        self._arrow_pos_bottom = max(
            0, min(len(self._line) - 1, self._arrow_pos_bottom)
        )
        # render right arrow based on movement direction
        arrow_top = ">" if self._top_direction == 1 else "<"
        arrow_bottom = ">" if self._bottom_direction == 1 else "<"

        start_x = self._x - len(self._line) // 2

        # draw lines with arrow by replacing at position where arrow should currently be
        current_line_top = (
            self._line[: self._arrow_pos_top]
            + arrow_top
            + self._line[self._arrow_pos_top + 1 :]
        )
        current_line_bottom = (
            self._line[: self._arrow_pos_bottom]
            + arrow_bottom
            + self._line[self._arrow_pos_bottom + 1 :]
        )

        # change direction only if hit bounds and going in wrong direction (otherwise get infinite flip at bounds)
        if (
            self._arrow_pos_bottom >= len(self._line) - 1
            and self._bottom_direction == 1
        ) or (self._arrow_pos_bottom <= 0 and self._bottom_direction == -1):
            self._bottom_direction *= -1
        if (
            self._arrow_pos_top >= len(self._line) - 1 and self._top_direction == 1
        ) or (self._arrow_pos_top <= 0 and self._top_direction == -1):
            self._top_direction *= -1

        # print lines w arrows to screen
        self._screen.print_at(
            current_line_top,
            start_x,
            self._y + 5,
            Screen.COLOUR_GREEN,
            attr=Screen.A_BOLD,
        )
        self._screen.print_at(
            current_line_bottom,
            start_x,
            self._y - 5,
            Screen.COLOUR_GREEN,
            attr=Screen.A_BOLD,
        )

    @property
    def stop_frame(self):
        return 0


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
