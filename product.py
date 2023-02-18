from DataAsses.DataBase import Database
import requests


db = Database()


def get_product(url: str, user: int):
    response = requests.Session().get(url=url)

    result_product = []
    data = response.json()
    products = data.get("products")

    for product in products:
        old_price = product.get("basePrice").get(
            "formattedValue").replace('  RSD', '')
        new_price = product.get("price").get(
            "formattedValue").replace('  RSD', '')

        discount = round(
            (float(old_price) - float(new_price)) / float(old_price) * 100)

        result_product.append(
            {
                "name": product.get('name'),
                "link": f'https://www.tehnomanija.rs{product.get("url")}',
                "old_price": old_price,
                "new_price": new_price,
                "discount": discount
            }
        )

    db.add_product(result_product, user)
