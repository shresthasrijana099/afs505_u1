#categories
types_of_people = 10
#in a particular place
x = f"There are {types_of_people} types of people."
#variables
binary = "binary"
do_not = "don't"
#formatting or replacing the values
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#another way of formatting
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

#adding two pieces of statements
print(w + e)
