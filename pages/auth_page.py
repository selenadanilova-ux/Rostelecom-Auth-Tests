from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self._url = url
        self._driver = driver

    def get_current_url(self):
        return self._driver.current_url

    def get_page(self, url):
        return self._driver.get(url)


class AuthPage(BasePage):
    def __init__(self, driver, url='https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                   '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                   '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef'):
        super().__init__(driver, url)
        self.wait = WebDriverWait(driver,20)
        self._configurate()

    def get_auth_page(self):
        return self._url

    def _configurate(self):
        self.get_page(self._url)

    def enter_phone_email_login(self, text):
        element = self.wait.until(EC.visibility_of_element_located((By.ID, "username")))
        element.send_keys(text)

    def enter_password(self, text):
        element = self.wait.until(EC.visibility_of_element_located((By.ID, "password")))
        element.send_keys(text)

    def click_login_btn(self):
        element = self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "rt-btn.rt-btn--orange.rt-btn--medium.rt-btn--rounded.login-form__login-btn")
        ))
        element.click()

    def click_forgot_password_btn(self):
        element = self.wait.until(EC.element_to_be_clickable((By.ID, "forgot_password")))
        element.click()
