from menu import MENU, resources


# TODO: import Menu and base resource values - Done
def initialize():
    milk_init = resources['milk']
    water_init = resources['water']
    coffee_init = resources['coffee']
    return milk_init, water_init, coffee_init


def restock():
    resources['milk'] += 500
    resources['water'] += 500
    resources['coffee'] += 500
    return initialize()


def startpoint():
    print("What would you like?")
    order = input('(espresso/latte/cappuccino):')
    return order, MENU[order]


# TODO: define a method to print how much resources we have - Done
def resource_report(milk_stat, water_stat, coffee_stat, money_stat):
    print(f"Water: {water_stat}ml\nMilk: {milk_stat}ml\nCoffee: {coffee_stat}ml\nMoney: ${money_stat}")


# TODO: define method that checks if there is enough resources to make order - Done
def resource_check(order_ingredients):
    #print(order_ingredients)
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Not enough {item}, need to restock!")
            return False
    return True


# TODO: define a method that receives money in quarters, dimes, pennies and nickels - Done
def money_input(order):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    total = money_count(quarters, dimes, nickles, pennies)
    if total < order['cost']:
        print("Insufficient funds, refunding money...")
        return -1
    else:
        return total


# TODO: define a method that adds the money together - Done
def money_count(quarter_count, dime_count, nickel_count, penny_count):
    return (quarter_count*0.25)+(dime_count*0.1)+(nickel_count*0.05)+(penny_count*0.01)


if __name__ == "__main__":
    milk, water, coffee = initialize()
    choice = True
    while choice:
        if milk|water|coffee < 50:
            milk, water, coffee = restock()
        drink_name, drink = startpoint()
        money = money_input(drink)
        if money > -1:
            resource_report(milk, water, coffee, money)
            if resource_check(drink['ingredients']):
                print(f"Order received. Here's your {drink_name}. Enjoy!")
                if money - drink['cost'] > 0:
                    print(f"your change is ${money - drink['cost']}")

            print("would you like another drink?")
            choice_change = input("Yes(y) or No(n): ").lower()
            if choice_change == 'n':
                choice = False
