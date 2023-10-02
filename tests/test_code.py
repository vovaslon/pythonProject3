from function import hide_cardnumbers, hide_accountnumbers, process_data, take_info, sort_by, \
    formatted_date, sort_by



def test_hide_cardnumbers():
    assert hide_cardnumbers('MasterCard 7158300734726758') == 'MasterCard 7158 30** **** 6758'
def test_hide_cardnumbers_for_empty():
   assert hide_cardnumbers('MasterCard 7158300734726758') != None
def test_hide_accountnumbers():
    assert hide_accountnumbers("Счет 72082042523231456215") == 'Счет **6215'
def test_hide_accountnumbers_for_empty():
    assert hide_accountnumbers("Счет 72082042523231456215") != None
def test_process_data():
    assert process_data(sort_by(take_info()), 5) != []
def test_take_info_for_empty():
    assert take_info() != None
def test_formatted_date():
    assert formatted_date("2019-08-26T10:50:58.294041") == '26.08.2019'

def test_sort_by_for_empty():
    assert sort_by([]) != None

