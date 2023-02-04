from ConfigFile.config import URLCATEGORIES, URLPAGESIZE
import requests
import json


def get_product(url):
    response = requests.Session().get(url=url)

    data = response.json()
    padination = data.get("pagination").get("totalPages")

    result_product = []
    for page in range(0, padination + 1):
        url = f"{URLCATEGORIES}currentPage={page}{URLPAGESIZE}"
        response = requests.Session().get(url=url)

        data = response.json()
        products = data.get("products")

        for product in products:
            price = product.get("price").get("formattedValue")

            result_product.append(
                {
                    "name": product.get('name'),
                    "url": f'https://www.tehnomanija.rs{product.get("url")}',
                    "price": price
                }
            )

        print(f"{page}/{padination}")

    with open("ProductResult/product.json", "w", encoding='utf-8') as file:
        json.dump(result_product, file, indent=4, ensure_ascii=False)
