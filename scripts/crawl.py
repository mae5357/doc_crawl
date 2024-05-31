import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = 'https://docs.pydantic.dev/latest/concepts/models/'
response = requests.get(url)

# Parse the webpage content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the text from the webpage
page_text = soup.get_text()

print(page_text)


