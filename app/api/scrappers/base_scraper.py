from abc import ABC, abstractmethod
class BaseScraper(ABC):
    def __init__(self, retailer_name: str):
        self.retailer_name = retailer_name
    @abstractmethod
    async def scrape(self, product_name: str):
        pass
