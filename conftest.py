from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless")
    web_chrome = webdriver.Chrome(options=options)
    return web_chrome

