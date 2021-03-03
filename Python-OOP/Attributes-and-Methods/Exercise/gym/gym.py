from .customer import Customer
from .trainer import Trainer
from .equipment import Equipment
from .exercise_plan import ExercisePlan
from .subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        sub = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer = [c for c in self.customers if c.id == sub.customer_id][0]
        trainer = [t for t in self.trainers if t.id == sub.trainer_id][0]
        plan = [p for p in self.plans if p.id == trainer.trainer_id][0]
        equipment = [e for e in self.equipment if e.id == plan.equipment_id][0]

        return f"{repr(sub)}\n{repr(customer)}\n{repr(trainer)}\n{repr(equipment)}\n{repr(plan)}"
