from aiogram.utils.markdown import hbold, hlink
from DataAsses.DataBase import Database

db = Database()


def test(user_id: int, price: dict = None):

    price_product = 'Цена: '
    if price is not None:
        if price['price'] < db.price_change(user_id, price['id']):
            db.update_price(price['price'], user_id)
            price_product = 'Цена изменилась: '

    data = db.get_product_user(user_id)
    for item in data:
        card = f"{hlink(item[0], item[1])}\n"\
            f"{hbold(price_product)} {item[2]} RSD\n"\

        return card
