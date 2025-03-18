from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    user = User()
    user.surname = "Ken"
    user.name = "Rid"
    user.age = 25
    user.position = "cock"
    user.speciality = "engineer"
    user.address = "module_2"
    user.email = "rid@mars.org"
    user1 = User()
    user1.surname = "Sid"
    user1.name = "Tidley"
    user1.age = 21
    user1.position = "doctor"
    user1.speciality = "doctor"
    user1.address = "module_1"
    user1.email = "sid@mars.org"
    user1.hashed_password = 'sid'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.add(user1)
    db_sess.commit()
    # app.run()




if __name__ == '__main__':
    main()