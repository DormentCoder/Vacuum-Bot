""" utils.py
#
# Some bits and pieces that are used in different places in the code.
#
# Written by: Simon Parsons
# Modified by: Helen Harman
# Last Modified: 01/02/24
"""

import random
import math
from enum import Enum

# Representation of directions
class Actions(Enum):
    MOVE_LEFT = 0
    MOVE_RIGHT = 1
    CLEAN  = 2
    STOP = 3
    NOOPS = 4 # no operations

# representation of game state
class State(Enum):
    PLAY = 0
    FINISHED  = 1
    
    
class Location(Enum):
    LEFT = 0
    RIGHT = 1
    
class LocState(Enum):
    CLEAR = 0
    DIRTY = 1

# Class to represent the position of elements within the game
#
class Pose():
    x = 0
    y = 0

    def print(self):
        print('[', self.x, ',', self.y, ']')
        
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Pose):
            return (self.x == other.x and self.y == other.y)
        return False

# Check if two game elements are in the same location
def same_location(pose1, pose2):
    return pose1 == pose2


# Define the order over two locations/poses by distance from origin
def ltPose(pose):
    origin = Pose()
    return separation(pose, origin)
    
# Return distance between two game elements.
def separation(pose1, pose2):
    return math.sqrt((pose1.x - pose2.x) ** 2 + (pose1.y - pose2.y) ** 2)

# Make sure that a location doesn't step outside the bounds on the world.
def check_bounds(max, dimension):
    if (dimension > max):
        dimension = max
    if (dimension < 0):
        dimension = 0

    return dimension

# Pick a location in the range [0, x] and [0, y]
#
# Used to randomize the initial conditions.
def pick_random_pose(x, y):
    p = Pose()
    p.x = random.randint(0, x)
    p.y = random.randint(0, y)

    return p

# Pick a unique location, in the range [0, x] and [0, y], given a list
# of locations that have already been chosen.

def pick_unique_pose(x, y, taken):
    unique_choice = False
    while(not unique_choice):
        candidate_pose = pick_random_pose(x, y)
        if not candidate_pose in taken:
            unique_choice = True
    return candidate_pose

# Check if a pose with the same x and y is already in poses (a list of poses).
#
def contained_in(pose, poses):
    return poses.contains(pose)


