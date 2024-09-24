# Digit of Life

user_input = input("Enter your birthdate in the format YYYYMMDD: ")

total_sum = 0

for char in user_input:
    total_sum += int(char)

if total_sum > 9:
    string_total = str(total_sum)
    total_sum = 0
    for char in string_total:
        total_sum += int(char)

print("The digit of life for {} is {}".format(user_input, total_sum))