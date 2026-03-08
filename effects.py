import random

from asciimatics.effects import Effect
from asciimatics.renderers import FigletText
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


class Sparkles(Effect):
    """Random sparkles around specific areas."""

    def __init__(self, screen, positions, radius=10, density=0.05, **kwargs):
        super().__init__(screen, **kwargs)
        self._positions: list[tuple[int, int]] = positions  # x, y tuples
        self._radius = radius
        self._density = density
        self._sparkle_chars = [
            "*",
            "✦",
            "✧",
            "·",
            "°",
            "⁕",
            "✳",
            "✴",
            "✶",
            "*",
        ]
        self._sparkles = []  # active sparkles tracked

    def reset(self):
        self._sparkles = []

    def _update(self, frame_no):
        # spawn new sparkles randomly
        for cx, cy in self._positions:
            # random spawning, controlled by density
            if random.random() < self._density:
                # get centre x,y of cluster
                cluster_x = cx + random.randint(-self._radius, self._radius)
                cluster_y = cy + random.randint(-self._radius, self._radius)

                # spawn cluster of sparkles close to centre
                num_in_cluster = random.randint(2, 5)
                cluster_radius = 2
                for _ in range(num_in_cluster):
                    spark_x = cluster_x + random.randint(
                        -cluster_radius, cluster_radius
                    )
                    spark_y = cluster_y + random.randint(
                        -cluster_radius, cluster_radius
                    )
                    char = random.choice(self._sparkle_chars)
                    lifetime = random.randint(4, 10)
                    self._sparkles.append([spark_x, spark_y, char, lifetime])

        # draw and age/remove sparkles
        new_sparkles = []
        for sparkle in self._sparkles:
            x, y, char, lifetime = sparkle
            if lifetime > 0:
                colour = Screen.COLOUR_WHITE
                self._screen.print_at(char, x, y, colour)
                sparkle[3] -= 1
                new_sparkles.append(sparkle)
            # clear the sparkle once time to live runs out (space in its place)
            else:
                self._screen.print_at(" ", x, y)

        self._sparkles = new_sparkles

    @property
    def stop_frame(self):
        return 0


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
        self._fig = FigletText(text, font="banner4")
        images = list(self._fig.rendered_text)
        self._image = images[0]

    @property
    def stop_frame(self):
        return 0

    def reset(self):
        pass

    def _update(self, frame_no):
        colour = Screen.COLOUR_GREEN
        x = (self._screen.width - self._fig.max_width) // 2

        for i, line in enumerate(self._image):
            self._screen.print_at(line, x, self._y + i, colour, attr=Screen.A_BOLD)
