import MySQLdb
import sys

class connection:
    def __init__(self, user, password, db, host='mysql23.hostland.ru'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None
    @property
    def connection(self):
        return self._connection
    def __enter__(self):
        return self.connect()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
    def connect(self):
        self._connection = MySQLdb.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            db=self.db,
            use_unicode=True,
            charset="utf8"
        )
    def disconnect(self):
        if self._connection:
            self._connection.close()

class Example:
    def __init__(self, db_connection, name=None, family=None):
        self.db_connection = db_connection.connection
        self.name = name
        self.family = family
    def count(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * from `example` WHERE `name`=%s and `family`=%s;", (self.name, self.family))
        return len(cursor.fetchall())
    def get(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * from `example` WHERE 1;")
        return cursor.fetchall()
    def insert(self, god):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO `example`(`name`, `family`, `god`) VALUES (%s,%s,%s);", (self.name, self.family, god))
        self.db_connection.commit()

"""name = input("Введите ваше имя: ")
family = input("Введите вашу фамилию: ")
if(name == "Костя"):
    god = 1
else:
    god = 0

connection = connection("host1371925_rip", "WouHDWpq", "host1371925_lab6")
connection.connect()
with connection:
    user = Example(connection, name, family)
    if(user.count() != 0):
        print("Вы уже есть")
        sys.exit(0)
    user.insert(god)
    users = user.get()
    for user in users:
        print(user[1], user[2], end = "")
        if(user[3] == 1):
            print(" - Бог")
        else:
            print(" - Не Бог")"""
