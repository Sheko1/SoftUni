import re
n = int(input())

pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"


for _ in range(n):
    product = input()

    match = re.findall(pattern, product)

    if len(match) == 0:
        print("Invalid barcode")

    else:
        result = ""
        
        for char in match[0]:
            if char.isdigit():
                result += char
                
        if not result:
            result = '00'

        print(f"Product group: {result}")
