from level import Level

class ParkingLotSystem:
    def __init__(self, total_levels: int, spots_per_level: int):
        self.total_levels = total_levels
        self.levels = [Level(i, spots_per_level) for i in range(total_levels)]

    def park(self, vehicle):
        for level in self.levels:
            if not level.is_full():
                level.park(vehicle):
                return
        raise Exception('Parking lot is full')