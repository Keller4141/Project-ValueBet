# Initialize your Python environment
# Import required libraries
import requests

# Define your API key
api_key = "wIr5YmTQe91HAXTKloYgdXk5klZtkBpoeS6MUCa3rhcUrqLxBMWd1p9oiGLd"

# Define the API endpoint URL
base_url = "https://api.sportmonks.com/v3/football"
endpoint = "/leagues"#define the endpoint URL here
include = "" #list your includes here
endpoint_url = f"{base_url}{endpoint}?include={include}"

# Include API key in request headers
headers = {"Authorization": api_key}

# Send a GET request to the Sportmonks API endpoint
response = requests.get(endpoint_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)


else:
    print("Failed to retrieve data. Status code:", response.status_code)