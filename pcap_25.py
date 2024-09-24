# Character frequency histogram

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
    
    for k in sorted(dict.keys()):
    	print(k, '->', dict[k])
    
except IOError as e:
    print('I/O Error: ', strerror(e.errno))