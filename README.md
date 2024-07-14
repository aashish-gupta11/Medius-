Python (Selenium) Assignment
This repository contains a Python script designed to automate the process of filling out a Google form, capturing a screenshot of the confirmation page, and sending it via email using SMTP.

Files:
main.py: Python script that performs the following actions:

Uses Selenium WebDriver to fill out the specified Google form with predefined data.
Captures a screenshot of the confirmation page.
Sends an email with the captured screenshot attached using SMTP.
requirements.txt: Lists the Python packages required to run the script. Install them using pip install -r requirements.txt.

Instructions:
1. Setup:
Ensure Python 3.x and pip are installed on your system.
Install required packages using pip install -r requirements.txt.

2. Configuration:
Edit main.py to customize form data (e.g., name, contact, email, address, etc.).
Replace placeholders for chrome_driver_path, from_email, password, to_email, and cc_email with appropriate values.

3. Execution:
Run python main.py to execute the script.
The script will launch a headless Chrome browser, fill out the form, capture a screenshot, and attempt to send an email with the screenshot attached.
