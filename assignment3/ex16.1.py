from sys import argv

script, filename = argv

print("Let's open a file.")
file = open(filename)
print(file.read())
file2 = open(filename, 'w')

file2.truncate()

print("Let's add few lines to the document.")
line1 = input("line 1: ")
line2 = input("line 2: ")
file.write(line1)
file.write("\n")
