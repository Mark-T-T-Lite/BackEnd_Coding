
x = int(input("number of files\n>"))
for i in range(x):
    fileObj = open(f"input{i}.in",'w')
    fileObj.close()
