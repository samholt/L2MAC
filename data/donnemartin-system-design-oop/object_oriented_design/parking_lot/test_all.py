import pytest
from vehicle import Motorcycle, Car, Bus, VehicleSize
from level import Level
from parking_lot import ParkingLot
from parking_spot import MotorcycleSpot, CompactSpot, LargeSpot

def test_motorcycle_parking():
    level = Level({'MotorcycleSpot': 10, 'CompactSpot': 10, 'LargeSpot': 10})
    m = Motorcycle('M1')
    assert level.park_vehicle(m) == True
    assert level.available_spots['MotorcycleSpot'] == 9

def test_car_parking():
    level = Level({'MotorcycleSpot': 10, 'CompactSpot': 10, 'LargeSpot': 10})
    c = Car('C1')
    assert level.park_vehicle(c) == True
    assert level.available_spots['CompactSpot'] == 9

def test_bus_parking():
    level = Level({'MotorcycleSpot': 10, 'CompactSpot': 10, 'LargeSpot': 10})
    b = Bus('B1')
    assert level.park_vehicle(b) == True # This might fail due to the 5 consecutive spot rule
    assert level.available_spots['LargeSpot'] == 5

def test_vehicle_removal():
    level = Level({'MotorcycleSpot': 10, 'CompactSpot': 10, 'LargeSpot': 10})
    m = Motorcycle('M1')
    c = Car('C1')
    level.park_vehicle(m)
    level.park_vehicle(c)
    assert level.remove_vehicle(m) == True
    assert level.available_spots['MotorcycleSpot'] == 10
    assert level.remove_vehicle(c) == True
    assert level.available_spots['CompactSpot'] == 10

def test_parking_lot():
    parking_lot = ParkingLot(3, {'MotorcycleSpot': 10, 'CompactSpot': 10, 'LargeSpot': 10})
    m = Motorcycle('M1')
    c = Car('C1')
    b = Bus('B1')
    assert parking_lot.park_vehicle(m) == True
    assert parking_lot.park_vehicle(c) == True
    assert parking_lot.park_vehicle(b) == True # This might fail due to the 5 consecutive spot rule
    assert parking_lot.remove_vehicle(m) == True
    assert parking_lot.remove_vehicle(c) == True

@pytest.mark.parametrize("spot_type, vehicle, result", [
    (MotorcycleSpot('1', 1), Motorcycle('M1'), True),
    (CompactSpot('2', 1), Motorcycle('M1'), True),
    (CompactSpot('2', 1), Car('C1'), True),
    (LargeSpot('3', 1), Motorcycle('M1'), True),
    (LargeSpot('3', 1), Car('C1'), True),
    (MotorcycleSpot('1', 1), Car('C1'), False),
])
def test_spot_parking(spot_type, vehicle, result):
    assert spot_type.park(vehicle) == result


if __name__ == "__main__":
    pytest.main([__file__])