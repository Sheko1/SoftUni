from math import floor
income = float(input())
average_success = float(input())
minimum_salary = float(input())

scholarship1 = minimum_salary * 0.35
scholarship2 = average_success * 25

if income < minimum_salary and average_success >= 5.5:
    if scholarship1 <= scholarship2:
        print(f"You get a scholarship for excellent results {floor(scholarship2)} BGN")
    else:
        print(f"You get a Social scholarship {floor(scholarship1)} BGN")


elif income < minimum_salary and average_success > 4.5:
    print(f"You get a Social scholarship {floor(scholarship1)} BGN")

elif average_success >= 5.5:
    print(f"You get a scholarship for excellent results {floor(scholarship2)} BGN")

else:
    print("You cannot get a scholarship!")
