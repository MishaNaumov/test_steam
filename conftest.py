from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def driver():
    web_chrome = webdriver.Chrome()
    return web_chrome

