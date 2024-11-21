from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "14.0"  # Your device's API level
options.device_name = "emulator-5554"  # Your device ID
options.app = "C:/Users/Kazi Ryan Imam/Downloads/Shudokkho_QA_Debug_1.9.6.apk" # Path to your APK
options.no_reset = True  # Ensures app data isn't reset
# options.full_reset = False  # Ensures app isn't reinstalled

driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)

# Step 1: Read the CSV file
csv_file_path = "service_data.csv"
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(f"Processing service for: {row['Farmer Name']}")

instant_service = driver.find_element("xpath", '//android.widget.FrameLayout[@resource-id="com.mpower.android.app.lpin.crm:id/cvTreatment"]/android.widget.LinearLayout')
instant_service.click()

type = driver.find_element("xpath", '(//android.widget.TextView[@resource-id="android:id/text1"])[1]')
type.click()

sickness = driver.find_element("xpath", '//android.widget.TextView[@resource-id="android:id/text1" and @text="অসুস্থতার সেবা"]')
sickness.click()

name = driver.find_element("xpath", '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvNameTreatment"]').send_keys(row["Farmer Name"])
mobile = driver.find_element("xpath", '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvMobileTreatment"]').send_keys(row["Mobile"])
adress = driver.find_element("xpath", '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvAddressTreatment"]').send_keys('11 test avenue')
animal_type = driver.find_element("xpath", '(//android.widget.TextView[@resource-id="android:id/text1"])[2]').click()
animal = driver.find_element("xpath", '//android.widget.TextView[@resource-id="android:id/text1" and @text="গরু"]').click()
animal_secondary = driver.find_element("xpath", '(//android.widget.TextView[@resource-id="android:id/text1"])[3]').click()
animal_sec_type = driver.find_element("xpath", '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="ষাঁড়"]').click()
med = driver.find_element("xpath", '//android.widget.ImageButton[@resource-id="com.mpower.android.app.lpin.crm:id/fabMedicine"]').click()
disease_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsDisease"]'))).click()
disease = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="অপুষ্টি"]'))).click()

med_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '(//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsMedicines"])[1]'))).click()

med_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="Liq. A Zinc vet"]'))).click()
med_submit = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@resource-id="com.mpower.android.app.lpin.crm:id/acivSubmitDialog"]'))).click()

driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.mpower.android.app.lpin.crm:id/mbSubmitMedicine"))')

time.sleep(2)

med_confirm = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/mbSubmitMedicine"]'))
)
if med_confirm.is_enabled():
    med_confirm.click()
else:
    print("Button is not enabled.")

ad_close = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageView[@resource-id="com.mpower.android.app.lpin.crm:id/btnDialogClose"]'))
).click()

nextday = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/acetNextDayTreatment"]'))
).send_keys("1")

follow_time = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsMidDayNewVisit"]'))
).click()
follow_pm = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="PM"]'))
).click()
collection = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/mbCollectionTreatment"]'))
).click()
med_price = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/acetMed"]'))
).send_keys("100")
fee_value = row["Fee"]  # Get the fee value from the CSV
fee = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f'(//android.widget.RadioButton[@text="{fee_value}"])[1]'))
).click()
payment_value = row["Payment"]  # Get the fee value from the CSV
payment = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f'(//android.widget.RadioButton[@text="{payment_value}"])[2]'))
).click()

submit_treatment = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/mbSubmitTreatment"]'))
).click()
no_message = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@resource-id="com.mpower.android.app.lpin.crm:id/actvNegCustomDialog"]'))
).click()
time.sleep(2)
service_save = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/mbSubmitTreatment"]'))
).click()
adress = driver.find_element("xpath", '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvAddressTreatment"]').send_keys('new park')
service_save = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/mbSubmitTreatment"]'))
).click()
no_message = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@resource-id="com.mpower.android.app.lpin.crm:id/actvNegCustomDialog"]'))
).click()

# Save data to CSV
# service_data = {
#     "Farmer Name": "Rahim Mia",
#     "Mobile": "01234121212",
#     "Fee": "300",
#     "Payment": "200",
#     "Due": "100"
#     }
#     "Address": "11 test avenue",
#     "Service Type": "অসুস্থতার সেবা",
#     "Animal": "গরু",
#     "Animal Type": "ষাঁড়",
#     "Disease": "অপুষ্টি",
#     "Medicine": "Liq. A Zinc vet",
#     "Follow-up Time": "1 Day, PM",
#     "Medicine Cost": "100",

# csv_file_path = "service_data.csv"
# headers = service_data.keys()

# with open(csv_file_path, mode="a", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(headers)  # Write headers
#     writer.writerow(service_data.values())  # Write row data

# print(f"CSV file created: {csv_file_path}")

# Quit driver
driver.quit()












 
    





