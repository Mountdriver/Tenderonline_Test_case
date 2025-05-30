from selenium.webdriver.common.by import By
from pages.base_pg import Base_Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID,"email"))
        )
        username_field.click()
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[3]/div[2]/div/div/div/div[2]/form/div[2]/button"))
        )
        login_button.click()

    def get_error_message(self):
        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[3]/div[2]/div/div/div/div[2]/form/div[1]/p"))
            )
            return error_message.text
        except Exception as e:
            return None