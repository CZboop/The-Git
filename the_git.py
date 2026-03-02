from asciimatics.effects import Print, Cycle
from asciimatics.renderers import FigletText, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.sprites import Arrow, Sprite
from asciimatics.paths import Path
from asciimatics.effects import Effect
import sys
from effects import CenterText
import random


def the_git(screen: Screen):
    """Main animation looping forever

    Args:
        screen (Screen): _description_
    """
    center_x = screen.width // 2
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
