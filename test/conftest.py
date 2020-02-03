import pytest

@pytest.fixture
def response_after_use_json():
    return { 'status': 1,
             'code': "80761761",
             'product':{'nutrition_grades':'e'}
            }