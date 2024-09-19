import requests

class BreweryInfo:
    def __init__(self, url):
        self.url = url

    # Method to fetch data from the API
    def fetch_api_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            return "ERROR-404"

    # List the names of all breweries in Alaska, Maine, and New York
    def list_breweries_in_states(self):
        data = self.fetch_api_data()
        if isinstance(data, str):
            print(data)
        else:
            states = ['Alaska', 'Maine', 'New York']
            for state in states:
                print(f"\nBreweries in {state}:")
                for brewery in data:
                    if brewery.get('state') == state:
                        print(f"- {brewery['name']}")

    # Count the breweries in Alaska, Maine, and New York
    def count_breweries_in_states(self):
        data = self.fetch_api_data()
        if isinstance(data, str):
            print(data)
        else:
            state_counts = {'Alaska': 0, 'Maine': 0, 'New York': 0}
            for brewery in data:
                state = brewery.get('state')
                if state in state_counts:
                    state_counts[state] += 1
            
            print("\nNumber of breweries in each state:")
            for state, count in state_counts.items():
                print(f"{state}: {count} breweries")

    # Count the types of breweries in each city in the specified states
    def count_brewery_types_by_city(self):
        data = self.fetch_api_data()
        if isinstance(data, str):
            print(data)
        else:
            city_brewery_types = {'Alaska': {}, 'Maine': {}, 'New York': {}}
            
            for brewery in data:
                state = brewery.get('state')
                if state in city_brewery_types:
                    city = brewery.get('city')
                    brewery_type = brewery.get('brewery_type')
                    
                    if city not in city_brewery_types[state]:
                        city_brewery_types[state][city] = {}
                    
                    if brewery_type not in city_brewery_types[state][city]:
                        city_brewery_types[state][city][brewery_type] = 0
                    
                    city_brewery_types[state][city][brewery_type] += 1
            
            print("\nBrewery types count by city in each state:")
            for state, cities in city_brewery_types.items():
                print(f"\nState: {state}")
                for city, types in cities.items():
                    print(f"City: {city}")
                    for brewery_type, count in types.items():
                        print(f"  {brewery_type}: {count}")

    # Count and list breweries with websites in the specified states
    def count_breweries_with_websites(self):
        data = self.fetch_api_data()
        if isinstance(data, str):
            print(data)
        else:
            state_website_counts = {'Alaska': 0, 'Maine': 0, 'New York': 0}
            print("\nBreweries with websites:")
            for brewery in data:
                state = brewery.get('state')
                website_url = brewery.get('website_url')
                if state in state_website_counts and website_url:
                    state_website_counts[state] += 1
                    print(f"- {brewery['name']} ({state}), Website: {website_url}")
            
            print("\nCount of breweries with websites in each state:")
            for state, count in state_website_counts.items():
                print(f"{state}: {count} breweries with websites")

# Main execution
url = "https://api.openbrewerydb.org/breweries"
brewery_info = BreweryInfo(url)

# List the breweries in Alaska, Maine, and New York
brewery_info.list_breweries_in_states()

# Count the breweries in Alaska, Maine, and New York
brewery_info.count_breweries_in_states()

# Count the types of breweries by city in Alaska, Maine, and New York
brewery_info.count_brewery_types_by_city()

# Count and list breweries with websites in Alaska, Maine, and New York
brewery_info.count_breweries_with_websites()
