from .hardware import Hardware


class PowerHardware(Hardware):
    CAPACITY_DECREASE = 0.25
    MEMORY_INCREASE = 0.75

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, type="Power", capacity=int(capacity * self.CAPACITY_DECREASE)
                         , memory=int(memory + (memory * self.MEMORY_INCREASE)))
