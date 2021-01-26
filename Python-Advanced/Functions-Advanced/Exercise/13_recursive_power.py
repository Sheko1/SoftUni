def recursive_power(number, power, n=0, result=1):
    if n == power:
        return result

    return recursive_power(number, power, n+1, result*number)
