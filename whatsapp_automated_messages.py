import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Path to your Chrome profile directory
chrome_profile_path = "C:\\Users\\kaush\\AppData\\Local\\Google\\Chrome\\User Data\\Default"  # Replace with your profile path

def is_logged_in(driver):
    try:
        driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        return True
    except NoSuchElementException:
        return False

# Initialize Chrome driver with webdriver_manager
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={chrome_profile_path}")

driver = webdriver.Chrome(service=service, options=options)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')
time.sleep(10)  # Give some time to load

if not is_logged_in(driver):
    print("Please scan the QR code to log in to WhatsApp Web.")
    time.sleep(20)  # Wait for the user to scan the QR code and log in

# Check again if logged in
if not is_logged_in(driver):
    print("Not logged in. Exiting.")
    driver.quit()
    exit()

print("Logged in successfully.")

# Define the target group name, message, and number of times to send
target_group = "name of contact"  # Replace with the name of your WhatsApp group
message = "message to be sent"
 
num_times = 10 #number of times thgis message has to be sent

# Search for the target group
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
time.sleep(1)
search_box.send_keys(target_group)
time.sleep(2)  # Wait for search results to appear
search_box.send_keys(Keys.ENTER)

# Find the message input box
message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')

# Send the message multiple times with tagging
for _ in range(num_times):
    message_box.send_keys(f" {message}")
    time.sleep(2)  # Wait for the dropdown to appear and select the contact
    message_box.send_keys(Keys.ENTER)  # Press Enter to send the message
    time.sleep(1)  # Short delay between messages

# Close the browser after sending messages
time.sleep(5)
driver.quit()
