# This is the function file for the Cat Cafe game. It is imported into the game file to make things simpler.

# Here is a list of each drink order that can be made in the game. I use a for loop to make print statements, as well as to check for accuracy.

# Ice Water
water_list = ['Cold Water','Ice Cubes','Toothpick Umbrella']
# Matcha Lattes
matcha_list = ['Hot Water', 'Matcha Powder', 'Whisk', "Soy Milk", 'Whisk']
matcha_list_1 = ['Hot Water','Matcha Powder','Whisk','Soy Milk',"Latte Art"]
# Hot Tea
tea_list = ['Hot Water', 'TEA', 'Sachet', 'Add to Water', 'Biscuit']
tea_list_1 = ['Hot Water', 'Green', 'Sachet', 'Add To Water', 'Biscuit']
tea_list_2 = ['Hot Water', 'Jasmine', 'Sachet', 'Add To Water', 'Biscuit']
tea_list_3 = ['Hot Water', 'Earl Grey', 'Sachet', 'Add To Water', 'Biscuit']
tea_list_4 = ['Hot Water', 'Chai', 'Sachet', 'Add To Water', 'Biscuit']
tea_list_5 = ['Hot Water', 'Ginger', 'Sachet', 'Add To Water', 'Biscuit']
# Bubble Tea
boba_list = ['Coconut Milk', 'FLAVOR', 'Stir', 'Bubbles']
boba_list_1 = ['Coconut Milk', 'Coffee', 'Stir', 'Bubbles']
boba_list_2 = ['Coconut Milk', 'Strawberry', 'Stir', 'Bubbles']
boba_list_3 = ['Coconut Milk', 'Mango', 'Stir', 'Bubbles']
boba_list_4 = ['Coconut Milk', 'Watermelon', 'Stir', 'Bubbles']
boba_list_5 = ['Coconut Milk', 'Lychee', 'Stir', 'Bubbles']
# Smoothies
smoothie_list = ['Banana', 'ITEM ONE', 'ITEM TWO', 'ITEM THREE', 'Coconut Water', 'Blend']
smoothie_list_1 = ['Banana', 'Strawberry', 'Peanuts', 'Cacao', 'Coconut Water', 'Blend']
smoothie_list_2 = ['Banana', 'Cherry', 'Lime', 'Chia Seeds', 'Coconut Water', 'Blend']
smoothie_list_3 = ['Banana', 'Blueberry', 'Oats', 'Spinach', 'Coconut Water', 'Blend']
smoothie_list_4 = ['Banana', 'Dragonfruit', 'Mango', 'Cayenne', 'Coconut Water', 'Blend']
smoothie_list_5 = ['Banana', 'Kiwi', 'Raspberry', 'Spirulina', 'Coconut Water', 'Blend']
# Instant Coffee
coffee_list = ['Hot Water', 'Instant Coffee', 'Stir']

# A friend suggested I create a function with iteration to use for collecting user input.

def fetchInput(numIngredients): 
    userInputs = [] 
    for i in range(numIngredients): 
        userInputs.append(input(str(i+1)+": ").title().strip()) 
    return userInputs     

# I created this function so the user can press 'enter' to move on to next line. This helps the user know what to focus, and it creates a more interactive experience.

def continue_func():
    cont = input("")
    if cont == "":
        print(end = "")

# This is where the instructions for orders are stored. Another friend suggested that I put the ingredients in separate list and loop through them instead of printing them individually.

def ice_water():
    print('ICE WATER:')
    for ingredient in water_list:
        print(ingredient)

def matcha_latte():
    print("MATCHA LATTE:")
    for ingredient in matcha_list:
        print(ingredient)

def hot_tea():
    print("CUP OF TEA WITH BISCUIT:")
    for ingredient in tea_list:
        print(ingredient)

def boba_tea():
    print('BUBBLE TEA:')
    for ingredient in boba_list:
        print(ingredient)

def smoothie():
    print("SMOOTHIE:")
    for ingredient in smoothie_list:
        print(ingredient)

def coffee():
    print("COFFEE:")
    for ingredient in coffee_list:
        print(ingredient)

