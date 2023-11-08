import requests


class SettlementAPI:
    def __init__(self, base_url, data):
        self.base_url = base_url
        self.data = data

    def add_new_settlement(self):
        url = f"{self.base_url}api/add-settlement/"

        response = requests.post(url, json=self.data)
        return response.json()["message"]

    def get_debts(self):
        telegram_id = self.data["telegram_id"]
        url = f"{self.base_url}api/get-debt/{telegram_id}/"

        response = requests.get(url)
        debts = response.json()["debts"]

        result = "Your debts\n\n"
        for person, amount in debts.items():
            result += f"{person}: {amount}\n"

        return result
