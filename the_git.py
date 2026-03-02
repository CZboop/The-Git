import sys

from asciimatics.scene import Scene
from asciimatics.screen import Screen

from effects import CenterText, Computer


def the_git(screen: Screen) -> None:
    """Main animation looping forever

    Args:
        screen (Screen): Screen passed from wrapper
    """
    center_x = screen.width // 2
    center_y = screen.height // 2

    # computer positions
    positions = {
        "top_left": (center_x - 25, center_y - 8),
        "top_right": (center_x + 10, center_y - 8),
        "bottom_left": (center_x - 25, center_y + 4),
        "bottom_right": (center_x + 10, center_y + 4),
        "top_middle": (center_x, center_y - 8),
        "bottom_middle": (center_x, center_y + 4),
    }

    effects = [
        CenterText(screen, "THE GIT HAPPENS HERE", center_y),
        Computer(screen, positions["top_left"][0], positions["top_left"][1]),
        Computer(screen, positions["top_right"][0], positions["top_right"][1]),
        Computer(screen, positions["bottom_left"][0], positions["bottom_left"][1]),
        Computer(screen, positions["bottom_right"][0], positions["bottom_right"][1]),
        Computer(screen, positions["top_middle"][0], positions["top_middle"][1]),
        Computer(screen, positions["bottom_middle"][0], positions["bottom_middle"][1]),
    ]

    scenes = [
        Scene(effects, -1),
    ]  # -1 means loop forever
    screen.play(scenes, stop_on_resize=True)


if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(the_git)
            sys.exit(0)
        except Exception as e:
            print(f"Something went wrong - {e}")
