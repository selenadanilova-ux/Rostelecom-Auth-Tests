import pytest

from selenium import webdriver

from pages.auth_page import AuthPage

from settings import valid_email, valid_password, valid_phone, valid_login

from settings import (nonvalid_password, nonvalid_email,
                      nonvalid_phone, nonvalid_login)

from settings import empty_password, empty_phone, empty_email, empty_login


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    driver.quit()



class TestAuthPositivePhone:

# Тест-кейс РТ-04 "Авторизация по валиному номеру телефона и валидному паролю"

    def test_positive_authorisation_by_valid_phone_and_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=valid_phone)
        page.enter_password(text=valid_password)
        page.click_login_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')


class TestAuthPositiveEmail:

# Тест-кейс РТ-10 "Авторизация по валиному адресу электронной почты и валидному паролю"

    def test_positive_authorisation_by_valid_email_and_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=valid_email)
        page.enter_password(text=valid_password)
        page.click_login_btn()
        assert (page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef') !=
            'https://b2c.passport.rt.ru/account_b2c/page#/')

class TestAuthPositiveLogin:

# Тест-кейс РТ-16 "Авторизация по валиному логину и валидному паролю"

    def test_positive_authorisation_by_valid_login_and_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=valid_login)
        page.enter_password(text=valid_password)
        page.click_login_btn()
        assert page.get_auth_page() == (
                'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')

class TestAuthNegative:

# Тест-кейс РТ-05 "Авторизация по пустым значениям номера телефона и пароля"

    def test_negative_authorisation_by_empty_phone_and_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=empty_phone)
        page.enter_password(text=empty_password)
        page.click_login_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')

# Тест-кейс РТ-06 "Авторизация по невалиному номеру телефона и валидному паролю"

    def test_negative_authorisation_by_nonvalid_phone_and_valid_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=nonvalid_phone)
        page.enter_password(text=valid_password)
        page.click_login_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')

# Тест-кейс РТ-07 "Авторизация по валиному номеру телефона и невалидному паролю"

    def test_negative_authorisation_by_valid_phone_and_nonvalid_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=valid_phone)
        page.enter_password(text=nonvalid_password)
        page.click_login_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')

# Тест-кейс РТ-08 "Авторизация по валиному номеру телефона и пустому полю пароля"

    def test_negative_authorisation_by_valid_phone_and_empty_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=valid_phone)
        page.enter_password(text=empty_password)
        page.click_login_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')

# Тест-кейс РТ-09 "Авторизация по пустому полю номера телефона и валидному паролю"

    def test_negative_authorisation_by_empty_phone_and_valid_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=empty_phone)
        page.enter_password(text=valid_password)
        page.click_login_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')


# Тест-кейс РТ-11 "Авторизация по пустым значениям адреса электронной почты и пароля"

    def test_negative_authorisation_by_empty_email_and_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=empty_phone)
        page.enter_password(text=empty_password)
        page.click_login_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')

# Тест-кейс РТ-12 "Авторизация по невалиному адресу электронной почты и валидному паролю"

    def test_negative_authorisation_by_nonvalid_email_and_valid_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=nonvalid_phone)
        page.enter_password(text=valid_password)
        page.click_login_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')

# Тест-кейс РТ-13 "Авторизация по валиному адресу электронной почты и невалидному паролю"

    def test_negative_authorisation_by_valid_email_and_nonvalid_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=valid_email)
        page.enter_password(text=nonvalid_password)
        page.click_login_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')

# Тест-кейс РТ-14 "Авторизация по валиному адресу электронной почты и пустому полю пароля"

    def test_negative_authorisation_by_valid_email_and_empty_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=valid_email)
        page.enter_password(text=empty_password)
        page.click_login_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')

# Тест-кейс РТ-15 "Авторизация по пустому полю электронной почты и валидному паролю"

    def test_negative_authorisation_by_empty_email_and_valid_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=empty_phone)
        page.enter_password(text=valid_password)
        page.click_login_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')

# Тест-кейс РТ-17 "Авторизация по пустым значениям логина и пароля"

    def test_negative_authorisation_by_empty_login_and_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=empty_phone)
        page.enter_password(text=empty_password)
        page.click_login_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')

# Тест-кейс РТ-18 "Авторизация по невалиному логину и валидному паролю"

    def test_negative_authorisation_by_nonvalid_login_and_valid_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=nonvalid_login)
        page.enter_password(text=valid_password)
        page.click_login_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')

# Тест-кейс РТ-19 "Авторизация по валиному логину и невалидному паролю"

    def test_negative_authorisation_by_valid_login_and_nonvalid_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=valid_login)
        page.enter_password(text=nonvalid_password)
        page.click_login_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')

# Тест-кейс РТ-20 "Авторизация по валиному логину и пустому полю пароля"

    def test_negative_authorisation_by_valid_login_and_empty_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=valid_login)
        page.enter_password(text=empty_password)
        page.click_login_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')

# Тест-кейс РТ-21 "Авторизация по пустому полю логин и валидному паролю"

    def test_negative_authorisation_by_empty_login_and_valid_password(self, driver):
        page = AuthPage(driver)
        page.enter_phone_email_login(text=empty_phone)
        page.enter_password(text=valid_password)
        page.click_login_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')

class TestTransitionPagePasswordRecovery:

# Тест-кейс РТ-22 "Переход на страницу восстановления пароля"

    def test_positive_transition_page_password_recovery(self, driver):
        page = AuthPage(driver)
        page.click_forgot_password_btn()
        assert page.get_auth_page() == ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                                    '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login'
                                    '&response_type=code&scope=openid&state=57fef103-9d17-4a55-a7b1-923a112b54ef')





