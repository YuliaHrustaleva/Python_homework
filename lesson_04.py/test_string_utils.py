import pytest
from string_utils import StringUtils

@pytest.fixture
def utils():
    return StringUtils()

# --- Тесты для метода capitalize ---

@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),         # Обычная строка строчными буквами
    ("hello world", "Hello world"), # Строка с пробелом
    ("Skypro", "Skypro"),         # Первая буква уже заглавная
])
def test_capitalize_positive(utils, input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                     # Пустая строка
    ("123sky", "123sky"),         # Строка начинается с цифры
    (" skypro", " skypro"),       # Строка начинается с пробела
])
def test_capitalize_negative(utils, input_str, expected):
    assert utils.capitalize(input_str) == expected


# --- Тесты для метода trim ---

@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),         # Один пробел в начале
    ("   test", "test"),           # Несколько пробелов в начале
    (" skypro ", "skypro "),       # Пробелы в начале и в конце (конец не должен меняться)
])
def test_trim_positive(utils, input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "skypro"),         # Без пробелов в начале
    ("", ""),                     # Пустая строка
    ("  ", ""),                   # Строка только из пробелов
])
def test_trim_negative(utils, input_str, expected):
    assert utils.trim(input_str) == expected


# --- Тесты для метода contains ---

@pytest.mark.parametrize("input_str, symbol", [
    ("SkyPro", "P"),              # Символ в середине строки
    ("SkyPro", "ro"),             # Подстрока в конце строки
])
def test_contains_positive(utils, input_str, symbol):
    assert utils.contains(input_str, symbol) is True


@pytest.mark.parametrize("input_str, symbol", [
    ("SkyPro", "S"),              # БАГ: символ на 0-м индексе (index == 0, условие > -1 упадет)
    ("SkyPro", "U"),              # Отсутствующий символ
    ("", "S"),                    # Поиск в пустой строке
])
def test_contains_negative(utils, input_str, symbol):
    # В зависимости от требований, здесь проверяется ожидаемое поведение (False)
    assert utils.contains(input_str, symbol) is False


# --- Тесты для метода delete_symbol ---

@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),      # Удаление одной буквы
    ("SkyPro", "Pro", "Sky"),      # Удаление подстроки
    ("sky-sky-sky", "sky", "--"), # Удаление всех вхождений подстроки
])
def test_delete_symbol_positive(utils, input_str, symbol, expected):
    assert utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "z", "SkyPro"),     # Удаление отсутствующего символа
    ("", "k", ""),                 # Удаление из пустой строки
    ("SkyPro", "", "SkyPro"),      # Передача пустого символа для удаления
])
def test_delete_symbol_negative(utils, input_str, symbol, expected):
    assert utils.delete_symbol(input_str, symbol) == expected
