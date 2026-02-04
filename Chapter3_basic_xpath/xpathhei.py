###Tutorial xpath

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selemium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os
import time

#optional, setup chtrome
chrome_options = Options()

#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialize browser
file_path = "file://" + os.path.abspath("main.html")
driver = webdriver.Chrome(options=chrome_options)
driver.get(file_path)

print("=" * 80)
print(XPATH TUTORIAL - EXECUTING ALL EXAMPLES")
print("=" * 80)
print(f"Testing URL : {file_path}\n")

def test_xpath(xpath, description, expect_multiple=False):
# Test an xpath expression and print results
try:
    if expect_multiple:
        elements = driver.find_elements(By.XPATH, xpath)
        count = len(elements)
        status = "✓ FOUND" if count > 0 else "✗ NOT FOUND"
        print(f"{status}")
        