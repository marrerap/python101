# ask for name
name = input("What is your name? ")

# greet user
print(f"Good day, {name}")

# check if name is longer than 10
if len(name) > 10:
    # if it is say "wow long name"
    print("match 10")

# elif name is greater than 5
elif len(name) > 5:
    print("match 5")
# if nothing matches print this value
else:
    print("Wow, you have a boring name")