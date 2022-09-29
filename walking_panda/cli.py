from .panda import WalkingPanda


def cli():
    walking = WalkingPanda()
    walking.run()

from . import panda

import argparse

def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate", help="Suppress Rotation",
                        action="store_true")
    parser.add_argument("--scale", help="Enlarge panda",
                        action="store_true")


    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()


