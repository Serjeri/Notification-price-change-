import sqlite3
from ConfigFile.urlConfig import URL


class Database:
    def __init__(self):
        self.db = sqlite3.connect('DataAsses/StoreUsers.db')
        self.cursor = self.db.cursor()
        self.db.commit()

    def add_user(self, user_id: str):
        with self.db:
            self.cursor.execute(
                """ INSERT INTO users (user) VALUES(?) """, (user_id,))
            self.db.commit()

            user_fk = self.cursor.execute(
                """ SELECT id, user FROM users WHERE user = ? """, (user_id,)).fetchall()[0]

            self.cursor.execute(
                """ INSERT INTO product (FK_users) VALUES(?) """, (user_fk[0],))
            self.db.commit()

    def search_user(self, user_id: str):
        with self.db:
            user = self.cursor.execute(
                """ SELECT user FROM users WHERE user = ? """, (user_id,))
            return user.fetchone()

    def add_product(self, products: list, user: int):
        with self.db:
            # TODO подумать над ссылкой магазина
            user_link_shop = self.cursor.execute(
                """ SELECT distinct product.link_shop FROM product
                    JOIN users ON product.FK_users = users.id
                    WHERE user = ? """, (user,)).fetchall()[0]

            if URL != user_link_shop[0]:
                user_fk = self.cursor.execute(
                    """ SELECT id, user FROM users WHERE user = ? """, (user,)).fetchall()[0]

                for product in products:
                    self.cursor.execute(
                        """ INSERT INTO product (product_name,link_product,old_price,
                        new_price,discount,FK_users) VALUES(?,?,?,?,?,?) """,
                        (product['name'], product['link'], product['old_price'],
                         product['new_price'], product['discount'], user_fk[0],))
                    self.db.commit()

    def show_product_user(self, user: int):
        with self.db:
            return self.cursor.execute(""" SELECT users.user,product.product_name,
            product.link_product,product.old_price,product.new_price,product.discount FROM product
            JOIN users ON product.FK_users = users.id
            WHERE user = ? """, (user,)).fetchall()
