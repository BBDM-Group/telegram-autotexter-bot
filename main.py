class Bot:

    def __init__(self):
        self.api = Database.get_cfg()

    def send(self, text, id):
        pass


class Database:

    def __init__(self):
        pass

    def get_ids(self):
        pass

    @staticmethod
    def get_cfg():
        pass

    def get_time(self):
        # Нужно проверить, настроено ли время
        pass