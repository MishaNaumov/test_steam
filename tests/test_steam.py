from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import pytest

text = "Please check your password and account name and try again."

locator_in = "//a[@class='global_action_link']"
unique_home_page = "//a[@class='pulldown_desktop' and text() = 'Your Store']"
unique_login_page = "//div[text()='Sign in']"
locator_user_name = "//div[@class='page_content']//input[@type='text']"
locator_password = "//div[@class='page_content']//input[@type='password']"
locator_loading = "//button[@type='submit']//div//div"
locator_error = \
    "//div[contains(@class,'tool-tip-source')]/following-sibling::div[2]"
locator_url = "//link[@rel='canonical']"
locator_button_in = "//button[@type='submit']"


@pytest.mark.parametrize(
    "param",
    [
        pytest.param((Faker().user_name(), Faker().password()),
                     id=f"login:{Faker().user_name()}, "
                        f"password:{Faker().password()}")
    ]
)
def test_steam_login(driver, wait, param):
    user_name, password = param
    home_page = wait.until \
        (EC.presence_of_element_located((By.XPATH, unique_home_page)))
    assert home_page.is_displayed(), "Home page not found"

    wait.until(EC.presence_of_element_located((By.XPATH, locator_in))).click()
    login_page = wait.until \
        (EC.presence_of_element_located((By.XPATH, unique_login_page)))
    assert login_page.is_displayed(), "Login page not found"

    wait.until(EC.presence_of_element_located
               ((By.XPATH, locator_user_name))).send_keys(user_name)
    wait.until(EC.presence_of_element_located
               ((By.XPATH, locator_password))).send_keys(password)
    wait.until(EC.presence_of_element_located
               ((By.XPATH, locator_button_in))).click()
    loading = wait.until(EC.presence_of_element_located
                         ((By.XPATH, locator_loading)))
    assert loading.is_displayed()

    wait.until_not(EC.presence_of_element_located((By.XPATH, locator_loading)))
    error_text = wait.until \
        (EC.presence_of_element_located((By.XPATH, locator_error))).text
    assert error_text == text, "The error text is missing"
