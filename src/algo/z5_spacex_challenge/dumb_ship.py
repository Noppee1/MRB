from src.algo.z5_spacex_challenge.model import *
from my_helpers.velo_control import *

# veloship jest ship-em
class DumbShip(Ship):

    def initialize(self, state: ShipState):
        pass

    def get_thrust_vectors(self, time: float, state: ShipState, debug=False) -> ThrustVectors:
        h = state.height
        v = state.speed
        maxT = state.max_thrust

        if h > 12:
            thrus = 0
        if h > 6:
            thrus = state.max_thrust * 0.9
        else:
            thrus = 10
        return ThrustVectors(a_vertical=thrus)




        return ThrustVectors(a_vertical=thrust)


