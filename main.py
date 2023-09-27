import json

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

# default browser - Firefox
preferred_browser = config_data.get("preferred_browser", "Firefox")

if preferred_browser == "Firefox":
    service_obj = FirefoxService(executable_path=GeckoDriverManager().install(), log_output="logs/geckodriver.log")
    driver = webdriver.Firefox(service=service_obj)
elif preferred_browser == "Chrome":
    service_obj = ChromeService(executable_path=ChromeDriverManager().install(), log_output="logs/chromedriver.log")
    driver = webdriver.Chrome(service=service_obj)
else:
    raise Exception("Unknown browser: " + preferred_browser)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.quit()
