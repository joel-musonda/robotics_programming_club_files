#In this session we created a code that checks if a user is eligible for a diver's licence

age = int(input("What is your age? "))

if age >= 16:
     print("You are eligible for a driver's licence.")
else:
     print("You are not eligible for a driver's licence yet.")


#You could also have a nested if statement to check for other conditions, such as if the user has passed a driving test.
  
age = int(input("What is your age? "))
has_passed_test = input("Have you passed the driving test? (yes/no) ")

if age >= 16:
    if has_passed_test == "yes":
        print("You are eligible for a driver's licence.")
    else:
        print("You need to pass the driving test first.")
else:
    print("You are not eligible for a driver's licence yet.")

# you can also have elif statements to check for multiple conditions. For example, you could check if the user is eligible for a learner's permit if they are between 15 and 16 years old.

name = str(input("What is your name? "))
if "a" in name:
    print("Your name contains the letter 'a'.")
elif "e" in name:
    print("Your name contains the letter 'e'.")
else:
    print