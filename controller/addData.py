import csv
from user import User


def add_users():
    with open(r'C:\Users\Selvia Nabil\Desktop\marketplace\controller\data\users.csv', 'rt')as f:
        data = csv.reader(f)
        for row in data:
            u1 = User(row[1], row[2], "0", row[0], "east", row[4])
            u2 = User(row[1], row[2], "0", row[0], "west", row[4])
            udata = u1.enter_app()
            u2data = u2.enter_app()
            u1.add_cash(int(row[5]), udata[0][0])
            u2.add_cash(int(row[5]), u2data[0][0])


add_users()
