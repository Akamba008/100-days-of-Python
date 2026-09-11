MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def sum_up():
    quarters = float(input("How many quarters: "))
    dimes = float(input("How many dimes: "))
    nickles = float(input("How many nickles: "))
    pennies = float(input("How many pennies: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total

def not_enough(order):
    if MENU[order]["ingredients"]["water"] > resources["water"]:
        print("Sorry there isn't enough water for your drink 😫. ")
    elif MENU[order]["ingredients"]["milk"] > resources["milk"]:
         print("Sorry there isn't enough milk for your drink 😫. ")
    elif MENU[order]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there isn't enough coffee for your drink 😫. ")


def coffee_machine():
    money = 0
    ordering = True
    while ordering:
        prompt = str(input("What would you like to order? (Espresso/Latte/Cappuccino): ")).lower()
        if prompt == "report":
            print(f'''
                1. Water = {resources["water"]}ml
                2. Milk = {resources["milk"]}ml
                3. Coffee = {resources["coffee"]}g
                4. Money = ${money}
                ''')
        elif prompt == "off":
            return
        else:
            if prompt != "espresso" and prompt != "latte" and prompt != "cappuccino":
                print("Please enter either Espresso/Latte/Cappuccino")
            else:
                if MENU[prompt]["ingredients"]["water"] > resources["water"] or MENU[prompt]["ingredients"]["milk"] > resources["milk"] or MENU[prompt]["ingredients"]["coffee"] > resources["coffee"]:
                    not_enough(prompt)
                else:
                    inadequate = True
                    while inadequate:
                        if money < MENU[prompt]["cost"]:
                            print("You don't have enough money for this drink 😫. Top-up your funds.")
                            money += sum_up()
                        else:
                            inadequate = False
                    print(money)
                    money -= MENU[prompt]["cost"]
                    if money > 0:
                        print(f"Here is your change: ${money}")
                    print(f"Here is your {prompt} ☕. Enjoy!")
                    print()
                    for resource in resources:
                        resources[resource] -= MENU[prompt]["ingredients"][resource]


coffee_machine()