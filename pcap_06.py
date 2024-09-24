
led_nums = [["###", "# #", "# #", "# #", "###"],
["  #", "  #", "  #", "  #", "  #"],
["###", "  #", "###", "#  ", "###"],
["###", "  #", "###", "  #", "###"],
["# #", "# #", "###", "  #", "  #"],
["###", "#  ", "###", "  #", "###"],
["###", "#  ", "###", "# #", "###"],
["###", "  #", "  #", "  #", "  #"],
["###", "# #", "###", "# #", "###"],
["###", "# #", "###", "  #", "###"]]



def led():
    strng = input("Enter an interger: ")
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""
    try:
        for char in strng:
            line1 = line1 + led_nums[int(char)][0] + " "
            line2 = line2 + led_nums[int(char)][1] + " "
            line3 = line3 + led_nums[int(char)][2] + " "
            line4 = line4 + led_nums[int(char)][3] + " "
            line5 = line5 + led_nums[int(char)][4] + " "
    except ValueError:
        print("You did not enter an integer.")
        
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)


led()