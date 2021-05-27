from sys import argv
from os.path import exists

script, source_file, target_file = argv

inFile = open(source_file, 'r')
inFile_data = inFile.read()

print(f"The source file: {source_file} is {len(inFile_data)} bytes long")

print(f"Does the output file exist? {exists(target_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")

print(f"Copying from {source_file} to {target_file} ")

outFile= open(target_file, 'w')
outFile.write(inFile_data)

print("Copied Successfully")

inFile.close()
outFile.close()
