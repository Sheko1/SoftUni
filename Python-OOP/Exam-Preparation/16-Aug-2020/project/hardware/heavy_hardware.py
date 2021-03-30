from .hardware import Hardware


class HeavyHardware(Hardware):
    CAPACITY_INCREASE = 2
    MEMORY_DECREASE = 0.75

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Heavy", capacity*self.CAPACITY_INCREASE, int(memory*self.MEMORY_DECREASE))
