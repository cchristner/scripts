from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # You may need to download the ChromeDriver

# Open the website
driver.get('https://www.dtnpf.com/agriculture/web/ag/markets/local-grain-bids')  # Replace with the website URL

# Find the input field and enter the required data
input_field = driver.find_element(By.ID, 'js-simpleLocationView-input input input_medium inputAddOn-input')  # Replace with the actual element ID or use other locators
input_field.send_keys('46914')  # Replace with the actual input data

# Submit the form or trigger the required action
input_field.send_keys(Keys.RETURN)

# Optionally, wait for the page to load the results
driver.implicitly_wait(10)  # Adjust the wait time if needed

# Extract the data from the resulting page
results = driver.find_elements(By.CLASS_NAME, 'hdg hdg_4 hdg_bold')  # Replace with the actual class name or use other locators

for result in results:
    print(result.text)

# Close the browser
driver.quit()