MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


def is_resource_sufficient(item):
    for i in item:
        if item[i] >=resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

def coins():
    print("pls insert coins.")
    total=int(input("how many quarters?"))*0.25
    total+=int(input("how many dimes?"))*0.1
    total+=int(input("how many nickels?"))*0.05
    total+=int(input("how many pennies?"))*0.01
    return total
def transaction(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry, not enough money.Money refunded")
        return False


profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def make_coffee(drink_name,item):
    for i in item:
        resources[i]-=item[i]
    print(f"Here is {drink_name}.☕")



is_on=True
while is_on:
    ch=input("What would you like? (espresso/latte/cappuccino):")
    if ch=="off":
        is_on=False
    elif ch=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink=MENU[ch]
        if is_resource_sufficient(drink["ingredients"]):
            payment=coins()
            if transaction(payment,drink["cost"]):
                make_coffee(ch,drink["ingredients"])



