import world
import random
import utils
from utils import Actions
from utils import Location
from utils import LocState

class Vacuum():
    def __init__(self, world):
        self.world = world
        self.moves = [Actions.MOVE_LEFT, Actions.MOVE_RIGHT, Actions.CLEAN]
        self.action_table = [
            [ [{Location.LEFT : LocState.CLEAR}],                                                                     Actions.MOVE_RIGHT ],
            [ [{Location.LEFT : LocState.DIRTY}],                                                                     Actions.CLEAN      ],
            [ [{Location.RIGHT: LocState.CLEAR}],                                                                     Actions.MOVE_LEFT  ],
            [ [{Location.RIGHT: LocState.DIRTY}],                                                                     Actions.CLEAN      ],
            [ [{Location.LEFT : LocState.DIRTY}, {Location.LEFT : LocState.CLEAR}],                                   Actions.MOVE_RIGHT ],
            [ [{Location.LEFT : LocState.CLEAR}, {Location.RIGHT: LocState.DIRTY}],                                   Actions.CLEAN      ],
            [ [{Location.RIGHT: LocState.CLEAR}, {Location.LEFT : LocState.DIRTY}],                                   Actions.CLEAN      ],
            [ [{Location.RIGHT: LocState.DIRTY}, {Location.RIGHT: LocState.CLEAR}],                                   Actions.MOVE_LEFT  ], 
            [ [{Location.LEFT : LocState.DIRTY}, {Location.LEFT : LocState.CLEAR}, {Location.RIGHT: LocState.DIRTY}], Actions.CLEAN      ],
            [ [{Location.RIGHT: LocState.DIRTY}, {Location.RIGHT: LocState.CLEAR}, {Location.LEFT : LocState.DIRTY}], Actions.CLEAN      ],     
            [ [{Location.LEFT : LocState.DIRTY}, {Location.LEFT : LocState.CLEAR}, {Location.RIGHT: LocState.DIRTY}, {Location.RIGHT: LocState.CLEAR}], Actions.STOP ],
            [ [{Location.RIGHT: LocState.DIRTY}, {Location.RIGHT: LocState.CLEAR}, {Location.LEFT : LocState.DIRTY}, {Location.LEFT : LocState.CLEAR}], Actions.STOP ],
            [ [{Location.LEFT : LocState.DIRTY}, {Location.LEFT : LocState.CLEAR}, {Location.RIGHT: LocState.CLEAR}], Actions.STOP ],
            [ [{Location.LEFT : LocState.CLEAR}, {Location.RIGHT: LocState.DIRTY}, {Location.RIGHT: LocState.CLEAR}], Actions.STOP ],
            [ [{Location.RIGHT: LocState.CLEAR}, {Location.LEFT : LocState.DIRTY}, {Location.LEFT : LocState.CLEAR}], Actions.STOP ],
            [ [{Location.RIGHT: LocState.DIRTY}, {Location.RIGHT: LocState.CLEAR}, {Location.LEFT : LocState.CLEAR}], Actions.STOP ],                                  
            [ [{Location.RIGHT: LocState.CLEAR}, {Location.LEFT : LocState.CLEAR}], Actions.STOP ],
            [ [{Location.RIGHT: LocState.CLEAR}, {Location.LEFT : LocState.CLEAR}], Actions.STOP ]                             
           ] 
        
        self.percepts = []
        self.state = { Location.LEFT : -1,  Location.RIGHT : -1 }
        self.vacuum_location = Location(self.world.get_vacuum_location().x)

    def make_move(self):
        return self.model_based_agent()
    
    def update_state(self):
        perceived_state = self.perceive_state()
        self.vacuum_location = list(perceived_state.keys())[0] 
        self.state[ self.vacuum_location ] = perceived_state[self.vacuum_location]
        
    def model_based_agent(self):
        self.update_state()
        if (self.state[ Location.LEFT ] == LocState.CLEAR and self.state[ Location.RIGHT ] == LocState.CLEAR):
            return Actions.STOP
        elif (self.vacuum_location == Location.LEFT and self.state[ Location.LEFT ] == LocState.DIRTY) or \
                (self.vacuum_location == Location.RIGHT and self.state[ Location.RIGHT ] == LocState.DIRTY):
            return Actions.CLEAN
        elif self.vacuum_location == Location.LEFT:
            return Actions.MOVE_RIGHT
        elif self.vacuum_location == Location.RIGHT:
            return Actions.MOVE_LEFT
        else:
            return Actions.NOOPS