import json

def take_info():
    """получает информацию из базы данных"""
    with open('operation.json', encoding='utf-8') as file:
        operations = json.load(file)
        return operations

def sort_by():
    """сортирует по типу операции и дате"""
    operations = take_info()
    done_operatinos = []
    for operation in operations:
        if operation.get("state") == "EXECUTED":
            done_operatinos.append(operation)
    # done_operatinos.sort(key=lambda dictionary: dictionary['date'])
    return done_operatinos


def hide_cardnumbers(card):
    """скрывает часть номера карты """
    numbers = card.split()[-1]
    return f'{card.split()[0]} {numbers[0:4]} {numbers[4:6]}** **** {numbers[-4:]}'


def hide_accountnumbers(account):
    """скрывает номер счета"""
    numbers = account.split()[-1]
    return f'{account.split()[0]} **{numbers[-4:]}'


def date_(date):
    """для отображения даты в нужном формате"""
    date_f = date.split('T')[0]
    return f'{date_f[-2:]}.{date_f[-5:-3]}.{date_f[0:4]}'


