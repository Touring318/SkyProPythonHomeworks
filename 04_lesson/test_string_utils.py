import pytest
from StringUtils import StringUtils

test_string = StringUtils()

@pytest.mark.parametrize("start_string, end_string", [
    ('лето', 'Лето'),
    ('осень', 'Осень'),
    ('0сень', '0сень'),
    ('весна', 'Весна'),
    ('5647382910', '5647382910'),
    ('4етверочк@', '4етверочк@'),
    ('4 июля 2042', '4 июля 2042')
    ])
def test_capitilize_positive(start_string, end_string):
    test_string = StringUtils()
    result = test_string.capitilize(start_string)
    assert result == end_string

@pytest.mark.parametrize("start_string, end_string", [
    ('', ''),
    (' ', ' '),
    ('👌🤦‍♂️😉🤷‍♀️🐱‍👤😜✔', '👌🤦‍♂️😉🤷‍♀️🐱‍👤😜✔'),
    (None, None)
    ])
def test_capitilize_negative(start_string, end_string):
    test_string = StringUtils()
    if start_string is None:
        with pytest.raises(AttributeError):
            test_string.capitilize(start_string)
    else:
        result = test_string.capitilize(start_string)
        assert result == end_string

@pytest.mark.parametrize("start_string, end_string", [
    ('       лето', 'лето'),
    (' осень', 'осень'),
    ('    0сень', '0сень'),
    ('         5647382910', '5647382910'),
    ('      4етверочк@', '4етверочк@'),
    ('     4 июля 2042', '4 июля 2042')
    ])
def test_trim_positive(start_string, end_string):
    test_string = StringUtils()
    result = test_string.trim(start_string)
    assert result == end_string

@pytest.mark.parametrize("start_string, end_string", [
    ('      ', ''),
    ('         👌🤦‍♂️😉🤷‍♀️🐱‍👤😜✔', '👌🤦‍♂️😉🤷‍♀️🐱‍👤😜✔'),
    (None, None)
    ])
def test_trim_negative(start_string, end_string):
    test_string = StringUtils()
    if start_string is None:
        with pytest.raises(AttributeError):
            test_string.trim(start_string)
    else:
        result = test_string.trim(start_string)
        assert result == end_string

@pytest.mark.parametrize("start_string, end_string, delimeter", [
    ("a,b,d,e,f,g,h", ["a", "b", "d", "e", "f", "g", "h"], ","),
    ("100:200:300:400:500", ["100", "200", "300", "400", "500"], ":"),
    ("A B C D F G H", ["A", "B", "C", "D", "F", "G", "H"], " "),
    ("29 февраля 2024", ["29", "февраля", "2024"], " ")
    ])
def test_to_list_positive(start_string, end_string, delimeter):
    test_string = StringUtils()
    result = test_string.to_list(start_string, delimeter)
    assert result == end_string

@pytest.mark.parametrize("start_string, end_string, delimeter", [
    (" , , , , , , ", [" ", " ", " ", " ", " ", " ", " "], ","),
    ("", [], ":"),
    (None, [None], " ")
    ])
def test_to_list_negative(start_string, end_string, delimeter):
    test_string = StringUtils()
    if start_string is None:
        with pytest.raises(AttributeError):
            test_string.to_list(start_string, delimeter)
    else:
        result = test_string.to_list(start_string, delimeter)
        assert result == end_string

@pytest.mark.parametrize("start_string, symbol, set_result", [
    ("Понедельник", "д", True),
    ("New Year", " ", True),
    ("12345678901234567890", "5", True),
    ("00 часов 00 минут", "ы", False),
    ("0000000", "0", True),
    ])
def test_contains_positive(start_string, symbol, set_result):
    test_string = StringUtils()
    result = test_string.contains(start_string, symbol)
    assert result == set_result

@pytest.mark.parametrize("start_string, symbol, set_result", [
    ("", "", True),
    (" ", " ", True),
    ("12345678901234567890", "567", False),
    (None, None, True)
    ])
def test_contains_negative(start_string, symbol, set_result):
    test_string = StringUtils()
    if start_string is None:
        with pytest.raises(AttributeError):
            test_string.contains(start_string, symbol)
    else:
        result = test_string.contains(start_string, symbol)
        assert result == set_result

