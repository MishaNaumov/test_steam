from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url_steam = "https://store.steampowered.com/"

text = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."

locator_in = "//div[text()='Вход']"
locator_user_name = "//div[@class='page_content']//input[@type='text']"
locator_password = "//div[@class='page_content']//input[@type='password']"
locator_loading = "//div[@class='_2rGL7Sq1d-ghJqJTfs4UXH" \
                  " _2G7Us8OaLB1rNQFWsD19hd']"
locator_error = "//div[text()='Пожалуйста, проверьте свой пароль и имя" \
                " аккаунта и попробуйте снова.']"


def test_steam_login(driver):
    driver.get(url_steam)
    url_get = driver.find_element(By.XPATH, "//link[@rel='canonical']"). \
        get_attribute("href")
    assert url_get == url_steam, "Home page not found"

    driver.find_element(By.XPATH, "//a[@class='global_action_link']").click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.XPATH, locator_in)))
    text_in = driver.find_element(By.XPATH, locator_in).text
    assert text_in == "Вход", "Login page not found"

    driver.find_element(By.XPATH, locator_user_name).send_keys("user_2")
    driver.find_element(By.XPATH, locator_password).send_keys("qwerty")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    loading = driver.find_element(By.XPATH, locator_loading)
    assert loading.is_displayed()

    wait.until_not(EC.presence_of_element_located((By.XPATH, locator_loading)))
    error_text = driver.find_element(By.XPATH, locator_error).text
    assert error_text == text, "The error text is missing"
