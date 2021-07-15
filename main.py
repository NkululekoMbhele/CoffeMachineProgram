from data import MENU, resources

def sum_of_coins():
    """Takes user input and output the total amount inserted"""
    print("Please insert coins.")
    quarters = int(input("how many quaters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = quarters*0.25 + dimes*0.1 + nickles*0.5 + pennies *0.1
    return total

def order_coffee(coffee, cash):
    """takes coffee ordered and amount paid and proccess coffee sale printing change"""
    coffee_cost = MENU[coffee]["cost"]
    change = cash - coffee_cost
    print(f"cash ${cash}")
    print(f"cost ${coffee_cost}")
    print(f"Here is ${change} in change.")
    print(f"Here is your {coffee} ☕️. Enjoy!")

def low_amount_check(coffee, amount):
    """Check if the coins provided are enough"""
    coffee_cost = MENU[coffee]["cost"]
    if coffee_cost > amount:
        return True
    else:
        return False
    
WATER_LEFT = 0
MILK_LEFT = 0
COFFEE_LEFT = 0

def check_resources(coffee_chosen):   
    """Check resource availability"""  
    ## Take resources amount
    _water =  resources["water"]
    _milk =  resources["milk"]
    _coffee =  resources["coffee"]
    
    #initialize global variables
    WATER_LEFT = _water
    MILK_LEFT = _milk
    COFFEE_LEFT = _coffee
    
    #update the resources
    WATER_LEFT = _water
    MILK_LEFT = _milk
    COFFEE_LEFT = _coffee

coffee_available = True

coffee_ordered = input("What would you like? (espresso/latte/cappuccino): ")
amount_paid = sum_of_coins()

coffee_selected = ""

if (coffee_ordered == "espresso"):
    coffee_selected = "espresso"
elif (coffee_ordered == "latte"):
    coffee_selected = "latte"
elif (coffee_ordered == "cappuccino"):
    coffee_selected = "cappuccino"

if low_amount_check(coffee_selected, amount_paid):  
    print(f"Not enough coins, ${amount_paid} refunded")
else:
    order_coffee(coffee_selected, amount_paid)

