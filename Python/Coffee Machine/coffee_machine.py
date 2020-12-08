espresso_water = 250
espresso_coffee = 16
espresso_money = 4

latte_water = 350
latte_milk = 75
latte_coffee = 20
latte_money = 7

cappuccino_water = 200
cappuccino_milk = 100
cappuccino_coffee = 12
cappuccino_money = 6

water = 400
milk = 540
coffee = 120
cups = 9
money = 550


def remaining():
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(coffee) + " of coffee beans")
    print(str(cups) + " of disposable cups")
    print(str(money) + " of money")


def buy():
    global water
    global milk
    global coffee
    global money
    global cups

    buy_input = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")

    if buy_input == "1":
        if water < espresso_water:
            print("Sorry, not enough water!")
        elif coffee < espresso_coffee:
            print("Sorry, not enough coffee beans!")
        elif cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= espresso_water
            coffee -= espresso_coffee
            cups -= 1
            money += espresso_money

    elif buy_input == "2":
        if water < latte_water:
            print("Sorry, not enough water!")
        elif milk < latte_milk:
            print("Sorry, not enough milk!")
        elif coffee < latte_coffee:
            print("Sorry, not enough coffee beans!")
        elif cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= latte_water
            milk -= latte_milk
            coffee -= latte_coffee
            cups -= 1
            money += latte_money

    elif buy_input == "3":
        if water < cappuccino_water:
            print("Sorry, not enough water!")
        elif milk < cappuccino_milk:
            print("Sorry, not enough milk!")
        elif coffee < cappuccino_coffee:
            print("Sorry, not enough coffee beans!")
        elif cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= cappuccino_water
            milk -= cappuccino_milk
            coffee -= cappuccino_coffee
            cups -= 1
            money += cappuccino_money

    elif buy_input == "back":
            pass

    else:
        print("error")


def fill():
    global water
    global milk
    global coffee
    global cups
    fill_water = int(input("Write how many ml of water do you want to add: "))
    fill_milk = int(input("Write how many ml of milk do you want to add: "))
    fill_coffee = int(input("Write how many grams of coffee beans do you want to add: "))
    fill_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    water += fill_water
    milk += fill_milk
    coffee += fill_coffee
    cups += fill_cups


def take():
    global money
    print("I gave you $" + str(money))
    money = 0


while True:
    user_input = input("Write action (buy, fill, take, remaining, exit): ")
    if user_input == "buy":
        print("")
        buy()
        print("")

    elif user_input == "remaining":
        print("")
        remaining()
        print("")

    elif user_input == "fill":
        print("")
        fill()
        print("")

    elif user_input == "take":
        print("")
        take()
        print("")

    elif user_input == "exit":
        break

    else:
        print("")
        print("error")
        print("")
