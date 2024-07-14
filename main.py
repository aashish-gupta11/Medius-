import os
import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Set the path to the Chrome WebDriver
chrome_driver_path = os.path.join(os.getcwd(), r"C:\Users\aashi\OneDrive - somaiya.edu\Desktop\chromedriver-win64\chromedriver.exe")

# Setup Selenium WebDriver
chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

chrome_service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Fill the Google form
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform')
time.sleep(3)  # Wait for the page to load

# Fill in the form fields
full_name_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
contact_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
email_id_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
pin_code_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
dob_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
gender_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
code_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')

# Enter the data
full_name_field.send_keys('Aashish Gupta')
contact_field.send_keys('9405182765')
email_id_field.send_keys('aashish.gupta@somaiya.edu')
address_field.send_keys('147, Shivdarshan Bunglow, Shivgiri Colony, College Road, Nashik')
pin_code_field.send_keys('422005')
dob_field.send_keys('11/11/2003')
gender_field.send_keys('Male')
code_field.send_keys('GNFPYC')

# Submit the form
submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
submit_button.click()

time.sleep(3)  # Wait for the submission to complete

# Capture the screenshot
screenshot_path = os.path.join(os.getcwd(), 'screenshot.png')
driver.save_screenshot(screenshot_path)

driver.quit()

# Send the email with the screenshot
subject = 'Python (Selenium) Assignment - Aashish Gupta'
body = 'Please find the attached screenshot of the Google form submission confirmation.'
from_email = 'aashish.gupta@somaiya.edu'
to_email = 'tech@themedius.ai'
cc_email = 'hr@themedius.ai'
password = 'tqie zour cuic pkro'

# Create the email message
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Cc'] = cc_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

# Attach the screenshot
attachment = open(screenshot_path, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(screenshot_path)}')
msg.attach(part)

# Send the email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, [to_email, cc_email], msg.as_string())
    server.quit()
    print("Email sent successfully")
except Exception as e:
    print(f"Error sending email: {e}")
