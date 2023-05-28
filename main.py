from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: 1 Create a MenuItem Class


# TODO: 2 Create a CoffeeMaker Class
my_coffee_maker = CoffeeMaker()


# TODO: 3 Create a MoneyMachine Class

my_money_machine = MoneyMachine()


menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    customers_choice = input(f"What would you like? ({options}).")
    if customers_choice == "off":
        is_on = False
    elif customers_choice == "reports":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(customers_choice)
        print(drink)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)



