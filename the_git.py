import sys

from asciimatics.scene import Scene
from asciimatics.screen import Screen

from effects import COMPUTER_SHAPE, CenterText, Computer, GitLine, Sparkles


def the_git(screen: Screen) -> None:
    """Main animation looping forever

    Args:
        screen (Screen): Screen passed from wrapper
    """
    center_x = screen.width // 2
    center_y = screen.height // 2

    # computer positions
    computer_width = len(COMPUTER_SHAPE[0])
    computer_height = len(COMPUTER_SHAPE)

    positions = {
        "top_left": (
            center_x - int(computer_width * 2),
            center_y - computer_height // 2,
        ),
        "top_right": (center_x + (computer_width), center_y - computer_height // 2),
    }
    # get computer centres to randomise sparkles roughly within their bounds
    computer_centres = [
        (
            positions["top_left"][0] + computer_width // 2,
            positions["top_left"][1] + computer_height // 2,
        ),
        (
            positions["top_right"][0] + computer_width // 2,
            positions["top_right"][1] + computer_height // 2,
        ),
    ]

    effects = [
        CenterText(screen, "THE GIT HAPPENS HERE", center_y),
        Computer(screen, positions["top_left"][0], positions["top_left"][1]),
        Computer(screen, positions["top_right"][0], positions["top_right"][1]),
        GitLine(screen, center_x, center_y),
        Sparkles(
            screen,
            positions=computer_centres,
            radius=min(computer_height, computer_width),
        ),
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
