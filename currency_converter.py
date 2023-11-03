import requests

# Define API URL to obatin change rates
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

# Method to obtain rate changes
def get_exchange_rates():
    response = requests.get(API_URL)
    # Verify if succes
    response.raise_for_status()
    print(f"response: {response}")
    rates = response.json().get('rates', {})
    return rates

# Method to convert 
def convert_currency(amount, from_currency, to_currency, exchange_rates):
    # Check if currencies are correct
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return None
    
    # Convert to USD first
    amount_in_usd = amount / exchange_rates[from_currency]

    # Convert from USD to to_currency
    amount_in_target = amount_in_usd * exchange_rates[to_currency]

    return amount_in_target

def main():
    rates = get_exchange_rates()
    print("Welcome to the Currency Converter!")

    # Obtain the amount to convert
    amount = float(input("Enter amount to convert..."))

    # Obtain the origin and destiny currencies
    from_currency = input("Enter the currency you want to convert from (3-letter code): ").upper()
    to_currency = input("Enter the currency you want to convert to (3-letter code): ").upper()

    result = convert_currency(amount, from_currency, to_currency, rates)

    if result: 
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
    else:
        print("Error: Invalid currency code")

if __name__ == "__main__":
    main()