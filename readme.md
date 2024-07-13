WhatsApp Text Automation Script
Overview
This Python script automates sending messages on WhatsApp Web using Selenium. It logs into WhatsApp Web using an existing Chrome session with a specified profile path and sends messages to a targeted group or contact multiple times.

Features
Automatically opens WhatsApp Web using an existing Chrome profile.
Checks if already logged into WhatsApp Web; prompts to scan the QR code if not.
Sends a specified message to a target group or contact with the option to tag a specific person.
Requirements
Python 3.x
Selenium
Chrome web browser
ChromeDriver (managed automatically by webdriver_manager)
Installation and Setup
Ensure Python 3.x is installed.
Install the required Python packages:
Copy code
pip install selenium webdriver_manager
Replace chrome_profile_path in the script with your Chrome profile directory path if different.
Run the script:
Copy code
python text_automation.py
Usage
Open the script in your preferred Python environment.
It will automatically open WhatsApp Web using your existing Chrome profile.
If not logged in, it will prompt you to scan the QR code using your mobile device.
Specify the target group or contact name (target_group) and the message (message) to send.
Optionally, you can tag a specific person in the group by modifying the message format (message_box.send_keys(f"@{person} {message}")).
It sends the message multiple times (num_times) with a delay between messages.
Note: Ensure that your Chrome browser is updated and the WebDriver is compatible with your browser version. The script manages WebDriver automatically using webdriver_manager.