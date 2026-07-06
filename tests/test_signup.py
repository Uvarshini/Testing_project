from utilities.driver_factory import get_driver
from pages.signup_page import SignupPage


def test_signup_page_load():

    driver = get_driver()

    driver.get("https://tichi-app-webapp-stage.web.app")

    assert "Tichi" in driver.title

    driver.quit()