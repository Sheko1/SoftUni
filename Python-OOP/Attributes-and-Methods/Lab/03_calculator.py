class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(first_num, *args):
        result = first_num
        for num in args:
            result *= num

        return result

    @staticmethod
    def divide(first_num, *args):
        result = first_num
        for num in args:
            result /= num

        return result

    @staticmethod
    def subtract(first_num, *args):
        result = first_num
        for num in args:
            result -= num

        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
