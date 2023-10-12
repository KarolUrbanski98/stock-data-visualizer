import json
import os
from datetime import datetime

import matplotlib.pyplot as plt

file_path = "historical_data.json"

if os.path.exists(file_path):
    with open(file_path, "r") as json_file:
        historical_data = json.load(json_file)

    # Wygeneruj wykresy dla każdej waluty
    for currency, data in historical_data.items():
        dates = [entry["date"] for entry in data]
        values = [entry["value"] for entry in data]

        # Konwertuj daty z "dd-mm-yy" na daty Python
        dates = [datetime.strptime(date, "%d-%m-%y") for date in dates]

        plt.plot(dates, values, label=currency)

    plt.xlabel("Data")
    plt.ylabel("Wartość")
    plt.legend()
    plt.title("Wykresy wartości walut w czasie")
    plt.xticks(rotation=45)
    plt.show()
