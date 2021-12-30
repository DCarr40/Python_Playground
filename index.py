# These are code academy practice problems

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

# Define the release and runtime integer variables below:
release_year = 2021
runtime = 230



# Define the rating_out_of_10 float variable below: 
rating_out_of_10 = 9.0

#simple computation
print(25*68+13/28)

#quilt squares
quilt_width = 8
quilt_length = 8

first_quilt = quilt_length * quilt_width

print(first_quilt)

# Calculation of squares for:
# 6x6 quilt

# 7x7 quilt

# 8x8 quilt

# How many squares for 6 people to have 6 quilts each that are 6x6?

print(6**6)
print(7**2)
print(8**2)
print(6**4)

#modulo operations
my_team = 27%4
print(my_team)

#Concatenation
string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:

message = f"{string1 }{string2 }{string3 }{string4 }{string5 }{string6 }"


print(message)

#Plus Equal Practice

total_price = 0

new_sneakers = 50.00

nice_sweater = 39.00
fun_books = 20.00

total_price += new_sneakers + nice_sweater + fun_books


# Update total_price here:

print("The total price is", total_price)

# Assign the string here
to_you = """Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?"""


print(to_you)

#Review

my_age = 32
half_my_age = my_age / 2
greeting = "Hello, "
name = "David"
greeting_with_name =  f"{greeting}{name}"
print(half_my_age)
print(greeting_with_name)

#David Carruthers
#tacos


first_letter ="""
DDDD 
D    D
D    D
D    D
D    D
D    D
DDDD 
"""

second_letter ="""
 CCC 
C    C
C    
C    
C    
C    C
 CCC 
"""

print(f"{first_letter}{second_letter}")