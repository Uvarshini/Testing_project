import pytest
from pages.login_page import LoginPage
from utilities.driver_factory import get_driver


def test_invalid_email():

    driver = get_driver()

    driver.get("https://tichi-app-webapp-stage.web.app/login")

    login = LoginPage(driver)

    login.enter_email("abc")
    login.click_continue()

    assert "login" in driver.current_url

    driver.quit()


def test_empty_email():

    driver = get_driver()

    driver.get("https://tichi-app-webapp-stage.web.app/login")

    assert "Tichi" in driver.title

    driver.quit()