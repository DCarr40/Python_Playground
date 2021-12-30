def test():
    
    is_it_hot = False
   
    is_it_cold = False

    name = input("Good morning! What's your name?")

    if is_it_hot:
        print(f"It's hot outside {name}")

    elif is_it_cold:
        print(f"It's cold outside {name}")

    else:
        print(f"It's warm outside {name}")
    
 
test()

#test comment

# """
# multiline
# """

my_name = "David C."
print(f"Hello {my_name}")

# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = "pizza"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner
meal = "chocolate cake"
# Printing out dinner
print("Dinner:")
print(meal)
