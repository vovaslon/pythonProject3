from function import take_info,sort_by, process_data


def main():
    data = take_info()
    sort_data = sort_by(data)
    result = process_data(sort_data, 5)
    print('\n'.join(result))

main()