from abc import ABC

from car import Car


class CapuletEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = int
        self.last_service_mileage = int
        

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000
    
    def needs_service(self):
        return super().needs_service()