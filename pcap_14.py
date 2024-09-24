# Raise Exceptions

def read_int(prompt, min, max):
    valid_value = False
    while not valid_value:
        user_input = input(prompt)
        try:
            if not user_input.isdigit():
                raise AssertionError
            num = int(user_input)
            if num < min or num > max:
                raise ValueError
            else:
                valid_value = True
                return num
        except AssertionError:
            print("Error: wrong input")
        except ValueError:
            print("Error: the value is not within permitted range ({}..{})".format(min, max))

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)