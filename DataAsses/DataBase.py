import sqlite3
from ConfigFile.urlConfig import URL


class Database:
    def __init__(self):
        self.db = sqlite3.connect('DataAsses/StoreUsers.db')
        self.cursor = self.db.cursor()
        self.db.commit()

    def add_product(self, products: dict, user: int):
        with self.db:
            self.cursor.execute(
                """ INSERT INTO users (user,producTitle,link,idProduct,price) VALUES(?,?,?,?,?) """,
                (user, products['title'], products['link'], products['id_product'],
                 products['price'],))
            self.db.commit()

    def get_product_user(self, user: int):
        with self.db:
            return self.cursor.execute(""" SELECT producTitle,link,price FROM users
            WHERE user = ? """, (user,)).fetchall()

    def price_change(self, user: int):
        with self.db:
            price = self.cursor.execute(
                """ SELECT price, user
                FROM users WHERE user = ?""", ( user,)).fetchone()
            return price

    def get_link_user(self, link: str):
        with self.db:
            link_dict = dict()
            user_link = self.cursor.execute(
                """ SELECT link FROM users""").fetchall()

            for i in user_link:
                link_dict[i[0]] = 'link'

            if link in link_dict:
                return True

    def add_new_user(self, link, user_id):
        with self.db:
            product = self.cursor.execute(
                """ SELECT producTitle,idProduct,price,user FROM users WHERE link = ? """, (link,)).fetchall()[0]

            self.cursor.execute(
                """ INSERT INTO users (user,producTitle,link,idProduct,price) VALUES(?,?,?,?,?) """,
                (user_id, product[0], link, product[1], product[2],))
            self.db.commit()

    def get_user(self, id: int):
        with self.db:
            user = self.cursor.execute(
                """ SELECT user FROM users WHERE user = ? """, (id,)).fetchone()
            return user

    def update_price(self, price: str, id: int):
        with self.db:
            self.cursor.execute(
                """ UPDATE users SET price = ? WHERE user = ? """, (price, id,))
