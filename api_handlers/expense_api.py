import requests


class ExpenseAPI:
    def __init__(self, base_url, data):
        self.base_url = base_url
        self.data = data

    def add_expense(self):
        url = f"{self.base_url}api/add-expense/"

        response = requests.post(url, json=self.data)
        return response.json()['message']