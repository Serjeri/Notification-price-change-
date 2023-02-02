import requests
import json


def get_product(url):
    response = requests.Session().get(url=url)

    data = response.json()
    padination = data.get("pagination").get("totalPages")

    result_product = []
    for page in range(0, padination + 1):
        url = f"https://api.tehnomanija.rs/occ/v2/tehnomanija/products/search?fields=products(discountAmount(DEFAULT)%2CdiscountRate%2CbasePrice(DEFAULT)%2Ccode%2Cname%2Csummary%2Cprice(FULL)%2Curl%2Cimages(DEFAULT)%2Cstock(FULL)%2CaverageRating%2CvariantOptions%2Ccategories%2Cbrand%2CcategoryNames%2Cstickers)%2Cfacets%2Cbreadcrumbs%2Cpagination(DEFAULT)%2Csorts(DEFAULT)%2CfreeTextSearch%2CcurrentQuery%2CsuggestedCategories(DEFAULT)%2CkeywordRedirectUrl&query=%3Arelevance%3AallCategories%3A100304&currentPage={page}&pageSize=12&lang=sr_RS&curr=RSD"
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

    with open("ResultProduct/product.json", "w", encoding='utf-8') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


def main():
    get_product(url=""" https://api.tehnomanija.rs/occ/v2/tehnomanija/products/search?fields=products(discountAmount(DEFAULT)%2CdiscountRate%2CbasePrice(DEFAULT)%2Ccode%2Cname%2Csummary%2Cprice(FULL)%2Curl%2Cimages(DEFAULT)%2Cstock(FULL)%2CaverageRating%2CvariantOptions%2Ccategories%2Cbrand%2CcategoryNames%2Cstickers)%2Cfacets%2Cbreadcrumbs%2Cpagination(DEFAULT)%2Csorts(DEFAULT)%2CfreeTextSearch%2CcurrentQuery%2CsuggestedCategories(DEFAULT)%2CkeywordRedirectUrl&query=%3Arelevance%3AallCategories%3A100304&pageSize=12&lang=sr_RS&curr=RSD """)


if __name__ == "__main__":
    main()
