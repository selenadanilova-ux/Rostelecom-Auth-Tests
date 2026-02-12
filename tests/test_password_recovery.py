import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.password_recovery_page import PasswordRecoveryPage

from settings import nonvalid_email, nonvalid_phone, nonvalid_login


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    driver.quit()


class TestNegativePasswordRecovery:

# Тест-кейс РТ-27 "Восстановление пароля по невалидному номеру телефона"

    def test_negative_password_recovery_by_nonvalid_phone(self, driver):
        page = PasswordRecoveryPage(driver)
        page.enter_phone_email_login(text=nonvalid_phone)
        page.click_reset_btn()
        assert page.get_password_recovery_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials'
                                        '?client_id=account_b2c&tab_id=EU0uMcoVReQ')

# Тест-кейс РТ-28 "Восстановление пароля по невалидному адресу электронной почты"

    def test_negative_password_recovery_by_nonvalid_email(self, driver):
        page = PasswordRecoveryPage(driver)
        page.enter_phone_email_login(text=nonvalid_email)
        page.click_reset_btn()
        assert page.get_password_recovery_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials'
                                        '?client_id=account_b2c&tab_id=EU0uMcoVReQ')

# Тест-кейс РТ-29 "Восстановление пароля по невалидному логину"

    def test_negative_password_recovery_by_nonvalid_login(self, driver):
        page = PasswordRecoveryPage(driver)
        page.enter_phone_email_login(text=nonvalid_login)
        page.click_reset_btn()
        assert page.get_password_recovery_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials'
                                        '?client_id=account_b2c&tab_id=EU0uMcoVReQ')


# Тест-кейс РТ-30 "Возврат на страницу авторизации"

    def test_positive_back_to_page_authorisation(self, driver):
        page = PasswordRecoveryPage(driver)
        page.back_to_authorisation()
        WebDriverWait(driver, 10).until(lambda d: "/login-actions/authenticate" in d.current_url)
        assert "/auth/realms/b2c/" in driver.current_url