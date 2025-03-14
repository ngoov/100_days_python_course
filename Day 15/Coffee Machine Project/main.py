from multiprocessing.sharedctypes import \
    Value
from tkinter.font import \
    names

MENU = {
    "e": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "l": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "c": {
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

def ask_coins(menu_item):
    inserted_coins = [
        { 'name': 'quarters', 'calc': 0.25 },
        { 'name': 'dimes', 'calc': 0.10 },
        { 'name': 'nickles', 'calc': 0.05 },
        { 'name': 'pannies', 'calc': 0.01 },
    ]
    print("Please insert coins.")
    total = 0
    for coin in inserted_coins:
        amount = int(input(f'How many {coin["name"]}?:'))
        total += amount * coin['calc']
    if total < menu_item['cost']:
        

def start_process():
    action = input('What would you like? ([e]spresso/[l]atte/[c]appuccino): ').lower()
    if action == 'e':
        ask_coins(MENU[action])

in_operation = True
while in_operation:
    start_process()

