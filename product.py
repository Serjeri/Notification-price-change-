from DataAsses.dataBase import Database
from bs4 import BeautifulSoup
from ConfigFile.urlConfig import HEADERS, URL
import requests


db = Database()


class Tehnomanija:

    def get_product(self):
        def get_product_lambda(soup): return dict(
            title=soup.find(
                "div", class_="pdp-header--product-name").find_next("h1").text.strip(),
            link=URL,
            id_product=soup.find(
                "div", class_="code-id").text.strip().replace('Id:\xa0 ', ''),
            price=soup.find(
                "span", class_="product-price-newprice").text.strip().replace('\xa0 RSD', ''))

        return self._process_response(get_product_lambda)

    def get_price(self):
        def get_price_lambda(soup): return soup.find(
            "span", class_="product-price-newprice").text.strip().replace('\xa0 RSD', '')

        return self._process_response(get_price_lambda)

    def _process_response(self, func):

        response = requests.get(url=URL, headers=HEADERS)
        soup = BeautifulSoup(response.text, "lxml")
        result = func(soup)
        response.close()

        return result
