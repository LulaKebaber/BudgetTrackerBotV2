import requests


class UserAPI:
    def __init__(self, base_url, message):
        self.base_url = base_url
        self.message = message

    def add_new_user(self):
        url = f"{self.base_url}/api/add-person/"

        data = {
            "username": self.message.from_user.username,
            "telegram_id": self.message.from_user.id,
        }

        response = requests.post(url, json=data)
        return response.json()["message"]
