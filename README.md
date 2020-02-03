# bot_telegram_food
With this bot we want to simplify the process of knowing the characteristics of the products without having to use apps directly from your mobile

We are using openfoodfacts api.

`base_url = https://world.openfoodfacts.org/api/v0/product/`

`product = 80761761`

end_url = f'{base_url}{product}.json'`

result:
https://world.openfoodfacts.org/api/v0/product/80761761.json


## For learning porpouses:

- ALL THE LOGIC, with TDD (delivery mechanism do not have logic, nor external libraries).
- If need to interact with outside and can't be mocked because of complex, Integration Test Needed.
- A function can't have more than 15 lines (unless we have a REALLY good reason).
