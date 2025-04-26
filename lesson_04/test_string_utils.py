import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str,expected", [
    ("skypro", "Skypro"),])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
def test_capitalize_invalid_type():
    with pytest.raises(AttributeError):
        string_utils.capitalize(12345)

@pytest.mark.positive
@pytest.mark.parametrize("input_str,expected", [
    ("   skypro", "skypro")])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
def test_trim_empty_string():
    res = string_utils.trim("")
    assert res == ""

@pytest.mark.positive
@pytest.mark.parametrize("input_str,symbol,expected", [
    ("SkyPro", "S", True)])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str,symbol,expected", [
    ("SkyPro", "U", False)])
def test_contains_false(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str,symbol", [
    (None, "S"),
    (12345, "S"),
])
def test_contains_negative(input_str, symbol):
    with pytest.raises(AttributeError):
        string_utils.contains(input_str, symbol)


@pytest.mark.positive
@pytest.mark.parametrize("input_str,symbol,expected", [
    ("SkyPro", "Pro", "Sky")])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.negative
def test_delete_symbol_not_found():
    res = string_utils.delete_symbol("SkyPro", "XYZ")
    assert res == "SkyPro"