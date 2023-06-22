from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

make_coffee = True
while make_coffee:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        make_coffee = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_data = menu.find_drink(choice)
        if drink_data:
            if coffee_maker.is_resource_sufficient(drink_data) and money_machine.make_payment(drink_data.cost):
                coffee_maker.make_coffee(drink_data)
