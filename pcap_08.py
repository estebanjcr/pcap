# Caesar cipher v2

text = input("Enter your message: ")
try:
    shift_val = int(input("Enter shift value (1 - 25): "))
except:
    print("Incorrect value entered.")
    
cipher = ''

for char in text:
    if not char.isalpha():
        # non alpha untouched
        cipher += char
    if ord(char) in range(65, 91):
        # upper case
        code = ord(char) + shift_val
        if code > ord('Z'):
            code = (code - ord('Z')) + ord('A') - 1
            cipher += chr(code)
        else:
            cipher += chr(code)
    elif ord(char) in range(97, 123):
        # lower case
        code = ord(char) + shift_val
        if code > ord('z'):
            code = (code - ord('z')) + ord('a') - 1
            cipher += chr(code)
        else:
            cipher += chr(code)

print(cipher)