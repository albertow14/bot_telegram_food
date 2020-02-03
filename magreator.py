import requests
from custom_errors import CodeBarNotValid

def get_info_of(code_number):
    try:
        _check(code_number)
        base_url = 'https://world.openfoodfacts.org/api/v0/product/'
        response = requests.get(f'{base_url}{code_number}.json').json()
        return response.get('product')
    except CodeBarNotValid:
        return {'errors': 'Code bar not valid'}

def _check(code_number):
    print(f'AAAAAAAAAAAAAAAA{code_number}')
    if len(code_number.chat.get('text')) < 8: # 'Message' has no len()
        raise CodeBarNotValid