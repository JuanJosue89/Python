#!/usr/bin/env python
from utils import print_message, get_size, order_latte

def coffe_bot():
    print('Welcome to the cafe!')
    
    order_drink = 'y'
    drinks = []

    while order_drink == 'y':
        size = get_size()
        drink_type = get_drink_type()

        drink = '{} {}'.format(size, drink_type)
        print('Alright, that\'s a {}!'.format(drink))
        drinks.append(drink)
        while True:
            order_drink = input('Would you like order another drink? (y/n) ')
            if order_drinl in ['y', 'n']:
                break
            print('Okay, so I have: ')

            for drink in drinks:
                print('-', drink)

                name = input('Can I get your name please? \n ')
                print('Thanks, {}! Your order will be ready shortly.'.format(name))

def get_drink_type():
    res = input('What type of drinl would you like? \n[a] Brewed Coffe \n[b] Mocha \n[c] Latte \n> ')

    if res == 'a':
        return 'Brewed Coffe'
    elif res == 'b':
        return 'Mocha'

    print_message()

coffe_bot()
order_mocha()
