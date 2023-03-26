import sqlite3
# DATABASE_NAME = "games.db"

class SqliteDb:

    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name)

    # def get_db(db_name):
    #     conn = sqlite3.connect(db_name)
    #     return conn


    def insert_val(self, table_name, name, avatar, time):
        cursor = self.db.cursor()
        statement = "INSERT INTO %s(name, avatar, time) VALUES (?, ?, ?)".format(table_name)
        cursor.execute(statement, [name, avatar, time])
        self.db.commit()
        return True


    def update_val(self, table_name, id):
        cursor = self.db.cursor()
        statement = "UPDATE %s SET flag = ? WHERE id = ?".format(table_name)
        cursor.execute(statement, [2, id])
        self.db.commit()
        return True


    def delete_game(self, table_name, id):
        cursor = self.db.cursor()
        statement = "DELETE FROM %s WHERE id = ?".format(table_name)
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
        statement = "SELECT id, name, avatar, msg_state FROM %s where flag = 0 order by msg_state, id desc".format(table_name)
        cursor.execute(statement)
        return cursor.fetchone()
    # def get_games(db):
    #     cursor = db.cursor()
    #     query = "SELECT id, name, price, rate FROM games"
    #     cursor.execute(query)
    #     return cursor.fetchall()