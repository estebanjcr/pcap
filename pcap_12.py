# Finder
 
input1 = input("Enter word to find: ").lower()
input2 = input("Enter word to be scanned: ").lower()
 
input1_list = []
for letter in input1:
    input1_list.append(letter)
 
input2_list = []
for letter in input2:
    input2_list.append(letter)
 
compare_list = input1_list[:]
for letter in input1_list:
    if letter in input2_list:
        compare_list.remove(letter)
        index = input2_list.index(letter)
        input2_list = input2_list[index + 1:]
 
if compare_list == []:
    print("Yes")
else:
    print("No")
 
# Can be solved with POS() function, may be a good idea to refactor with it
# Sample input: donor, NAbucodonosor