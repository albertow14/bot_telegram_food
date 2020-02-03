import pytest
from ..magreator import get_info_of
from ..custom_errors import CodeBarNotValid

def test_happy_path():
    code_number = '80761761'

    result = get_info_of(code_number)

    assert result.get('nutrition_grades') == 'e'

def test_number_is_ok():
    code_number = '1'

    with pytest.raises(CodeBarNotValid):
        result = get_info_of(code_number)


