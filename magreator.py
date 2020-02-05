import requests
from custom_errors import CodeBarNotValid

def get_info_of(code_number):
    base_url = 'https://world.openfoodfacts.org/api/v0/product/'
    response = requests.get(f'{base_url}{code_number.text}.json').json()
    print(response, 'aaaaadsfdafadsfsfsafsa')
    if response.get('status_verbose') == 'product not found':
        return {'product_name':'Alberto','nutriscore_grade':'No seas Flojo' }    
    return response.get('product')
    