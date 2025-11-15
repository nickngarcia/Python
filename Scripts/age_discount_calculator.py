# Get user's age

user_age = int(input("Enter your age: "))

# Determine discount 

if user_age <= 10:
    discount_percent = 100
elif user_age >= 60:
    discount_percent = 20
else:
    discount_percent = 0

    #Output the discount percentage
print(f"Your discount is {discount_percent}%")
# End of code