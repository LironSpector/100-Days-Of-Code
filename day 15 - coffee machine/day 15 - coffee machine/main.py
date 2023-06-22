from menu import MENU

water = 300
milk = 200
coffee = 100

money_paid = 0

cost = 0

wants_coffee = True
while wants_coffee:
    did_not_pay = True
    while did_not_pay:
        coffee_type = input("What would you like? (espresso/latte/cappuccino):").lower()
        if coffee_type == "off":
            did_not_pay = False
            wants_coffee = False
        elif coffee_type == "report":
            print(f"Water: {water}ml")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"Money: ${money_paid}")
        elif coffee_type != "espresso" and coffee_type != "latte" and coffee_type != "cappuccino":
            print("You didn't chose a kind of coffee")
        elif water < MENU[coffee_type]["ingredients"]["water"]:
            print("Sorry there is not enough water")
        elif coffee < MENU[coffee_type]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
        elif coffee_type != "espresso":
            if milk < MENU[coffee_type]["ingredients"]["milk"]:
                print("Sorry there is not enough milk")
            else:
                did_not_pay = False
        else:
            did_not_pay = False

    if coffee_type != "off":
        cost = MENU[coffee_type]["cost"]

        print("Please insert coins")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        total_pay = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
        if total_pay < cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            water -= MENU[coffee_type]["ingredients"]["water"]
            coffee -= MENU[coffee_type]["ingredients"]["coffee"]
            if coffee_type != "espresso":
                milk -= MENU[coffee_type]["ingredients"]["milk"]

            money_paid += cost

            change = round(total_pay - cost, 2)
            print(f"Here is ${change} in change.")
            print(f"Here is your {coffee_type} ☕️. Enjoy!")