import requests

API_KEY = "wB9ZaKoJ1uBP3s216r4jjoD0YHcOjRAZ"

def get_supported_currencies():
    url = "https://api.apilayer.com/currency_data/list"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if "currencies" in data:
            return data["currencies"]
        else:
            print("Error: Currency list not found.")
            return None
    else:
        print(f"Error: Unable to fetch data, Status code: {response.status_code}")
        return None

def currency_converter(from_currency, to_currency, amount):
    url = f"https://api.apilayer.com/currency_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if "result" in data:
            return data["result"]
        else:
            print("Error: Conversion data not found.")
            return None
    else:
        print(f"Error: Unable to fetch data, Status code: {response.status_code}")
        return None


show_currencies = input("Do you want to see the list of supported currencies? (y/n): ").strip().lower()
supported_currencies = get_supported_currencies() 


if show_currencies == "y":
    print("Supported Currencies:")
    for prefix, name in supported_currencies.items():
        print(f"{prefix}: {name}")
else:
    None      

# Verify currency input
while True:
    from_currency = input("Enter the currency you want to convert from: ").upper()
    to_currency = input("Enter the currency you want to convert to: ").upper()
    
    # Validation of currencies
    if (from_currency not in supported_currencies or to_currency not in supported_currencies):
        print("One or both of the currencies you entered are invalid.")
        again = input("Do you want to see the list of supported currencies? (y/n): ").strip().lower()
        if again == "y":
            print("Supported Currencies:")
            for prefix, name in supported_currencies.items():
                print(f"{prefix}: {name}")
        continue  

    
    while True:
        try:
            amount = float(input("Enter the amount you want to convert: "))
            break  
        except ValueError:
            print("Invalid input! Please enter a numeric value for the amount.")

    
    result = currency_converter(from_currency, to_currency, amount)
    if result:
        print(f"{amount} {from_currency} = {result} {to_currency}")
    break  
