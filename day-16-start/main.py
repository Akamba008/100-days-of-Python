from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

def coffee_machine():
    while True:
        options = menu.get_items()
        prompt = input(f"What would you like to order, {options} :").lower()
        if prompt == "report":
            coffee_maker.report()
            money_machine.report()
        elif prompt == "off":
            return
        elif prompt == "drinks":
            print(options)
        else:
            drink = menu.find_drink(prompt)
            if drink == None:
                print(f"Sorry, we don't have {prompt}.")
            else:
                sufficient = coffee_maker.is_resource_sufficient(drink)
                if sufficient and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


coffee_machine()