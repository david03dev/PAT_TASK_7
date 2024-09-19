import requests

class CountryInfo:
    def __init__(self, url):
        self.url = url

    # Method to fetch all JSON data from the URL
    def fetch_api_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()  
        else:
            return "ERROR: Unable to fetch data"

    # Method to display the name of countries, currencies, and currency symbols
    def display_countries_and_currencies(self):
        data = self.fetch_api_data()
        if isinstance(data, str):  
            print(data)
        else:
            for country in data:
                name = country.get('name', {}).get('common', 'N/A')
                currencies = country.get('currencies', {})
                for currency_code, currency_info in currencies.items():
                    currency_name = currency_info.get('name', 'N/A')
                    currency_symbol = currency_info.get('symbol', 'N/A')
                    print(f"Country: {name}, Currency: {currency_name}, Symbol: {currency_symbol}")

    # Method to display countries with DOLLAR as currency
    def display_dollar_countries(self):
        data = self.fetch_api_data()  
        if isinstance(data, str):    
            print(data)               
        else:                        
            for country in data:      
                name = country.get('name', {}).get('common', 'N/A') 
                currencies = country.get('currencies', {})           
                for currency_info in currencies.values():            
                    if currency_info.get('symbol', '') == '$':
                        name = country.get('name', {}).get('common', 'Unknown Country')
                        print(name)


    # Method to display countries with EURO as currency
    def display_euro_countries(self):
        data = self.fetch_api_data()
        if isinstance(data, str):
            print(data)
        else:
            for country in data:
                name = country.get('name', {}).get('common', 'N/A')
                currencies = country.get('currencies', {})
                for currency_info in currencies.values():
                    if 'Euro' in currency_info.get('name', ''):
                        name = country.get('name', {}).get('common', 'Unknown Country')
                        print(name)

# Example usage
url = "https://restcountries.com/v3.1/all"
country_info = CountryInfo(url)

# Fetch and display countries and currencies
print("Countries and their currencies:")
country_info.display_countries_and_currencies()

# Display countries using Dollar as currency
print("\nCountries using Dollar as currency:")
country_info.display_dollar_countries()

# Display countries using Euro as currency
print("\nCountries using Euro as currency:")
country_info.display_euro_countries()
