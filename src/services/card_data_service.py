import os
import json

import requests


class CardDataService:
    API_URL = "https://api.dotgg.gg/cgfw/getcards?"

    def __init__(self, cache_file: str = None):
        self.base_url = "https://api.dotgg.gg"

        self.card_data = {}
        self.cache_file = cache_file
        self.load_card_data()

    def load_card_data(self):
        if self.cache_file and os.path.exists(self.cache_file):
            with open(self.cache_file, "r", encoding="utf-8") as f:
                self.card_data = json.load(f)
                print(f"Number of cards loaded from cache: {len(self.card_data)}")
                return

        self.fetch_and_cache_card_data()

    def fetch_and_cache_card_data(self):
        endpoint = "/cgfw/getcards"
        params = {"game": "pokepocket", "mode": "indexed"}
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
        }
        response = requests.get(
            url=self.base_url + endpoint, headers=headers, params=params
        )

        if response.status_code != 200:
            print(f"Failed to fetch card data. Status code: {response.status_code}")
            return

        data = response.json()
        print(f"Number of cards received: {len(data['data'])}")
        self.process_card_data(data)
        self.cache_card_data()

    def process_card_data(self, data):
        names = data["names"]
        for card_info in data["data"]:
            card_dict = dict(zip(names, card_info))
            card_id = card_dict["id"]
            self.card_data[card_id] = card_dict

    def get_card_by_name(self, name):
        if name is None:
            return []
        name = name.lower()
        return [
            card for card in self.card_data.values() if name in card["name"].lower()
        ]

    def get_card_by_id(self, _id):
        return self.card_data.get(_id, None)

    def get_card_image_url(self, card_id):
        endpoint = f"/pokepocket/card/{card_id}.webp"
        return self.base_url + endpoint

    def cache_card_data(self):
        if self.cache_file:
            with open(self.cache_file, "w", encoding="utf-8") as f:
                json.dump(self.card_data, f)
