"""SKILLS: FUNCTIONS

Please complete the following promps.
"""

#################### PART 1 ####################

"""PROMPT 1

Write a function that returns `True` if a town name matches the name of your
hometown.

Examples: (let's say my hometown is San Francisco)
    - 'Oakland' -> False
    - 'San Francisco' -> True

Arguments:
    - The name of a town (str)

Return:
    - True or False (bool)
"""

# Write your function here
hometown = "San Francisco"
your_hometown = input("What's the name of your hometown?>")
print()#adding space

def matching_hometowns(hometown):
    """Checks if your hometown matches the given hometown."""

    if your_hometown == hometown: #check if both match
        return True

    else:
        return False

print(matching_hometowns(hometown))#call the function
print()#adding space

"""PROMPT 2

Write a function that takes in a first and last name and returns a full name.

Examples:
    - 'Brighticorn', 'Hackbright' -> 'Brighticorn Hackbright'

Arguments:
    - First name (str)
    - Last name (str)

Return:
    - Full name (str)
"""

# Write your function here
first = input("What is your first name?>")#ask for first name
last = input("What is your last name?>")#ask for last name
print()#adding space

def full_name(first,last): 
    """Prints out the full name from the given first and last name."""

    return f"{first} {last}"#return full name

print(full_name(first,last))

print()#adding space
"""PROMPT 3

Write a function that prints a greeting.

If the person is from your hometown, print
    Hi <full name>, we're from the same place!

Otherwise, print
    Hi <full name>, I'd like to visit <town name>!

HINT: You can reuse the functions that you wrote in PROMPT 1 and Prompt 2.

Examples: (still assume my hometown is San Francisco)
    - 'Fido', 'Bark', 'Oakland' -> Hi Fido Bark, I'd like to visit Oakland!
    - 'Mel', 'M', 'San Francisco' -> Hi Mel M, we're from the same place!

Arguments:
    - First name (str)
    - Last name (str)
    - Hometown (str)
"""

# Write your function here

def greeting(hometown,first,last):
    """Greet the user and say if they're from the same place or wanting to visit their hometown"""

    hometown = matching_hometowns(hometown)#reusing function
    name = full_name(first,last)#reusing function

    if hometown == "San Francisco":
        return f"Hello {name}, we're from the same town!"

    else:
        return f"Hey {name}, I want to visit {your_hometown} some day!"

print(greeting(hometown, first, last))#call function

print()#adding space


"""PROMPT 4

Write a function that returns True if a fruit is a berry.

Valid berries are:
    - strawberry
    - raspberry
    - blackberry
    - currant

Examples:
    - currant -> True
    - durian -> False

Arguments:
    - A fruit (str)

Return:
    - True or False (bool)
"""

# Write your function here
fruits = input("Write the name of a fruit: ")
berries = ['strawberry', "raspberry", 'blackberry', 'currant','blueberry','boysenberry']

def identify_berry(fruits):
    """See if the given fruits are berries or not"""
    
    # berries = ['strawberry', "raspberry", 'blackberry', 'currant','blueberry','boysenberry']#list of potential berries

    if fruits in berries: #check if given fruit is in the berries list
        return "Yes, that's a berry!"

    else:
        return "Sorry, that's not a berry" 

print(identify_berry(fruits)) #call function

print()#adding space


"""PROMPT 5

Write a function that returns the shipping cost of an item.

Berries cost $0 to ship. Everything else costs $5.

Arguments:
    - Something that needs to be shipped (str)

Return:
    - Shipping cost (int)
"""

# Write your function here
def shipping_cost(fruits):
    """Tells user the shipping cost for berries or other items"""
    berry = identify_berry(fruits) #getting input from previous function

    if fruits in berries: #comparing input to the berries list
        return f"The {fruits} will ship for FREE!"
    
    else:
        return f"The {fruits} will cost $5 to ship."

print(shipping_cost(fruits))#call the function

print()#adding space

"""PROMPT 6

Write a function that returns the total cost of something by applying
taxes and fees of various states.

States will be given as their two-letter abbreviations. For example,
California's abbreviation is 'CA'.

There are some states with special fees. All fees should be added to the new
subtotal *after* tax:
    - CA (California): add a 3% (0.03) tax for recycling
    - PA (Pennsylvania): add $2.00 safety fee
    - MA (Massachusettes):
        - add $1.00 for items with a base price of $100.00 or less
        - add $3.00 for items over $100.00

Arguments:
    - Base price (int)
    - Two-letter state abbreviation (str)
    - Tax percentage as a decimal (optional, float)
        - If a tax percentage is not given, it defaults to 0.05 (or 5%)

Return:
    - Total price after taxes and fees (float)
"""

# Write your function here
price = float(input("How much is your item?> "))
state = input("Choose a state [CA, PA, MA] > ")

print()#adding space

def total_cost(price,state,tax_and_fees = 0.05):
    """Calculate the taxes and cost by state"""

    CA_tax = 0.03
    PA_fee = 2.00
    MA_fee = 1.00 #if cost is < $100
    MA_added_fee = 3.00 #if cost is > $100

    total_price = 0 

    if state == "CA":
        CA_total = price + CA_tax
        total_price += CA_total

    elif state == "PA":
        PA_total = price + PA_fee
        total_price += PA_total
    
    elif state == "MA": #MA has 2 conditions
        if price < 100.00:
            MA_total = price + MA_fee
            total_price += MA_total
        else:
            total_price = price + MA_added_fee
    
    return f"Your total cost is: ${float(total_price)}"

print(total_cost(price,state,tax_and_fees = 0.05))#call the function

print()#adding space

"""PROMPT 7

Write a function that takes in a list and *any* number of additional arguments.
The function should add all those items to the end of the  list and return
the list.

We haven't taught you how to do this! You'll need to do some research on your
own --- find a way to write a Python function that can take in an arbitrary
amount of arguments.

Arguments:
    - A list (list)
    - Additional args

Return:
    - A list with arguments added to the end (list)
"""

# Write your function here
groceries = ['cereal', 'bananas', 'almond milk', 'spinach']

def grocery_list(groceries, *added_groceries):
    """Add groceries to the current grocery list"""
    
    return groceries + list(added_groceries)#add to the groceries list and change tuple into a list


print(grocery_list(groceries, 'tofu', 'apples'))#call the function

print()#adding space


"""PROMPT 8

Write a function that takes in a word and returns a tuple. You'll do this in an
interesting way though, so make sure you read these directions thoroughly.

The tuple will contain two items:
    - The given word
    - The given word, multiplied 3 times

To do this, your function will create an *inner* function. The *inner*
function will multiply the given word by 3 and return it.

Then, the outer function will call the *inner* function to create a tuple.

Examples:
    - 'hi' -> ('hi', 'hihihi')

Arguments:
    - A word (str)

Return:
    - (word, wordx3) (tuple)
"""

# Write your function here
users_word = input("Type in a word: ")

def create_a_tuple(users_word):
    """Take in a word and mulitply it by 3"""


    def multiple_word(users_word, n=3): #hidden from outer function
        return users_word * n
        
    
    new_word = multiple_word(users_word, n=3)#call the inner function

    # return word, new_word 
    return users_word, (new_word) #return the user's word and the tuple

print(create_a_tuple(users_word))#call the outer function
