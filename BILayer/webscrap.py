from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def wait_for_page_load(driver, timeout=10):
    # Wait for the page to load by waiting for the presence of the body tag
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )

def save_webpage_after_loading(url, output_filename):
    try:
        # Initialize the Chrome driver
        driver = webdriver.Chrome()

        # Navigate to the webpage
        driver.get(url)

        # Wait for the page to load (wait for the body tag to be present)
        wait_for_page_load(driver)

        # Wait for additional time (adjust as needed) to ensure dynamic content has loaded
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

if __name__ == "__main__":
    # Replace 'https://example.com' with the URL of the webpage you want to open and save
    url = 'https://www.discover.com/student-loans/'

    # Replace 'output.html' with the desired filename for the saved content
    output_filename = 'C:\\Users\\vinmayp\\Desktop\\Resources\\output.html'

    # Call the function to open the webpage, wait for it to load, and then save the HTML code
    save_webpage_after_loading(url, output_filename)

    with open(output_filename, 'r', encoding='utf-8') as file:
        file_content = file.read()

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(file_content, 'html.parser')
    rate_element = soup.find('div', class_='variableRate')
    rate_fixed = rate_element.get_text().strip()
    print(rate_fixed)
