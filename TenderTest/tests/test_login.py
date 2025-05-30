import time
from config.configure import configure_driver
from config.base_url import BASE_URL
from pages.login import LoginPage

driver = configure_driver()
driver.get(BASE_URL)


login = LoginPage(driver)


login.enter_username("")
login.enter_password("")
login.click_login()
time.sleep(4)

error = login.get_error_message()
if "Invalid username or password" in error:
    print("❌ Test failed: error message displayed as expected.")
else:
    print("✅ Test passed: No error message shown.")

driver.quit()
