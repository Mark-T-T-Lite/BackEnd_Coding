from sys import argv

script, fileDir = argv

def print_all(f):
    print(f.read())

def moveFilePointer(f,position):
    f.seek(position)

def print_line(linecount,f):
    print(linecount,f.readline())
    

#Create file object
fileObject= open(fileDir)

#to print all file contents
print_all(fileObject)

#move position to beginning of file
moveFilePointer(fileObject,0)

#print one line
print_line(1,fileObject)
