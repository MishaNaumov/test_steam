import selenium.common
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils import JsonUtils
from faker import Faker
import pytest

TEXT = "Please check your password and account name and try again."

LOCATOR_IN = "//a[@class='global_action_link']"
UNIQUE_HOME_PAGE = "//a[@class='pulldown_desktop' and text() = 'Your Store']"
UNIQUE_LOGIN_PAGE = "//div[text()='Sign in']"
LOCATOR_USER_NAME = "//div[@class='page_content']//input[@type='text']"
LOCATOR_PASSWORD = "//div[@class='page_content']//input[@type='password']"
LOCATOR_LOADING = "//button[@type='submit']//div//div"
LOCATOR_ERROR = \
    "//div[contains(@class,'tool-tip-source')]/following-sibling::div[2]"
LOCATOR_BUTTON_IN = "//button[@type='submit']"


@pytest.mark.parametrize(
    "param",
    [
        pytest.param((Faker().user_name(), Faker().password()),
                     id=f"login:{Faker().user_name()}, "
                        f"password:{Faker().password()}")
    ]
)
def test_steam_login(driver, param):
    user_name, password = param
    wait = WebDriverWait(driver, JsonUtils.get_attribute("timeout"))

    def is_page_opened(locator):
        try:
            wait.until \
                (EC.presence_of_element_located((By.XPATH, locator)))
            return True
        except selenium.common.TimeoutException:
            return False

    assert is_page_opened(UNIQUE_HOME_PAGE), "Home page not opened"

    wait.until(EC.element_to_be_clickable((By.XPATH, LOCATOR_IN))).click()
    assert is_page_opened(UNIQUE_LOGIN_PAGE), "Login page not opened"

    wait.until(EC.visibility_of_element_located
               ((By.XPATH, LOCATOR_USER_NAME))).send_keys(user_name)
    wait.until(EC.visibility_of_element_located
               ((By.XPATH, LOCATOR_PASSWORD))).send_keys(password)
    wait.until(EC.element_to_be_clickable
               ((By.XPATH, LOCATOR_BUTTON_IN))).click()
    loading = wait.until(EC.presence_of_element_located
                         ((By.XPATH, LOCATOR_LOADING)))
    assert loading.is_displayed()

    wait.until_not(EC.presence_of_element_located((By.XPATH, LOCATOR_LOADING)))
    error_text = wait.until \
        (EC.presence_of_element_located((By.XPATH, LOCATOR_ERROR))).text
    assert error_text == TEXT, f"{error_text} The error text is missing"
