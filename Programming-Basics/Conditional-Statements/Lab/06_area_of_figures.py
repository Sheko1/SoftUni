ahmet = str(input())
from math import pi

if ahmet == str("square"):
    s = float(input())
    s1 = s * s
    print(f"{s1:.3f}")

elif ahmet == str("rectangle"):
    a = float(input())
    b = float(input())
    s = a * b
    print(f"{s:.3f}")

elif ahmet == str("circle"):
    r = float(input())
    s = pi * r * r
    print(f"{s:.3f}")

elif ahmet == str("triangle"):
    a = float(input())
    h = float(input())
    s = a * h / 2
    print(f"{s:.3f}")
