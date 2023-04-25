import sqlite3
# DATABASE_NAME = "games.db"

class SqliteDb:

    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name, check_same_thread=False)
        self.db.row_factory = self.dict_factory
    # def get_db(db_name):
    #     conn = sqlite3.connect(db_name)
    #     return conn


    def insert_val(self, table_name, args):
        key_str = ""
        val_arr = []
        val_expr = ""
        for key, val in args.items():
            key_str += key if len(key_str) == 0 else ", " + key
            val_arr.append(val)
            val_expr += "?" if len(val_expr) == 0 else ", ?"
        cursor = self.db.cursor()
        statement = "INSERT INTO {}({}) VALUES ({})".format(table_name, key_str, val_expr)
        # print(val_expr)
        # print(statement)
        cursor.execute(statement, val_arr)
        self.db.commit()
        return True


    def update_val(self, table_name, id):
        cursor = self.db.cursor()
        statement = "UPDATE {} SET tag = ? WHERE id = ?".format(table_name)
        cursor.execute(statement, [2, id])
        self.db.commit()
        return True


    def delete_game(self, table_name, id):
        cursor = self.db.cursor()
        statement = "DELETE FROM {} WHERE id = ?".format(table_name)
        cursor.execute(statement, [id])
        self.db.commit()
        return True


    def get_by_id(self, table_name, id):
        cursor = self.db.cursor()
        statement = "SELECT id, name, avatar FROM %s WHERE id = ?".format(table_name)
        cursor.execute(statement, [id])
        return cursor.fetchone()

    def get_one(self, table_name):

        cursor = self.db.cursor()
        statement = "SELECT * FROM {} where tag = 0 order by GiftLevel, id desc".format(table_name)
        cursor.execute(statement)
        return cursor.fetchone()

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d