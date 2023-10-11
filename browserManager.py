import json
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class BrowserManager:
    def __init__(self):
        self.__driver = self.__initialize_browser()

    def __initialize_browser(self):
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)

        preferred_browser = config_data.get("preferred_browser", "Firefox")

        if preferred_browser == "Firefox":
            return self.__initialize_firefox()
        elif preferred_browser == "Chrome":
            return self.__initialize_chrome()
        else:
            raise Exception("Unknown browser: " + preferred_browser)

    def __initialize_firefox(self):
        service_obj = FirefoxService(executable_path=GeckoDriverManager().install(), log_path="geckodriver.log")
        return webdriver.Firefox(service=service_obj)

    def __initialize_chrome(self):
        service_obj = ChromeService(executable_path=ChromeDriverManager().install(), log_path="chromedriver.log")
        return webdriver.Chrome(service=service_obj)

    def get_driver(self):
        return self.__driver
