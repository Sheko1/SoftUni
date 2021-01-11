number = float(input())
input_unit = str(input())
output_unit = str(input())

if input_unit == "mm" and output_unit == "cm":
    cm = number / 10
    print(f"{cm:.3f}")

elif input_unit == "cm" and output_unit == "mm":
    mm = number * 10
    print(f"{mm:.3f}")

elif input_unit == "mm" and output_unit == "m":
    m = number / 1000
    print(f"{m:.3f}")

elif input_unit == "m" and output_unit == "mm":
    mm = number * 1000
    print(f"{mm:.3f}")

elif input_unit == "cm" and output_unit == "m":
    m = number / 100
    print(f"{m:.3f}")

elif input_unit == "m" and output_unit == "cm":
    cm = number * 100
    print(f"{cm:.3f}")
