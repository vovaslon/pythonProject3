from function import take_info
from function import date_
from function import sort_by
from function import hide_cardnumbers

take_info()
base = sort_by()
user_input = input('Для отображения последних 5 операций нажмите Enter').lower()
if user_input == '':
    for i in range(5):
        print(f'{date_(base[i - 1]["date"])} {base[i - 1]["description"]}\n{hide_cardnumbers(base[i - 1]["from"])}')
else:
    print('Введена неверная команда')
