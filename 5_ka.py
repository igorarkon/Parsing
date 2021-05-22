import json
import time
import os
from pathlib import Path
import requests


class Parse5ka:
    headers = {
        "User-Agent": "Igor"
    }

    def __init__(self, start_url, save_path: Path):
        self.start_url = start_url
        self.save_path = save_path

    def _get_response(self, url):  # Запрос, если 200 то респонс
        while True:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response
            time.sleep(0.5)

    def run(self): # Запуск
        for product in self._parse(self.start_url):
            file_path = self.save_path.joinpath(f"{product['id']}.json")
            self._save(product, file_path)

    def _parse(self, url):  #Парсинг
        while url:
            response = self._get_response(url)
            data: dict = response.json()
            url = data["next"]
            for product in data['results']:
                yield product

    def _save(self, data: dict, file_path: Path):  #Сохранение
        file_path.write_text(json.dumps(data, ensure_ascii=False))

os.mkdir('products')
def get_save_path(dir_name: str) -> Path:
   save_path = Path(__file__).parent.joinpath(dir_name)
   if not save_path.exists():
       save_path.mkdir()
   return save_path

if __name__ == '__main__':
    url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=973&ordering=&price_promo__gte=&price_promo__lte=&search='
    product_path = get_save_path('products/mai')
    parser = Parse5ka(url, product_path)
    parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=698&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/dairy_products')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=888&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/bread')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=716&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/meat_poultry')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=628&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/sausage')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=602&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/frozen_food')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=800&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/fish')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=870&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/grocery_stores')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=853&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/sweets')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=902&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/tea_coffee')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=732&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/drinks')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=637&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/canned_food')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=661&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/beauty')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=575&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/pet_products')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=523&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/products_children')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=542&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/household_goods')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=938&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/best_promotion')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=939&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/rating_leaders')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=943&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/cozy_dinner')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=942&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/brisk_breakfast')
   parser = Parse5ka(url, product_path)
   parser.run()

if __name__ == '__main__':
   url = 'https://5ka.ru/api/v2/special_offers/?store=Y238&records_per_page=12&page=1&categories=945&ordering=&price_promo__gte=&price_promo__lte=&search='
   product_path = get_save_path('products/for_kids')
   parser = Parse5ka(url, product_path)
   parser.run()
