from project.medicine.medicine import Medicine


class Painkiller(Medicine):
    HEALTH_INCREASE = 20

    def __init__(self):
        super().__init__(health_increase=self.HEALTH_INCREASE)
