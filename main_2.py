import database_2
import utils_2
import auth


def main_2():
    database_2.setup_database()
    auth.login_user()


if __name__ == "__main__":
    main_2()
