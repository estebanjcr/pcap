# Sorted character frequency histogram

from os import strerror

file = input("Enter file path: ")

try:
    f = open(file, 'rt')
    content = f.read()
    dict = {}
    for char in content:
    	if not char.lower().isalpha():
    		pass
    	else:	
    	    if char not in dict:
    		    dict[char] = 1
    	    else:
    		    dict[char] += 1
    		    
    # sorted() takes a <key> parameter to specify a function
    # to be called on each list element prior to making comparisons
    vsorted_dict = {k:v for k, v in sorted(dict.items(), key=lambda dict: dict[1], reverse=True)}
    
    for k in vsorted_dict:
    	print(k, '->', vsorted_dict[k])
    
except IOError as e:
    print('I/O Error: ', strerror(e.errno))