import json
import os


class DataManager:
    def __init__(self):
        self.file_path = "historical_data.json"

    def load_or_initialize_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as json_file:
                historical_data = json.load(json_file)
        else:
            historical_data = {
                "USD": [],
                "GBP": [],
                "EUR": [],
                "CHF": []
            }
        return historical_data

    def save_data(self, historical_data):
        with open(self.file_path, "w") as json_file:
            json.dump(historical_data, json_file)
