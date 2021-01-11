def data_converter(data_type, data):
    if data_type == "int":
        return int(data) * 2

    elif data_type == "real":
        return f"{float(data) * 1.5:.2f}"

    elif data_type == "string":
        return "$" + data + "$"


type_data = input()
value = input()

print(data_converter(type_data, value))