# I've used this little story tidbit to give the user a chance to understand game mechanics more moving to something more difficult. These functions were really troublesome to get right. But I finally got it with some help (and realizing that I made a silly mistake...)

def water_trial():
    print("Nadia: Pretend I'm a customer. Make me an Ice Water.")
    userInputs = fetchInput(3)
    if water_list == userInputs:
        print(" ")
    else:
        print("Your technique could use some work. Let's try again.")
        water_trial()

# These are the regular customer/story functions.

# Florence One
def flo_one():
    print("Flo: Matcha Latte with Soy Milk")
    userInputs = fetchInput(5)
    if matcha_list == userInputs:
        print(" ")
    else:
        print("Hmm... this drink could use a litte help. Would you please make another one?")
        flo_one()

# Florence Two
def flo_two():
    print("Flo: Matcha Latte with Soy Milk")
    userInputs = fetchInput(5)
    if matcha_list == userInputs:
        print(" ")
    else:
        print("Hmm... this drink could use a litte help. Would you please make another one?")
        flo_two()

# Florence Three
def flo_three():
    print('Flo: Matcha Latte with Soy Milk')
    userInputs = fetchInput(5)
    #matcha_list_1 has a secret step at the end that you have to read the source code to find (or make a very lucky guess...)
    if userInputs == matcha_list_1:
        print("Flo: The swamp puts a spell on nearby dwellers, making them more... suggestible.")
        continue_func()
        print("Nadia: (That explains a lot...)")
    #matcha_list is just a regular order, with the result being a regular response
    elif userInputs == matcha_list:
        print("Flo: Some secrets should stay secret.")
        continue_func()
        print("Flo: ... at least in this lifetime...")
    else:
        print("Hmm... this drink could use a litte help. Would you please make another one?")
        flo_three()

# Florence Four
def flo_four():
    print('Flo: Matcha Latte with Soy Milk.')
    userInputs = fetchInput(5)
    if matcha_list == userInputs:
        print(" ")
    else:
        print("Hmm... this drink could use a litte help. Would you please make another one?")
        flo_four()

# Florence Five
def flo_five():
    print('Flo: Matcha Latte with Soy Milk')
    userInputs = fetchInput(5)
    if matcha_list == userInputs:
        print(" ")
    else:
        print("Hmm... this drink could use a litte help. Would you please make another one?")
        flo_five()

# Dr. Spencer One
def spencer_one():
    print('Spencer: Green Tea with a biscuit')
    userInputs = fetchInput(5)
    if userInputs == tea_list_1:
        print(" ")
    else:
        print("This is unsatisfactory. I demand a new one.")
        spencer_one()

# Dr. Spencer Two
def spencer_two():
    print('Spencer: Jasmine Tea with a biscuit')
    userInputs = fetchInput(5)
    if userInputs == tea_list_2:
        print(" ")
    else:
        print("This is unsatisfactory. I demand a new one.")
        spencer_two()

# Dr. Spencer Three
def spencer_three():
    print('Spencer: Earl Gray Tea with a biscuit')
    userInputs = fetchInput(5)
    if userInputs == tea_list_3:
        print(" ")
    else:
        print("This is unsatisfactory. I demand a new one.")
        spencer_three()

# Dr. Spencer Four
def spencer_four():
    print('Spencer: Chai Tea with a biscuit')
    userInputs = fetchInput(5)
    if userInputs == tea_list_4:
        print(" ")
    else:
        print("This is unsatisfactory. I demand a new one.")
        spencer_four()

# Dr. Spencer Five
def spencer_five():
    print('Spencer: Ginger Tea with a biscuit')

    userInputs = fetchInput(5)

    if userInputs == tea_list_5:
        print(" ")
    else:
        print("This is unsatisfactory. I demand a new one.")
        spencer_five()

# Kylie One
def kylie_one():
    print('Kylie: Coffee flavored Boba Tea')
    userInputs = fetchInput(4)
    if userInputs == boba_list_1:
        print(" ")
    else:
        print("This one is kind of weird. Can I have another?")
        kylie_one()

