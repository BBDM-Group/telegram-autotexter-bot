from telebot.types import KeyboardButton


class AdminBotKeyboard:

    def __init__(self):
        self.settings = KeyboardButton('Настройки')
        self.start_mailing = KeyboardButton('Начать рассылку')
        self.text_settings = KeyboardButton('Настроить тексты')
        self.timer_settings = KeyboardButton('Настроить таймер рассылки')
        self.text_for_mailing = KeyboardButton('Добавить вариант текста авторассылки')
        self.text_for_users = KeyboardButton('Настроить универсальный текст для пользователей')
        self.back = KeyboardButton('В главное меню')
