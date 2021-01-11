str_1 = input()
str_2 = input()

string = ""
last_string = str_1

for i in range(len(str_1)):
    for index_str2 in range(0, i+1):
        string += str_2[index_str2]

    for index_str1 in range(i + 1, len(str_1)):
        string += str_1[index_str1]

    if last_string != string:
        print(string)
    last_string = string
    string = ""
