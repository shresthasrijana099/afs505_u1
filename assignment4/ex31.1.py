print("""I have a gift for you in these two bags, little kid.
From which bag do you want? red or blue?""")

bag = input("> ")

if bag == "red":
    print("Again I have two boxes: big one and small one.")
    print("Which one do you want?")

    box = input("> ")

    if box == "big":
        print("Oops! It's only a lollipop. You can have it.")
    elif box == "small":
        print("Wow! lots of stuff. Chocolates, cookies and toys. You better share with your sister.")
    else:
        print("I don't have that. You got nothing.")

elif bag == "blue":
    print("Again I have two boxes: big one and small one.")
    print("Which one do you want?")

    box = input("> ")

    if box == "big":
        print("Oh my God! That's a lot of books. Now, you got to read all of these.")
    elif box == "small":
        print("Is it a laptop? Oh yes, it is.")
    else:
        print("I don't have that. You got nothing.")

else:
    print("Sorry, next time.")
