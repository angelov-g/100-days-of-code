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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_balance = 0


def prompt_user():
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return choice


def enough_resources(coffee):
    for ingredient in MENU[coffee]["ingredients"]:
        if resources[ingredient] < MENU[coffee]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
        else:
            return True


def process_coins(quarters, dimes, nickles, pennies):
    total_quarters = quarters * 0.25
    total_dimes = dimes * 0.10
    total_nickles = nickles * 0.05
    total_pennies = pennies * 0.01
    total = total_quarters + total_dimes + total_nickles + total_pennies
    return round(total, 2)


def make_coffee(coffee):
    for ingredient in MENU[coffee]["ingredients"]:
        resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]
    print(f"Here is your {coffee} ☕. Enjoy!")


machine_on = True
while machine_on:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user_choice = prompt_user()
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt
    if user_choice == "off":
        machine_on = False
    # TODO: 3. Print report
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${machine_balance}")
    else:
        # TODO: 4. Check resources sufficient?
        if enough_resources(user_choice):
            print("Please insert coins.")
            quarters_in = int(input("How many quarters? "))
            dimes_in = int(input("How many dimes? "))
            nickles_in = int(input("How many nickles? "))
            pennies_in = int(input("How many pennies? "))
            # TODO: 5. Process coins.
            total_in = process_coins(quarters_in, dimes_in, nickles_in, pennies_in)
            # TODO: 6. Check transaction successful?
            if total_in < MENU[user_choice]["cost"]:
                print("Sorry that's not enough money. Money refunded")
            else:
                machine_balance += MENU[user_choice]["cost"]
                if total_in > MENU[user_choice]["cost"]:
                    change = total_in - MENU[user_choice]["cost"]
                    print(f"Here is ${round(change,2)} dollars in change.")
                # TODO: 7. Make Coffee.
                make_coffee(user_choice)