@pytest.mark.parametrize("start_string, symbols, end_string", [
    ("Тестирование", "ирование", "Тест"),
    ("00000", "00", "0"),
    ("100000", "00", "10"),
    ("1234567001", "234", "1567001"),
    ("10002345", "00", "102345"),
    ("Москва 2042", "20", "Москва 42")
    ])
def test_delete_symbol_positive(start_string, symbols, end_string):
    test_string = StringUtils()
    result = test_string.delete_symbol(start_string, symbols)
    assert result == end_string

@pytest.mark.parametrize("start_string, symbols, end_string", [
    ("", "", ""),
    (" ", " ", ""),
    (None, None, None)
    ])
def test_delete_symbol_negative(start_string, symbols, end_string):
    test_string = StringUtils()
    if start_string is None:
        with pytest.raises(AttributeError):
            test_string.delete_symbol(start_string, symbols)
    else:
        result = test_string.delete_symbol(start_string, symbols)
        assert result == end_string

@pytest.mark.parametrize("start_string, symbol, set_result", [
    ("Стрессоустойчивость", "c", False),
    ("987654321", "1", False),
    ("У нас все получится", "У", True)
    ])
def test_starts_with_positive(start_string, symbol, set_result):
    test_string = StringUtils()
    result = test_string.starts_with(start_string, symbol)
    assert result == set_result

@pytest.mark.parametrize("start_string, symbol, set_result", [
    ("", "", True),
    (" ", " ", True),
    ("Воодушевленность", "Ва", True),
    (None, None, False)
    ])
def test_starts_with_negative(start_string, symbol, set_result):
    test_string = StringUtils()
    if start_string is None:
        with pytest.raises(AttributeError):
            test_string.starts_with(start_string, symbol)
    else:
        result = test_string.starts_with(start_string, symbol)
        assert result == set_result

@pytest.mark.parametrize("start_string, symbol, set_result", [
    ("What this?", "?", True),
    ("4536271809", "0", False),
    ("Многоходовка", "М", False),
    ("12345zaqxswcde", "e", True)
    ])
def test_end_with_positive(start_string, symbol, set_result):
    test_string = StringUtils()
    result = test_string.end_with(start_string, symbol)
    assert result == set_result

@pytest.mark.parametrize("start_string, symbol, set_result", [
    ("", "", True),
    (" ", " ", True),
    ("Mashine learning", "ang", True),
    ("Mashine learning", "ing", True),
    (None, None, None)
    ])
def test_end_with_negative(start_string, symbol, set_result):
    test_string = StringUtils()
    if start_string is None:
        with pytest.raises(AttributeError):
            test_string.end_with(start_string, symbol)
    else:
        result = test_string.end_with(start_string, symbol)
        assert result == set_result

@pytest.mark.parametrize("string, empty_status", [
    ("Motherboard", False),
    ("123456123456", False),
    ("Once upon a time", False)
    ])
def test_is_empty_positive(string, empty_status):
    test_string = StringUtils()
    result = test_string.is_empty(string)
    assert result == empty_status

@pytest.mark.parametrize("string, empty_status", [
    ("", True),
    (" ", True),
    (None, None)
    ])
def test_is_empty_negative(string, empty_status):
    test_string = StringUtils()
    if string is None:
        with pytest.raises(AttributeError):
            test_string.is_empty(string)
    else:
        result = test_string.is_empty(string)
        assert result == empty_status

@pytest.mark.parametrize("start_list, joiner, end_string", [
    (["One", "Two", "Three", "Four", "Five"], ": ", "One: Two: Three: Four: Five"),
    ([2, 0, 2, 4], ", ", "2, 0, 2, 4")
    ])
def test_list_to_string_positive(start_list, joiner, end_string):
    test_string = StringUtils()
    result = test_string.list_to_string(start_list, joiner)
    assert result == end_string

@pytest.mark.parametrize("start_list, joiner, end_string", [
    ([], "", ""),
    (["", "", "", ""], ":", ":::"),
    ([" ", " ", " ", " "], "; ", " ;  ;  ;  ")
    ])
def test_list_to_string_negative(start_list, joiner, end_string):
    test_string = StringUtils()
    result = test_string.list_to_string(start_list, joiner)
    assert result == end_string
