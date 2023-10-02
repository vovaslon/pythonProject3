from function import hide_cardnumbers



def test_hide_cardnumbers():
    assert hide_cardnumbers('MasterCard 7158300734726758') == 'MasterCard 7158 30** **** 6758'
    assert hide_cardnumbers('Счет 44812258784861134719') == 'Счет 4481 22** **** 4719'
