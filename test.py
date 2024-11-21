from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
 
# Define options for the Android device and application
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "14.0"  # api level
options.device_name = "emulator-5554" # device id
options.app = "C:/Users/Kazi Ryan Imam/Downloads/Shudokkho_QA_Debug_1.9.6.apk"  # Path to your APK
options.no_reset = True  # Optional, prevents resetting the app on each run

# Start the driver
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)
time.sleep(5)

try:
    # Locate the registration button using XPath and click it
    registration_button = driver.find_element("xpath", '//android.widget.Button[@text="নতুন একাউন্ট তৈরি করুন"]')
    registration_button.click()
     # Wait for the element to be present using WebDriverWait
    name_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/etNameReg"]'))
    ).send_keys('Ryan')
    mobile = driver.find_element("xpath", '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/etMobileReg"]').send_keys('01952200108')
    occupation = driver.find_element("xpath", '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsServiceType"]').click()
    occupation = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="পল্লী প্রাণী সেবাকর্মী"]'))).click()
    gender = driver.find_element("xpath", '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsGender"]').click()
    gender = driver.find_element("xpath", '//android.widget.TextView[@resource-id="android:id/text1" and @text="পুরুষ"]').click()
    age = driver.find_element("xpath", '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsAge"]').click()
    age = driver.find_element("xpath", '//android.widget.TextView[@resource-id="android:id/text1" and @text="২৫-৩০ বছর"]').click()
    division = driver.find_element("xpath", '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsDivision"]').click()
    division = driver.find_element("xpath", '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Chittagong"]').click()
    district = driver.find_element("xpath", '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsDistrict"]').click()
    district = driver.find_element("xpath", '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Chittagong"]').click()
    sub_district = driver.find_element("xpath", '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsUpazila"]').click()
    sub_district = driver.find_element("xpath", '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Anowara"]').click()
    union = driver.find_element("xpath", '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsUnion"]').click()
    union = driver.find_element("xpath", '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Anwara"]').click()
    experience = driver.find_element("xpath", '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsExperience"]').click()
    experience = driver.find_element("xpath", '//android.widget.TextView[@resource-id="android:id/text1" and @text="৩ থেকে ৬ বছর"]').click()
    confirm = driver.find_element("xpath", '//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/mbSubmitReg"]').click()
    driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.mpower.android.app.lpin.crm:id/actvPosCustomDialog"))')
    term_yes = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="com.mpower.android.app.lpin.crm:id/actvPosCustomDialog"]'))).click()
    otp_code = input("Enter the OTP received: ")

    # Locate the OTP input field and enter the OTP
    otp_field = driver.find_element("id", "com.mpower.android.app.lpin.crm:id/etSMSCode")  # Replace with actual ID
    otp_field.send_keys(otp_code)
    submit = driver.find_element("xpath", '//android.widget.Button[@text="নিশ্চিত করুন"]').click()


    #print("Clicked on the registration button successfully!")
 
    # Optional: wait to see the next screen
    time.sleep(3)
 
except Exception as e:
    print(f"An error occurred: {e}")
 
finally:
    # Close the driver
    driver.quit()
    
 
