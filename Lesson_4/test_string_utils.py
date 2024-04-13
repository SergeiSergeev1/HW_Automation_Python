import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.parametrize('string, result', [('sky','Sky'), ('sky, про', 'Sky, про'), ('и ван', 'И ван')])
def positive_test_capitilize( string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('string, result', [(' sky',' Sky'), ('_sky', '_Sky'), (None, ''),  (123, '123')])
def negative_test_capitilize(string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == result

@pytest.mark.parametrize('string, result', [('  sky','sky'), (' Иван', 'Иван'), (' 123', '123')])
def positive_test_trim(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('string, result', [('s ky','sky'), (None, ''), (' ', ' '), ([ 1,2,3], '1,2,3')])
def negative_test_trim(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result

@pytest.mark.parametrize('string, result', [("a,b,c,d", ["a", "b", "c", "d"]), (' ', []), ("1,2,3,4", ["1", "2", "3", "4"]),("@, $, *, &", ["@", " $", " *", " &"])])
def positive_test_to_list(string, result):
     string_utils = StringUtils()
     res = string_utils.to_list(string)
     assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('string, result', [("a b c d", ["a", " b", " c", " d"]), (' , ', []), ((1, 2, 3, 4), ["1", "2", "3", "4"]) ])
def negative_test_to_list(string, result):
     string_utils = StringUtils()
     res = string_utils.to_list(string)
     assert res == result


@pytest.mark.parametrize('string, delimeter, result', [("a:b:c:d", ":", ["a", "b", "c", "d"]), ("1-2-3-4", "-", ["1", "2", "3", "4"]), ("@; $; *; &", ";", ["@", " $", " *", " &"])])
def positive_test_to_list_with_delimeter(string, delimeter, result):
    string_utils = StringUtils()
    res = string_utils.to_list(string, delimeter)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('string, delimeter, result', [("a b c d", ":", ["a", "b", "c", "d"]), ("1-2-3-4", ":", ["1", "2", "3", "4"]), (None, ":", [])])
def negative_test_to_list_with_delimeter(string, delimeter, result):
    string_utils = StringUtils()
    res = string_utils.to_list(string, delimeter)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [('Sky', 'S', True), ('Sky', '', False), ('S ky', ' ', True), ('Sky', 'F', False)])
def positive_test_contain(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains( string, symbol)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', [('Sky', 'S', False), ('Sky', 'u', True), ('Sky', ' ', True), (123, 2, False)])
def negative_test_contain(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains( string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [('SkySro', 'S', 'kyro'), ('Sky@Pro', '@', 'SkyPro'), ('123456', '123', '456'), ('SkyPro', '', 'SkyPro')] )    
def positive_test_delete_symbol(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', [('SkyPro', None, 'SkyPro'), (['SkyPro'], ['Sky'], 'Pro'), (123456, 123, 456)] )    
def negative_test_delete_symbol(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == result
   

@pytest.mark.parametrize('string, symbol, result', [('Sky', 'S', True), ('Sky', 'u', False), ('@,2,3,4', '@', True), ('1234', '', False)])
def positive_test_starts_with(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(string, symbol)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', [('S,k,y', 'Y', True), ('Sky', ' ', True), (1234, '1', True), (['1,2,3,4'], '4', False)])
def negative_test_starts_with(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [('Sky', 'y', True), ('Sky', '', False),('@23', '@', False), ('1,2,3,4', '4', True)])
def positive_test_end_with(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(string, symbol)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', [('Sky', 'y', False), ('Sky', None, False),(123, '1', False), (['1,2,3,4'], '4', True)])
def negative_test_end_with(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, result', [('', True), ('  ', True), ('S', False)])
def positive_test_is_empty(string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(string)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('string, result', [("'',''", True), (['  ',''], True), ('', False), (None, True)])
def negative_test_is_empty(string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(string)
    assert res == result

@pytest.mark.parametrize('input_list, result', [([], ""), ([1,2,3,4], "1, 2, 3, 4"), (['Sky', 'Pro'], "Sky, Pro")])
def positive_test_list_to_string(input_list, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(input_list)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('input_list, result', [(None, ""), ('1,2,3,4', '1,2,3,4')])
def negative_test_list_to_string(input_list, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(input_list)
    assert res == result

@pytest.mark.parametrize('input_list, joiner, result', [(["sky", "pro"], "-", "sky-pro"), ([1, "мая", 2024], "-", "1-мая-2024")])
def positive_test_to_list_with_joiner(input_list, joiner,result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(input_list, joiner)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('input_list, joiner, result', [(["sky, pro"], "-", "sky-pro"), ([], "-", "-"), (None,'-','1-')])
def negative_test_to_list_with_joiner(input_list, joiner,result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(input_list, joiner)
    assert res == result





