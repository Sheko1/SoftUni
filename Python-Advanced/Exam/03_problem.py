def stock_availability(stocks, command, *args):
    if command == "delivery":
        [stocks.append(stock) for stock in args]

    elif command == "sell":
        if not args:
            stocks = stocks[1:]

        elif type(args[0]) == int:
            stocks = stocks[args[0]:]

        else:
            for item in args:
                if item in stocks:
                    stocks = [stock for stock in stocks if item != stock]

    return stocks


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
