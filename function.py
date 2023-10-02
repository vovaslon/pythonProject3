import json

def take_info():
    """получает информацию из базы данных"""
    with open('operation.json', encoding='utf-8') as file:
        operations = json.load(file)
        return operations

def sort_by(data):
    """сортирует по типу операции и дате"""
    done_operatinos = []
    for operation in data:
        if operation.get("state") == "EXECUTED":
            done_operatinos.append(operation)
    done_operatinos.sort(key=lambda dictionary: dictionary['date'])
    done_operatinos.reverse()
    return done_operatinos


def hide_cardnumbers(card):
    """скрывает часть номера карты """
    numbers = card.split()[-1]
    return f'{card.split()[0]} {numbers[0:4]} {numbers[4:6]}** **** {numbers[-4:]}'


def hide_accountnumbers(account):
    """скрывает номер счета"""
    numbers = account.split()[-1]
    return f'{account.split()[0]} **{numbers[-4:]}'


def formatted_date(date):
    """для отображения даты в нужном формате"""
    date_f = date.split('T')[0]
    return f'{date_f[-2:]}.{date_f[-5:-3]}.{date_f[0:4]}'


def process_data(data, count=5):
    total_list = []
    for i in range(count):
        op = data[i]
        date = formatted_date(op['date'])
        trans_from = ''
        if 'from' in op:
            if 'счет' in op['from'].lower():
                trans_from = f'{hide_accountnumbers(op["from"])} -> '
            else:
                trans_from = f'{hide_cardnumbers(op["from"])} -> '
        trans_to = hide_accountnumbers(op['to']) if 'счет' in op['to'].lower() \
            else hide_cardnumbers(op['to'])
        amount = f'{op["operationAmount"]["amount"]} {op["operationAmount"]["currency"]["name"]}'
        total_list.append(f'{date} {op["description"]}\n{trans_from}{trans_to}\n{amount}\n')
    return total_list

