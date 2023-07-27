# 1. Parking lot system
# 2. Entry and exit terminals
# 3. Parking spot
# 4. Ticket
# 5. Monitoring sysytem
from abc import ABC, abstractmethod
import time


class ParkingSpotType(ABC):
    def __init__(self, vehicle_id, reserved):
        self.reserved = reserved

    @abstractmethod
    def get_spot_id(self):
        # code for getting available spot id and choosing minimum of that
        pass


class motorbike(ParkingSpotType):
    def get_parking_details(self):
        return {'parked_at_id', 'issue_time'}





class ParkingTicket:
    def __init__(self, parking_id, parking_spot_type, issue_time):
        self.parking_id = parking_id
        self.parking_spot_type = parking_spot_type
        self.issue_time = issue_time

class Payment:
    @staticmethod
    def calculate_amount(issuetime, hourly_rate):
        return  (time.time() - issuetime) * hourly_rate

class Terminal(ParkingTicket):
    def get_ticket():
        print('T231')

    @staticmethod
    def accept_ticket():


vehicle = motorbike(vehicle_id = '123', reserved='no')





