from appium import webdriver
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "14.0"  # Your device's API level
options.device_name = "emulator-5554"  # Your device ID
options.app = "C:/Users/Kazi Ryan Imam/Downloads/Shudokkho_QA_Debug_1.9.6.apk" # Path to your APK
options.no_reset = True  # Ensures app data isn't reset
# options.full_reset = False  # Ensures app isn't reinstalled

driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)

mobile = driver.find_element("xpath", '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/etUserId"]').send_keys('01952200108')

login_button = driver.find_element("xpath", '//android.widget.Button[@text="লগ ইন"]')
login_button.click()

otp_code = input("Enter the OTP received: ")

# Locate the OTP input field and enter the OTP
otp_field = driver.find_element("id", "com.mpower.android.app.lpin.crm:id/etSMSCode")  # Replace with actual ID
otp_field.send_keys(otp_code)
submit = driver.find_element("xpath", '//android.widget.Button[@text="নিশ্চিত করুন"]').click()

