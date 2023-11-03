import requests


class UserAPI:

    @staticmethod
    def add_new_user(message):
        url = "http://127.0.0.1:8000/api/add-person/"

        data = {
            "username": message.from_user.username,
            "telegram_id": message.from_user.id,
        }

        response = requests.post(url, json=data)
        return response.json()["message"]
