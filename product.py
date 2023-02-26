from DataAsses.DataBase import Database
from bs4 import BeautifulSoup
import requests


db = Database()


class Product:

    def get_product(self,url: str, user: int):

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")
        product_title = soup.find(
            "div", class_="pdp-header--product-name").find_next("h1").text.strip()
        id_product = soup.find(
            "div", class_="code-id").text.strip().replace('Id:\xa0 ', '')
        price = soup.find(
            "span", class_="product-price-newprice").text.strip().replace('\xa0 RSD', '')

        self.result_product = dict()
        self.result_product.update(
            {
                "title": product_title,
                "link": url,
                "id_product": id_product,
                "price": price,
            }
        )
        response.close()

        if db.id_product(id_product) is None:
            db.add_product(self.result_product, user)
