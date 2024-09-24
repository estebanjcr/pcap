# Palindrome

user_input = input("Palindrome checker. Enter sentence to verify: ")

if user_input.strip() == "":
    print("It's not a palindrome")
    
input_letters = ""
for letter in user_input.lower():
    if not letter.isalpha():
        continue
    else:
        input_letters = input_letters + letter

length = len(input_letters)

if length % 2 == 0:
    # even number of letters
    first_half = input_letters[:int(length / 2)]
    second_half = input_letters[int(length / 2):]
    second_half = second_half[::-1]

elif length % 2 != 0:
    # odd number of letters
    length = length - 1
    first_half = input_letters[:int(length / 2)]
    second_half = input_letters[int(length / 2) + 1:]
    second_half = second_half[::-1]


if first_half == second_half:
    print("It's a palindrome")
else:
    print("It's not a palindrome")