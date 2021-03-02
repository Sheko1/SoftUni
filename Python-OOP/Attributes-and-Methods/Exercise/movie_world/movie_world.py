from .customer import Customer
from .dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += str(customer) + "\n"

        for dvd in self.dvds:
            result += str(dvd) + "\n"

        return result

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    @staticmethod
    def get_customer_and_dvd_by_id(customer_id, dvd_id, customers, dvds):
        return [c for c in customers if c.id == customer_id][0], [d for d in dvds if d.id == dvd_id][0]

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer, dvd = self.get_customer_and_dvd_by_id(customer_id, dvd_id, self.customers, self.dvds)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        elif dvd.is_rented:
            return "DVD is already rented"

        elif customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer, dvd = self.get_customer_and_dvd_by_id(customer_id, dvd_id, self.customers, self.dvds)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False

        return f"{customer.name} has successfully returned {dvd.name}"
