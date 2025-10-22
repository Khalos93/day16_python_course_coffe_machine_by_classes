from coffe_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine


latte = MenuItem('latte',100, 200, 24, 2.5)
cappuccino = MenuItem('cappuccino', 250, 50, 24, 3)
espresso = MenuItem('espresso', 50, 0, 12, 1.5)

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    print("Welcome to our coffee shop! What can I serve you?")
    drink_order = str(input(f"{menu.get_items()}"))
    if drink_order == 'report':
        coffe_maker.report()
        money_machine.report()

    elif drink_order == 'off':
        break
    else:
        drink_order = menu.find_drink(drink_order)
        if not drink_order:
            continue

        if not coffe_maker.is_resource_sufficient(drink_order):
            continue

        else:
            payment = money_machine.make_payment(drink_order.cost)
            if not payment:
                continue
            else:
                coffe_maker.make_coffee(drink_order)
