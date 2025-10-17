""" game.py
#
# The top level loop that runs the world until it is clean.
#
# run this using:
#
# python3 game.py
#
# Written by: Simon Parsons
# Modified by: Helen Harman
# Last Modified: 01/02/24
"""

from world import World
from vacuum  import Vacuum
from dirtyEnvironment import DirtyEnvironment
import random
import config
import utils
import time

def run_vacuum_world():
    # How we set the game up. Create a world, then connect player and
    # display to it.
    world = World()
    player = Vacuum(world)
    display = DirtyEnvironment(world)

    # Show initial state
    display.update()
    time.sleep(1)

    # Now run the game...
    while not(world.isEnded()):
        world.update_vacuum(player.make_move())
        display.update()
        time.sleep(1)
        
if __name__ == '__main__':
    run_vacuum_world()

