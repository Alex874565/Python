from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
menu = Menu()

on = True

while on:
    coffeemaker.report()
    order = input(f"What would you like? {menu.get_items()} ")
    
    if order == "off":
        on = False
        exit()
        
    elif order == "report":
        coffeemaker.report()
        moneymachine.report()
        print("\n")

    else:
        drink = menu.find_drink(order)
        enough_resources = coffeemaker.is_resource_sufficient(drink)
        
        if enough_resources:
            paid = moneymachine.make_payment(drink.cost)
            
            if paid:
                coffeemaker.make_coffee(drink)
