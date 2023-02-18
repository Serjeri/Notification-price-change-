from ConfigFile.urlConfig import URL_CATEGORIES, URL_PAGE_COUNT, URL
import schedule
import json
import requests


def markdown_notice():
    response = requests.Session().get(url=URL)

    data = response.json()
    padination = data.get("pagination").get("totalPages")

    result_product = []
    for page in range(0, padination + 1):
        url = f"{URL_CATEGORIES}currentPage={page}{URL_PAGE_COUNT}"
        response = requests.Session().get(url=url)

        data = response.json()
        products = data.get("products")

        for product in products:
            old_price = product.get("basePrice").get(
                "formattedValue").replace('  RSD', '')
            new_price = product.get("price").get(
                "formattedValue").replace('  RSD', '')

            for item in data:
                if item.get('new_price') > new_price:
                    result_product.append(
                        {
                            "name": product.get('name'),
                            "url": f'https://www.tehnomanija.rs{product.get("url")}',
                            "old_price": old_price,
                            "new_price": new_price,
                        }
                    )



# schedule.every().day.at("10:30").do()
# while True:
#     schedule.run_pending(markdown_notice())
markdown_notice()

# with open('ProductResult/product.json', encoding='UTF-8') as first, open('ProductResult/priceDrop.json', encoding='UTF-8') as second:
#     first_json = json.load(first)
#     second_json = json.load(second)

# result = {}
# for pair in first_json.items():
#     for second_pair in second_json.items():
#         if pair[1]['card_name'] == second_pair[1]['card_name']:
#             first_price = to_int(pair[1]['card_price'])
#             second_price = to_int(second_pair[1]['card_price'])
#             if first_price < second_price:
#                 result[pair[0]] = pair[1]
#             else:
#                 result[second_pair[0]] = second_pair[1]

# print(result)
