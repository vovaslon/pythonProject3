from function import take_info
from function import date_
from function import sort_by
from function import hide_cardnumbers
from function import hide_accountnumbers

take_info()
base = sort_by()
user_input = input('Для отображения последних 5 операций нажмите Enter').lower()
if user_input == '':
    for i in range(5):
        if 'from' in base[i-1]:
            print(f'\n{date_(base[i - 1]["date"])} {base[i - 1]["description"]}\n{hide_cardnumbers(base[i - 1]["from"])} ->'
                  f'{hide_accountnumbers(base[i - 1]["to"])}\n{base[i-1]["operationAmount"]["amount"]} '
                  f'{base[i-1]["operationAmount"]["currency"]["name"]}')
        else:
            print(f'\n{date_(base[i - 1]["date"])} {base[i - 1]["description"]}\n'
                  f'{hide_accountnumbers(base[i - 1]["to"])}')
else:
    print('Введена неверная команда')
