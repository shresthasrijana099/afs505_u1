from sys import argv

script, filename = argv
# opens the file that you enter
txt = open(filename)
# replace filename with the name you enter and print
print(f"Here's your file {filename}: ")
# reads the opened file and then prints the content
print(txt.read())
# asks you to enter the filename again