# Kylie Two
def kylie_two():
    print('Kylie: Strawberry flavored Boba Tea')
    
    userInputs = fetchInput(4)

    if userInputs == boba_list_2:
        print(" ")
    else:
        print("This one is kind of weird. Can I have another?")
        kylie_two()

# Kylie Three
def kylie_three():
    print('Kylie: Mango flavored Boba Tea')
    userInputs = fetchInput(4)
    if userInputs == boba_list_3:
        print(" ")
    else:
        print("This one is kind of weird. Can I have another?")
        kylie_three()

# Kylie Four
def kylie_four():
    print('Kylie: Watermelon flavored Boba Tea')
    userInputs = fetchInput(4)
    if userInputs == boba_list_4:
        print(" ")
    else:
        print("This one is kind of weird. Can I have another?")
        kylie_four()

# Kylie Five
def kylie_five():
    print('Kylie: Lychee flavored Boba Tea')
    userInputs = fetchInput(4)
    if userInputs == boba_list_5:
        print(" ")
    else:
        print("This one is kind of weird. Can I have another?")
        kylie_five()

# Business Guy One
def bus_one():
    print('Silas: Black Coffee')
    userInputs = fetchInput(3)
    if coffee_list == userInputs:
        print(" ")
    else:
        print("THIS COFFEE SUCKS. I'm giving you guys zero stars on Yelp!!!")
        bus_one()

# Business Guy Two
def bus_two():
    print('Silas: Black Coffee') 
    userInputs = fetchInput(3)
    if coffee_list == userInputs:
        print(" ")
    else:
        print("THIS COFFEE SUCKS. I'm giving you guys zero stars on Yelp!!!")
        bus_two()

# Business Guy Three
def bus_three():
    print('Silas: Black Coffee')
    userInputs = fetchInput(3)
    if coffee_list == userInputs:
        print(" ")
    else:
        print("THIS COFFEE SUCKS. I'm giving you guys zero stars on Yelp!!!")
        bus_three()

# Business Guy Four
def bus_four():
    print('Silas: Black Coffee')
    userInputs = fetchInput(3)
    if coffee_list == userInputs:
        print(" ")
    else:
        print("THIS COFFEE SUCKS. I'm giving you guys zero stars on Yelp!!!")
        bus_four()

# Business Guy Five
def bus_five():
    print('Silas: Black Coffee')
    userInputs = fetchInput(3)
    if coffee_list == userInputs:
        print(" ")
    else:
        print("THIS COFFEE SUCKS. I'm giving you guys zero stars on Yelp!!!")
        bus_five()

# Traveler One
def trav_one():
    print('Traveler: Smoothie with Strawberry Peanuts and Cacao')
    userInputs = fetchInput(6)
    if userInputs == smoothie_list_1:
        print(" ")
    else:
        print("This smoothie is not aligned aligned with the energy of the universe. I shall give you one further attempt.")
        trav_one()

# Traveler Two
def trav_two():
    print('Traveler: Smoothie with Cherry Lime and Chia Seeds')
    userInputs = fetchInput(6)
    if userInputs == smoothie_list_2:
        print(" ")
    else:
        print("This smoothie is not aligned aligned with the energy of the universe. I shall give you one further attempt.")
        trav_two()

# Traveler Three
def trav_three():
    print('Traveler: Smoothie with Blueberry Oats and Spinach')
    userInputs = fetchInput(6)
    if userInputs == smoothie_list_3:
        print(" ")
    else:
        print("This smoothie is not aligned aligned with the energy of the universe. I shall give you one further attempt.")
        trav_three()

# Traveler Four
def trav_four():
    print('Traveler: Smoothie with Dragonfruit Mango and Cayenne')
    userInputs = fetchInput(6)
    if userInputs == smoothie_list_4:
        print(" ")
    else:
        print("This smoothie is not aligned aligned with the energy of the universe. I shall give you one further attempt.")
        trav_four()

# Traveler Five
def trav_five():
    print('Traveler: Smoothie with Kiwi Raspberry and Spirulina')
    userInputs = fetchInput(6)
    if userInputs == smoothie_list_5:
        print(" ")
    else:
        print("This smoothie is not aligned aligned with the energy of the universe. I shall give you one further attempt.")
        trav_five()