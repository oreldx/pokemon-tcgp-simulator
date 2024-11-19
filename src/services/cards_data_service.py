import os
import json

import requests


class CardsDataService:
    def __init__(self, cache_file: str = None):
        self.base_url = "https://api.dotgg.gg"

        self.cards_data = {}
        self.cache_file = cache_file

        self._load_cards_data()

    def _load_cards_data(self) -> None:
        if self.cache_file and os.path.exists(self.cache_file):
            with open(self.cache_file, "r", encoding="utf-8") as f:
                self.cards_data = json.load(f)
                print(f"Number of cards loaded from cache: {len(self.cards_data)}")

        data = self._fetch_cards_data()
        print(f"Number of cards received: {len(data['data'])}")

        self.cards_data = self._process_cards_data(data)
        self._cache_cards_data()

    def _fetch_cards_data(self) -> dict:
        endpoint = "/cgfw/getcards"
        params = {"game": "pokepocket", "mode": "indexed"}
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
        }
        response = requests.get(
            url=self.base_url + endpoint,
            headers=headers,
            params=params,
            timeout=10,
        )

        if response.status_code != 200:
            print(f"Failed to fetch card data. Status code: {response.status_code}")
            return []

        return response.json()

    def _process_cards_data(self, data: dict) -> dict:
        cards_data = {}
        names = data["names"]
        for card_info in data["data"]:
            card_dict = dict(zip(names, card_info))
            card_id = card_dict["id"]
            cards_data[card_id] = card_dict

        return cards_data

    def get_card_by_name(self, name: str) -> list:
        if name is None:
            return []
        name = name.lower()
        return [
            card for card in self.cards_data.values() if name in card["name"].lower()
        ]

    def get_card_by_id(self, _id: str) -> dict:
        return self.cards_data.get(_id, None)

    def get_card_image_url(self, card_id: str) -> str:
        endpoint = f"/pokepocket/card/{card_id}.webp"
        base_url = self.base_url.replace("api", "static")
        return base_url + endpoint

    def _cache_cards_data(self) -> None:
        if self.cache_file:
            with open(self.cache_file, "w", encoding="utf-8") as f:
                json.dump(self.cards_data, f, indent=2)
