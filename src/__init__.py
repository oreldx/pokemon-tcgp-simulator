from .services import CardsDataService


class PokemonTCGPSimulator:
    def __init__(self, cache_file: str = None):
        self.card_data_service = CardsDataService(cache_file=cache_file)

    def test(self):
        card = self.card_data_service.get_card_by_name("Pikachu")[0]
        print(self.card_data_service.get_card_by_id(card["id"]))
        print(self.card_data_service.get_card_image_url(card["id"]))
