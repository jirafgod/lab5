import MySQLdb
import sys

db = MySQLdb.connect(
    host="mysql23.hostland.ru",
    user="host1371925_rip",
    passwd="WouHDWpq",
    db="host1371925_lab6",
    use_unicode=True,
    charset="utf8"
)

name = input("Введите ваше имя: ")
family = input("Введите вашу фамилию: ")

cursor = db.cursor()

cursor.execute("SELECT * from `example` WHERE `name`=%s and `family`=%s;", (name, family))
if(len(cursor.fetchall()) != 0):
    print("Вы уже есть")
    sys.exit(0)
if(name == "Костя"):
    god = 1
else:
    god = 0
cursor.execute("INSERT INTO `example`(`name`, `family`, `god`) VALUES (%s,%s,%s);", (name, family, god))
db.commit()

cursor.execute("SELECT * from `example` WHERE 1;")
users = cursor.fetchall()

for user in users:
    print(user[1], user[2], end = "")
    if(user[3] == 1):
        print(" - Бог")
    else:
        print(" - Не Бог")

cursor.close()
db.close()
