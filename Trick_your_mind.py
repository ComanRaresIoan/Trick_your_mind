# Ask the user for a number
a = int(input("Enter your number: "))

# Double the number
print("I will double that number for you: ")
input("Press Enter to continue...")  # Wait for user input

b = a + a

# Remind the user to remember the result
print("Keep in mind the result!")
input("Press Enter to continue...")

# Ask the user to ask somebody else for a number
print("Somebody at your choice will give you an additional number. Ask them.")
somebody_else_number = int(input("Ask a person to give a number to you: "))
c = b + somebody_else_number

# We will half the total number
print("The thief will steal half of it.")
input("Press Enter to continue...")
d = c / 2 # c = 30, d = 15

# You ask the user to give your part back
print("You give me back my part. (initial number)")
input("Press Enter to continue...")
e = d - a # d = 15, e = 10

# We say to the user what is the
print("And you will remain with ", e, "!")

# The whole point of the game is to trick the user's mind
# But in reality, the final result 'e' is half of the 'somebody_else_number'
