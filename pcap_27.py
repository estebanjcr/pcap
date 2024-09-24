# Evaluating student's results

class StudentsDataException(Exception):
    def __init__(self):
    	Exception.__init__(self)

class BadLine(StudentsDataException):
    def __init__(self):
    	StudentsDataException.__init__(self)

class FileEmpty(StudentsDataException):
    def __init__(self):
        StudentsDataException.__init__(self)

try:
    file = input('Enter file path: ')
    f = open(file, 'rt')
    if len(f.read()) == 0:
    	raise FileEmpty
    	
    grades = {}
    for line in open(file, 'rt'):
    	line = line.split()
    	if type(line[0]) and type(line[1]) is not str:
    	    raise BadLine
    	if type(float(line[2])) is not float:
    		raise BadLine
    	
    	name = line[0] + ' ' + line[1]
    	grade = float(line[2])
    	if name not in grades.keys():
    		grades[name] = grade
    	else:
    		grades[name] += grade

    for k in sorted(grades.keys()):
    	print(k, grades[k])


except FileNotFoundError:
    print('Exception. File does not exist.')
except FileEmpty:
    print('Exception. File is empty.')
except BadLine:
    print('Exception. Bad line in file.')
