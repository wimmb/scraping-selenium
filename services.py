import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import config
from decorators import social_login_required


class SocialNetworkScraper:

    BASE_URL = f"{config.SOCIAL_NETWORK_HOST}:{config.SOCIAL_NETWORK_PORT}"
    LOGIN_URL = f"{BASE_URL}/auth/login"
    BLOG_URL = f"{BASE_URL}/user/blog"

    def __init__(self, driver=None):
        self.driver = driver or self.create_driver()
        self.is_logged_in = False

    def create_driver(self):
        try:
            options = Options()
            options.add_argument("--start-maximized")

            self.driver = webdriver.Chrome(executable_path=config.FIREFOX_DRIVER_PATH, options=options)
            return self.driver
        except Exception as e:
            print(e.args)

    def social_network_login(self):

        self.driver.get(self.LOGIN_URL)
        time.sleep(1)

        username_elem = self.driver.find_element(By.XPATH, "//div/input[@id='username']")
        username_elem.send_keys(config.SOCIAL_NETWORK_LOGIN)
        time.sleep(1)

        password_elem = self.driver.find_element(By.XPATH, "//div/input[@id='password']")
        password_elem.send_keys(config.SOCIAL_NETWORK_PASSWORD)
        time.sleep(1)

        button_elem = self.driver.find_element(By.XPATH, "//div/button[@type='submit']")
        button_elem.click()
        self.is_logged_in = True

    @social_login_required
    def social_network_add_post(self, title, content):

        self.driver.get(self.BLOG_URL)
        time.sleep(1)

        title_elem = self.driver.find_element(By.XPATH, "//form/div/input[@id='title']")
        title_elem.send_keys(title)
        time.sleep(1)

        content_elem = self.driver.find_element(By.XPATH, "//form/div/textarea[@id='content']")
        content_elem.send_keys(content)
        time.sleep(1)

        button_elem = self.driver.find_element(By.XPATH, "//form/button[@type='submit']")
        button_elem.click()
