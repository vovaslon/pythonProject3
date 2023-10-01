import json

def take_info():
    with open('operation.json', encoding='utf-8') as file:
        operations = json.load(file)
        return operations

def sort_by():
    operations = take_info()
    done_operatinos = []
    for operation in operations:
        if operation.get("state") == "EXECUTED":
            done_operatinos.append(operation)
    done_operatinos.sort(key=lambda dictionary: dictionary['date'])
    done_operatinos.reverse()
    return done_operatinos


def print_5(dict):
    for i in range(5):
        print(dict[i])


def hide_cardnumbers(card):
    numbers = card.split()[-1]
    return (f'{numbers[0:4]} {numbers[4:6]}** **** {numbers[-4:]}')


def hide_accountnumbers(account):
    numbers = account.split()[-1]
    return (f'**{numbers[-4:]}')



