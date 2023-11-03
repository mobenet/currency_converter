import requests
import time 

# Define API URL to obatin change rates
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

# Cache to store rates and last update time
CACHE = {
    'rates': None,
    'last_updated': None
}
# Cache duration in seconds; 1 hour
CACHE_DURATION = 3600


# Method to obtain rate changes
def get_exchange_rates():
    current_time = time.time(); 
    print("hola")
    # Verify if rates in cache and if still valid
    if CACHE['rates'] and (current_time - CACHE['last_updated'] < CACHE_DURATION):
        print("Using cached rates.")
        return CACHE['rates']
    else: 
        response = requests.get(API_URL)
        # Verify if succes
        response.raise_for_status()
        rates = response.json().get('rates', {})
        # Update cache 
        CACHE['rates'] = rates
        CACHE['last_updated'] = current_time
        print("Updated rates from API.")
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