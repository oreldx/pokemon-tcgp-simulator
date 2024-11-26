class Card:
    def __init__(
        self,
        card_id: str,
        name: str,
    ):
        self.id = card_id
        self.name = name

    def __str__(self):
        return f"{self.name}"
