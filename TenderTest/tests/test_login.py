import time
from config.configure import configure_driver
from config.base_url import BASE_URL
from pages.login import LoginPage

driver = configure_driver()


login = LoginPage(driver)
login.open()
time.sleep(2)
login.enter_username("naveensiki2003@gmail.com")
login.enter_password("Rishitha@2003")
login.click_login()
time.sleep(4)

error = login.get_error_message()
if "Invalid username or password" in error:
    print("❌ Test failed: error message displayed as expected.")
else:
    print("✅ Test passed: No error message shown.")

driver.quit()
