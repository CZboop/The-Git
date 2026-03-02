import sys

from asciimatics.scene import Scene
from asciimatics.screen import Screen

from effects import CenterText


def the_git(screen: Screen) -> None:
    """Main animation looping forever

    Args:
        screen (Screen): Screen passed from wrapper
    """
    # center_x = screen.width // 2
    center_y = screen.height // 2
    effects = [CenterText(screen, "THE GIT HAPPENS HERE", center_y)]

    scenes = [Scene(effects, -1)]  # -1 means loop forever
    screen.play(scenes, stop_on_resize=True)


if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(the_git)
            sys.exit(0)
        except Exception as e:
            print(f"Something went wrong - {e}")
