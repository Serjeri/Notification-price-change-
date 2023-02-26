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

    def show_product_user(self, user: int):
        with self.db:
            return self.cursor.execute(""" SELECT producTitle,link,price FROM users
            WHERE user = ? """, (user,)).fetchall()

    def id_product(self, id):
        with self.db:
            id_product = self.cursor.execute(
                """ SELECT idProduct FROM users
                    WHERE idProduct = ? """, (id,)).fetchone()

            return id_product

    def price_updates(self, products: dict):
        with self.db:
            pass

    def price_change(self, user: int, id_product: str):
        with self.db:
            id_product = self.cursor.execute(
                """ SELECT price, idProduct, user
                FROM users WHERE idProduct = ? and user = ?""", (id_product,user,)).fetchall()
