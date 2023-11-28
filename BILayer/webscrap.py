import requests
from bs4 import BeautifulSoup

def get_webpage_text(url):
    try:
        # Make a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract text from the parsed HTML
            text_content = soup.get_text()
            
            return text_content
        else:
            print(f"Error: Unable to fetch the webpage. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'https://example.com' with the URL of the webpage you want to fetch
    url = 'https://example.com'
    
    # Call the function and print the text content
    webpage_text = get_webpage_text(url)
    if webpage_text:
        print(webpage_text)
