from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from utility import Util
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--lang=EN")
    web_chrome = webdriver.Chrome(options=options)
    web_chrome.get(Util().get_url())
    return web_chrome


@pytest.fixture()
def wait(driver):
    wait_1 = WebDriverWait(driver, 10)
    return wait_1
