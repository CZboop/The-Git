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
        self._spinner_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

    def stop_frame(self):
        pass

    def reset(self):
        pass

    def _update(self, frame_no):
        colour = self._colours[(frame_no // 5) % len(self._colours)]
        current_spinner_char = self._spinner_chars[
            (frame_no // 5) % len(self._spinner_chars)
        ]
        x = (self._screen.width - len(self._text)) // 2

        self._screen.print_at(
            f"{current_spinner_char} {self._text} {current_spinner_char}",
            x,
            self._y,
            colour,
            attr=Screen.A_BOLD,
        )
