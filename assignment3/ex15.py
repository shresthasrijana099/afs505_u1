from sys import argv

script, filename = argv
# opens the file that you enter
txt = open(filename)
# replace filename with the name you enter and print
print(f"Here's your file {filename}: ")
# reads the opened file and then prints the content
print(txt.read())
# asks you to enter the filename again
print("Type the filename again:")
# the name of file you entered is saved as file_again
file_again = input(">")
# opens up the file you just entered and the content is saved as txt_again
txt_again = open(file_again)
# reads the opened file and prints
print(txt_again.read())
