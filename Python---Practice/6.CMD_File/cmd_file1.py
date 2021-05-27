from sys import argv

script, filename= argv
print(f"Opened Script:{filename}")
txt= open(filename) #open file
print(f"Opened File:{filename}")
print(txt.read()) #read from text file
txt.close()         #close text file
print(f"Closed File:{filename}")
