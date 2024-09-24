# Anagrams

input1 = input("Anagram checker. Enter word 1: ")
input2 = input("Enter word 2: ")

if input1.strip() == "" and input2.strip() == "":
    print("Not anagrams.")

input1_letters = []
for letter in input1.lower():
    if not letter.isalpha():
        continue
    else:
        input1_letters.append(letter)

input2_letters = []
for letter in input2.lower():
    if not letter.isalpha():
        continue
    else:
        input2_letters.append(letter)

no_pair_letters = input1_letters[:]
for letter in input1_letters:
    if letter in input2_letters:
        no_pair_letters.remove(letter)
    else:
        continue

if no_pair_letters == []:
    print("Anagrams")
else:
    print("Not anagrams")