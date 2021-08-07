#!/usr/bin/python
def print_message():
    print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')

    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print_message()
        return get_size()

def order_latte():
    res = input('And what kind of milk for your latte? \n[a] 2% mill \n[b] Non-Fat Milk \n[c] Soy Milk\n> ')

    if res == 'a':
        return 'Latte'
    elif res == 'b':
        return 'Non-Fat Latte'
    elif res == 'c':
        return 'Soy Latte'
    else:
        print_message()
        return order_latte()
