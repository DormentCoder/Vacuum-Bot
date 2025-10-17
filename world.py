""" world.py
#
# A file that represents the Vacuum World, keeping track of the
# position of all the objects and the agent, and
# moving them when necessary.
#
# Written by: Simon Parsons
# Modified by: Helen Harman
# Last Modified: 01/02/24
"""

import random
import config
import utils
from utils import Pose
from utils import Actions
from utils import State

class World():

    def __init__(self):

        # Import boundaries of the world. because we index from 0,
        # these are one less than the number of rows and columns.
        self.maxx = config.WORLD_LENGTH - 1
        self.maxy = config.WORLD_BREADTH - 1

               
        # Vacuum
        loc = utils.pick_random_pose(self.maxx, self.maxy)
        self.vacuum_loc = loc
        
        # Dirt
        self.dirty_locations = []
        for i in range(config.NUMBER_OF_DIRTY_LOCATIONS):
            loc = utils.pick_unique_pose(self.maxx, self.maxy, self.dirty_locations) 
            self.dirty_locations.append(loc)

        # Game state
        self.status = State.PLAY

        
    #--------------------------------------------------
    # Access Methods
    #
    # These are the functions that should be used by Link to access
    # information about the world.

    # Where is the vacuum?
    def get_vacuum_location(self):
        return self.vacuum_loc

    # Where are the dirty locations?
    def get_dirt_locations(self):
        return self.dirty_locations

    def is_vacuum_at_dirty_location(self):
        for i in range(len(self.dirty_locations)):
            if utils.same_location(self.vacuum_loc, self.dirty_locations[i]):
                return True
        return False
 
    #
    # Methods
    #
    # These are the functions that are used to update and report on
    # world information.

    # Has the game come to an end?
    def isEnded(self):
        if self.status == State.FINISHED:  
            print("Done!")
            return True
        return False
            
    #------------        
            
    # Implements the move 
    def update_vacuum(self, action):
        print("Executing action: ", action.name)
        
        if action == Actions.MOVE_LEFT:
            if self.vacuum_loc.x > 0:
                self.vacuum_loc.x = self.vacuum_loc.x - 1
                
        elif action == Actions.MOVE_RIGHT:
            if self.vacuum_loc.x < self.maxx:
                self.vacuum_loc.x = self.vacuum_loc.x + 1
                
        elif action == Actions.CLEAN: 
            index = -1
            for i in range(len(self.dirty_locations)):
                if utils.same_location(self.vacuum_loc, self.dirty_locations[i]):
                    self.dirty_locations.pop(i)
                    break

        elif action == Actions.STOP:            
            self.status = State.FINISHED
        else: # noops
            pass
            
            
        

        
            
