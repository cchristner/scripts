from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager  # Optional for automatic ChromeDriver management


"""
Issues:
> not sure that it's inserting the zip that I want data for
> not pulling correct data, regardless of zip
"""



# Set up the Selenium WebDriver using the Service object
service = ChromeService(executable_path=ChromeDriverManager().install())  # This line uses webdriver_manager to auto-install the ChromeDriver

driver = webdriver.Chrome(service=service)

# Open the website
driver.get('https://www.dtnpf.com/agriculture/web/ag/markets/local-grain-bids')  

# Wait for the input field to be present
wait = WebDriverWait(driver, 10)
input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.js-simpleLocationView-input.input.input_medium.inputAddOn-input")))

# Enter the required data
input_field.send_keys('46914')
input_field.send_keys(Keys.RETURN)

# Optionally, wait for the page to load the results
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'hdg.hdg_4.hdg_bold')))

# Extract the data from the resulting page
results = driver.find_elements(By.CLASS_NAME, 'hdg.hdg_4.hdg_bold')

for result in results:
    print(result.text)

# Close the browser
driver.quit()