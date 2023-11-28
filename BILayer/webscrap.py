from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time

def save_webpage_with_selenium(url, output_filename):
    try:
        # Set up options for a headless Chrome browser
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=chrome_options)

        # Navigate to the webpage
        driver.get(url)

        # Wait for a moment (optional, adjust as needed)
        time.sleep(2)

        # Save the HTML content after the page has fully loaded
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(driver.page_source)

        print(f"The HTML code has been saved to {output_filename}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the browser window
        driver.quit()

def extract_rate_from_html(file_content):
    try:
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(file_content, 'html.parser')

        # Find the rate element
        rate_element = soup.find('div', class_='variableRate')

        # Extract and print the rate
        if rate_element:
            rate_fixed = rate_element.get_text().strip()
            print(f"Fixed Rate: {rate_fixed}")
        else:
            print("Rate element not found in the HTML.")

    except Exception as e:
        print(f"Error extracting rate: {e}")

if __name__ == "__main__":
    # Replace 'https://example.com' with the URL of the webpage you want to download
    url = 'https://www.discover.com/student-loans/'

    # Replace 'output.html' with the desired filename for the saved content
    output_filename = 'C:\\Users\\vinmayp\\Desktop\\Resources\\output.html'

    # Call the function to open the webpage with a headless browser and save the HTML code
    save_webpage_with_selenium(url, output_filename)

    # Read the HTML content from the saved file
    with open(output_filename, 'r', encoding='utf-8') as file:
        file_content = file.read()

    # Extract and print the rate from the HTML content
    extract_rate_from_html(file_content)
