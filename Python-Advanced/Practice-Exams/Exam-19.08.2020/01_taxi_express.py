from collections import deque

customers = deque([int(num) for num in input().split(", ")])
taxis = [int(num) for num in input().split(", ")]

time_passed = 0

while customers and taxis:
    curr_customer = customers[0]
    curr_taxi = taxis.pop()

    if curr_taxi >= curr_customer:
        time_passed += curr_customer
        customers.popleft()


if not customers:
    print(f"All customers were driven to their destinations\nTotal time: {time_passed} minutes")

else:
    print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join(str(x) for x in customers)}")
