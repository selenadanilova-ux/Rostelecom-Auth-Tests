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


class PasswordRecoveryPage(BasePage):
    def __init__(self, driver, url='https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials'
                                   '?client_id=account_b2c&tab_id=EU0uMcoVReQ'):
        super().__init__(driver, url)
        self.wait = WebDriverWait(driver,20)
        self._configurate()

    def get_password_recovery_page(self):
        return self._url

    def _configurate(self):
        self.get_page(self._url)

    def enter_phone_email_login(self, text):
        element = self.wait.until(EC.visibility_of_element_located((By.ID, "username")))
        element.send_keys(text)

    def click_reset_btn(self):
        element = self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "rt-btn.rt-btn--orange.rt-btn--medium.rt-btn--rounded.reset-form__reset-btn")
        ))
        element.click()

    def back_to_authorisation(self):
        element = self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "rt-btn.rt-btn--orange.rt-btn--medium.rt-btn--rounded.rt-btn--transparent.reset-form__back-btn")
        ))
        element.click()
