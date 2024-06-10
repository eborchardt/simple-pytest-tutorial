class ItemDatabase:
    def __init__(self) -> None:
        self.applePrice = 1.0
        self.orangePrice = 2.0

    def get(self, item: str) -> float:
        if item == "apple":
            return self.applePrice
        if item == "orange":
            return self.orangePrice
        raise ValueError(f"Item '{item}' not found in database")
