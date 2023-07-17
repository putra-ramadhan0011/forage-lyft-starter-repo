from engine import Engine


from abc import ABC

from car import Car


class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = bool

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
    
    def needs_service(self):
         return super().needs_service()