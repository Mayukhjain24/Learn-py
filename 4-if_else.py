# age = 12

# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You're not eligible to vote")

# if else-if else

age = int (input("Enter your age:"))

if age >= 18 and age < 60:
    print("You are eligible to vote")
elif age >= 60:
    print("You're too aged to vote")
else:
    print("You're not eligible to vote")