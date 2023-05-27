from abc import ABC, abstractmethod
from battery import Battery
from engine import Engine

class Car(ABC):
    def __init__(self, engine, battery):
        # self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery


    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
        # pass
