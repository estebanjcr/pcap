def mysplit(strng):
    if strng.strip() == "":
        return []
    else:
        list1 = []
        word1 = ""
        strng = strng + " "
        for char in strng:
            if char != " ":
                word1 = word1 + char
            else:
                if word1 != "":
                    list1.append(word1)
                    word1 = ""
        
        return list1


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))