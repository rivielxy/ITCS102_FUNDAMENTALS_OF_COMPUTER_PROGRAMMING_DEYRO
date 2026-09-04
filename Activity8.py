# STRING ASSIGNMENT OPERATOR

hobbies = ""

a = input("What are your hobbies? (One at a time) ")
hobbies += a + ", "

b = input("What else? ")
hobbies += b + ", "

c = input("Anything else? ")
hobbies += c + "."

print("Your hobbies are: {", hobbies, "}")
