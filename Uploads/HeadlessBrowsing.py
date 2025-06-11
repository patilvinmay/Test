import os, shutil
from playwright.sync_api import sync_playwright
import time

def empty_directory(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # Remove file or symlink
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Remove subdirectory
        except Exception as e:
            print(f'❌ Failed to delete {file_path}. Reason: {e}')
            exit(1)

def search_bing(query):
    print("🌐 Launching Bing search for " + query + "...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Open Bing homepage
        page.goto("https://www.bing.com")

        # Wait briefly to ensure page is fully loaded and search box is focused
        time.sleep(2)

        # Type the query directly (search box is already focused by default)
        page.keyboard.type(query, delay=100)  # Typing with a slight delay to mimic human behavior
        page.keyboard.press("Enter")

        # Wait for results to load
        page.wait_for_selector("#b_results", timeout=10000)
        time.sleep(2)

        # Take a screenshot of the result
        image_path = os.path.join("RuntimeScreenShots", "bing_result.png")
        page.screenshot(path=image_path, full_page=True)
        print("✅ Search result screenshot saved at: ", image_path)

        browser.close()

    return image_path
