import requests

url = "http://www.googllllye.com"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("HTTP Response:")
    print(response.status_code)  # Print the content of the response
else:
    print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
