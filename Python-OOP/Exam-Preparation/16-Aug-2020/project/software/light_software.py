from .software import Software


class LightSoftware(Software):
    CAPACITY_INCREASE = 0.5
    MEMORY_DECREASE = 0.5

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, type="Light", capacity_consumption=int(
            capacity_consumption + (capacity_consumption * self.CAPACITY_INCREASE)),
                         memory_consumption=int(memory_consumption * self.MEMORY_DECREASE))
