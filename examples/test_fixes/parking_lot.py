from typing import List
from level import Level
from vehicle import Vehicle

class ParkingLot:
    def __init__(self, levels: List[Level]):
        self.levels = levels

    def park_vehicle(self, vehicle: Vehicle):
        for level in self.levels:
        if level.is_spot_available() and level.park_vehicle(vehicle):
            return True
        return False

    def unpark_vehicle(self, spot_id: str, level_id: int):
        for level in self.levels:
            if level.level_id == level_id:
                return level.unpark_vehicle(spot_id)
        return False

    def get_status(self):
        status = []
        for level in self.levels:
            status.append(level.get_status())
        return status
