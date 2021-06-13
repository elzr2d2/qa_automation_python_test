import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_login_url():
        login_url = config.get('common info', 'loginURL')
        return login_url

    @staticmethod
    def get_application_url():
        main_url = config.get('common info', 'mainURL')
        return main_url

    @staticmethod
    def get_username():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
