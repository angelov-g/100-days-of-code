from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino/):"
    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice == "off":
        machine_on = False
    # TODO: 3. Print report.
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        # TODO: 4. Check resources sufficient?
        if coffee_maker.is_resource_sufficient(drink):
            # TODO: 5. Process coins.
            # TODO: 6. Check transaction successful?
            if money_machine.make_payment(drink.cost):
                # TODO: 7. Make Coffee.
                coffee_maker.make_coffee(drink)
