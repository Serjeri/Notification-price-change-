from aiogram.utils.markdown import hbold, hlink
from DataAsses.dataBase import Database
from product import Tehnomanija
from ConfigFile.urlConfig import URL


def test(user_id: int):
    db = Database()
    tehnomanija = Tehnomanija()

    user = db.get_user(user_id)
    link = db.get_link_user(URL)
    price_title = 'Цена: '

    if user is None and link is None:
        product = tehnomanija.get_product()
        db.add_product(product, user_id)

    elif link is True and user is None:
        db.add_new_user(URL, user_id)

    else:
        price = tehnomanija.get_price()
        if price < db.price_change(user_id):
            db.update_price(price, user_id)
            price_title = 'Цена изменилась: '

    data = db.show_product_user(user_id)
    for item in data:
        card = f"{hlink(item[0], item[1])}\n"\
            f"{hbold(price_title)} {item[2]} RSD\n"\

    return card
    