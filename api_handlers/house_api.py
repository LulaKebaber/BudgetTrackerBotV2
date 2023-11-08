import requests


class HouseAPI:

    def __init__(self, base_url, data):
        self.base_url = base_url
        self.data = data

    def create_new_house(self):
        url = f"{self.base_url}/api/create-house/"

        response = requests.post(url, json=self.data)
        return response.json()['message']

    def add_member(self):
        url = f"{self.base_url}/api/add-house-member/"

        response = requests.post(url, json=self.data)
        return response.json()['message']

    def get_house_members(self):
        house_name = self.data['house_name']

        url = f"{self.base_url}/api/get-house-info/{house_name}/"
        response = requests.get(url)

        data = "House name: " + response.json()['house_name'] + "\n" + "Owner: " + response.json()['owner'] + "\n"
        members = [member['username'] for member in response.json()['members']]
        members_parsed = ", ".join(members)
        data += "Members: " + members_parsed

        return data
