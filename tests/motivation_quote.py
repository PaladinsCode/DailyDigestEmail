# import requests
# from bs4 import BeautifulSoup
# import random

# # Define the URL of the website you want to scrape
# url = "https://www.brainyquote.com/quote_of_the_day"

# # Set a User-Agent header to mimic a real web browser
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }

# try:
#     # Send an HTTP GET request to the URL with headers
#     response = requests.get(url, headers=headers)

#     # Check the response status code
#     if response.status_code == 200:
#         # Parse the HTML content of the page
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Find the element containing the motivational quote
#         quote_element = soup.find("a", {"title": "view quote"})

#         # Extract the text of the quote
#         quote = quote_element.get_text()

#         # Print the motivational quote
#         print("Motivational Quote of the Day:")
#         print(quote)
#     else:
#         print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred: {e}")


import requests

# Define the URL
url = "https://type.fit/api/quotes"

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Print the data
        print(data)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
