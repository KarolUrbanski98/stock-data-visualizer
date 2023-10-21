import json
import os
from datetime import datetime

import matplotlib.pyplot as plt

file_path = "historical_data.json"

if os.path.exists(file_path):
    with open(file_path, "r") as json_file:
        historical_data = json.load(json_file)

    for currency, data in historical_data.items():
        dates = [entry["date"] for entry in data]
        values = [entry["value"] for entry in data]

        dates = [datetime.strptime(date, "%d-%m-%y") for date in dates]

        plt.plot(dates, values, label=currency)

    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend(["USD", "GBP", "EUR", "CHF"])
    plt.title("Currencies values in time")
    plt.xticks(rotation=45)
    plt.show()
