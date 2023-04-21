from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import config


class SocialNetworkScraper:

    BASE_URL = f"{config.SOCIAL_NETWORK_HOST}:{config.SOCIAL_NETWORK_PORT}"
    LOGIN_URL = f"{BASE_URL}/auth/login"

    def __init__(self):
        self.driver = None

    def create_driver(self):
        try:
            self.driver = webdriver.Firefox(executable_path=config.FIREFOX_DRIVER_PATH)
            return self.driver
        except Exception as e:
            print(e.args)

    def social_network_login(self):
        driver = self.create_driver()
        driver.get(self.LOGIN_URL)
