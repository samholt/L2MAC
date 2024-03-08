import sys
import difflib

from summarizer_and_modifier import remove_line_numbers

s1 = """
from parking_spot import MotorcycleSpot, CompactSpot, LargeSpot
from vehicle import Vehicle, VehicleSize

class Level:
    def __init__(self, spots):
        self.available_spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}

    def park_vehicle(self, vehicle):
        if isinstance(vehicle, Motorcycle):
            if self.available_spots[MotorcycleSpot] > 0:
                self.available_spots[MotorcycleSpot] -= 1
                return True
        elif isinstance(vehicle, Car):
        self.spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}
            if self.available_spots[CompactSpot] > 0:
                self.available_spots[CompactSpot] -= 1
                return True
        elif isinstance(vehicle, Bus):
            if self.available_spots[LargeSpot] >= 5:
                self.available_spots[LargeSpot] -= 5
                return True
        return False

    def remove_vehicle(self, vehicle):
        if isinstance(vehicle, Motorcycle):
            self.available_spots[MotorcycleSpot] += 1
            return True
        elif isinstance(vehicle, Car):
            self.available_spots[CompactSpot] += 1
            return True
        elif isinstance(vehicle, Bus):
            self.available_spots[LargeSpot] += 5
            return True
        return False
"""

s2 = """
from vehicle import Motorcycle, Car, Bus

class Level:
    def __init__(self, spots):
        self.spots = spots
        self.available_spots = {k: v for k, v in spots.items()}

    def park_vehicle(self, vehicle):
        if isinstance(vehicle, Motorcycle):
            if self.available_spots['MotorcycleSpot'] > 0:
                self.available_spots['MotorcycleSpot'] -= 1
                return True
            elif self.available_spots['CompactSpot'] > 0:
                self.available_spots['CompactSpot'] -= 1
                return True
            elif self.available_spots['LargeSpot'] > 0:
                self.available_spots['LargeSpot'] -= 1
                return True
        elif isinstance(vehicle, Car):
            if self.available_spots['CompactSpot'] > 0:
                self.available_spots['CompactSpot'] -= 1
                return True
            elif self.available_spots['LargeSpot'] > 0:
                self.available_spots['LargeSpot'] -= 1
                return True
        elif isinstance(vehicle, Bus):
            if self.available_spots['LargeSpot'] >= 5:
                self.available_spots['LargeSpot'] -= 5
                return True
        return False

    def remove_vehicle(self, vehicle):
        if isinstance(vehicle, Motorcycle):
            if self.spots['MotorcycleSpot'] > self.available_spots['MotorcycleSpot']:
                self.available_spots['MotorcycleSpot'] += 1
                return True
            elif self.spots['CompactSpot'] > self.available_spots['CompactSpot']:
                self.available_spots['CompactSpot'] += 1
                return True
            elif self.spots['LargeSpot'] > self.available_spots['LargeSpot']:
                self.available_spots['LargeSpot'] += 1
                return True
        elif isinstance(vehicle, Car):
            if self.spots['CompactSpot'] > self.available_spots['CompactSpot']:
                self.available_spots['CompactSpot'] += 1
                return True
            elif self.spots['LargeSpot'] > self.available_spots['LargeSpot']:
                self.available_spots['LargeSpot'] += 1
                return True
        elif isinstance(vehicle, Bus):
            if self.spots['LargeSpot'] - 5 >= self.available_spots['LargeSpot']:
                self.available_spots['LargeSpot'] += 5
                return True
        return False
"""

print(''.join(list(difflib.context_diff(s1, s2, fromfile='before.py', tofile='after.py'))))

print('')