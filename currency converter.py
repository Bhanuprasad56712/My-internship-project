import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f'https://openexchangerates.org/api/latest.json?app_id={api_key}&base={base_currency}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        exchange_rate = data['rates'].get(target_currency)
        return exchange_rate
    else:
        return None

def currency_converter():
    api_key = 'YOUR_API_KEY'
    base_currency = input("Enter the base currency code (e.g., USD, EUR): ").upper()
    target_currency = input("Enter the target currency code (e.g., USD, EUR): ").upper()

    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)

            if exchange_rate is not None:
                converted_amount = amount * exchange_rate
                print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}.")
                print(f"Exchange rate used: 1 {base_currency} = {exchange_rate:.2f} {target_currency}")
            else:
                print("Invalid currency codes. Please check your inputs and try again.")
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except Exception as e:
            print(f"An error occurred: {e}")

currency_converter()
