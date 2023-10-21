import json
from datetime import datetime
from selenium.webdriver.common.by import By
from browserManager import BrowserManager
from dataManager import DataManager

current_date = datetime.now().strftime("%d-%m-%y")

data_manager = DataManager()
historical_data = data_manager.load_or_initialize_data()

browser_manager = BrowserManager()
driver = browser_manager.get_driver()
driver.get("https://nbp.pl/statystyka-i-sprawozdawczosc/kursy/tabela-a/")

rows = driver.find_elements(By.XPATH, "//tbody/tr")

for row in rows:
    currency = row.find_element(By.XPATH, "./td[2]")

    if currency.text == "1 USD":
        value = row.find_element(By.XPATH, "./td[3]")
        usd_string = value.text
        usd = float(usd_string.replace(",", "."))
        historical_data["USD"].append({"date": current_date, "value": usd})

    if currency.text == "1 GBP":
        value = row.find_element(By.XPATH, "./td[3]")
        gbp_string = value.text
        gbp = float(gbp_string.replace(",", "."))
        historical_data["GBP"].append({"date": current_date, "value": gbp})

    if currency.text == "1 EUR":
        value = row.find_element(By.XPATH, "./td[3]")
        eur_string = value.text
        eur = float(eur_string.replace(",", "."))
        historical_data["EUR"].append({"date": current_date, "value": eur})

    if currency.text == "1 CHF":
        value = row.find_element(By.XPATH, "./td[3]")
        chf_string = value.text
        chf = float(chf_string.replace(",", "."))
        historical_data["CHF"].append({"date": current_date, "value": chf})

data_manager.save_data(historical_data)

driver.close()
driver.quit()
