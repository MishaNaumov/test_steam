from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import JsonUtils
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument(JsonUtils.get_attribute("options", "lang"))
    web_chrome = webdriver.Chrome(options=options)
    web_chrome.get(JsonUtils.get_attribute("url_steam"))
    return web_chrome
