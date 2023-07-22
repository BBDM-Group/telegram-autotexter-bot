import telebot
from telebot.types import ReplyKeyboardMarkup, Message

from src.utils import *
from src.AdminBotKeyboard import AdminBotKeyboard
from src.AutoMailingBot import mail

bot = telebot.TeleBot(get_settings()['admin_bot_api'])

bot_keyboard = AdminBotKeyboard()


class UserPosition:
    MAIN_MENU = 0
    SETTINGS = 1
    TEXT_SETTINGS = 2
    TIMER_SETTINGS = 3
    TEXT_FOR_MAILING = 4
    TEXT_FOR_USERS = 5


ADMIN_POS = UserPosition.MAIN_MENU


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Здравствуйте. Для управления ботом используйте кнопки ниже:",
        reply_markup=make_keyboard('main_menu')
    )


def wait_input1(message: Message):
    bot.send_message(message.from_user.id, 'Текст успешно обновлен')
    update_settings('text', message.text)


def wait_input2(message: Message):
    bot.send_message(message.from_user.id, 'Текст усешно обновлен')
    update_settings('text_for_reply', message.text)


def wait_input_date(message: Message):
    try:
        new_timers = []
        for i in message.text.split(','):
            new_timers.append(datetime.strftime(datetime.strptime(i.strip( ), '%d-%m-%y %H:%M:%S'), '%d-%m-%y %H:%M:%S'))
    except:
        bot.send_message(message.from_user.id, 'Неправильный формат даты. Проверьте сообщение и отправьте еще раз')
        bot.register_next_step_handler(message, wait_input_date)
    new_timers = []
    for i in message.text.split(','):
        new_timers.append(datetime.strftime(datetime.strptime(i.strip(), '%d-%m-%y %H:%M:%S'), '%d-%m-%y %H:%M:%S'))
    update_settings('timer', new_timers)
    bot.send_message(message.from_user.id, 'Таймер рассылки успешно обновлен')


@bot.message_handler(func=lambda message: True)
def all_messages(message: Message):
    if message.from_user.id == get_settings()['admin_id']:
        if message.text == "Настройки":
            bot.send_message(message.from_user.id, text='Доступные настройки: ', reply_markup=make_keyboard('settings'))
        elif message.text == 'Начать рассылку':
            bot.send_message(message.from_user.id, text='Начата рассылка...', reply_markup=make_keyboard('main_menu'))
            mail()
        elif message.text == 'Настроить тексты':
            bot.send_message(message.from_user.id, 'Здесь можно настроить текст для рассылки и для пользователей',
                             reply_markup=make_keyboard('text_settings'))
        elif message.text == 'Настроить таймер рассылки':
            bot.send_message(message.from_user.id,
                             'Отправьте дату следующей рассылки в формате ДД-ММ-ГГ ЧЧ:ММ:СС. Например: 21-07-23 '
                             '23:55:00\nЕсли таймеров несколько, то пишите их через запятую: \n21-07-23 23:55:00, '
                             '21-07-23 23:55:05')
            bot.register_next_step_handler(message, wait_input_date)
        elif message.text == 'Настроить текст авторассылки':
            bot.send_message(message.from_user.id, 'Отправьте текст, который вы хотите рассылать в чаты')
            bot.register_next_step_handler(message, wait_input1)
        elif message.text == 'Настроить универсальный текст для пользователей':
            bot.send_message(message.from_user.id, 'Отправьте текст, которым вы хотите отвечать пользователям')
            bot.register_next_step_handler(message, wait_input2)
        elif message.text == 'В главное меню':
            bot.send_message(message.from_user.id, 'Возвращение в главное меню', reply_markup=make_keyboard('main_menu'))
        else:
            bot.send_message(message.from_user.id, 'Неверная команда')


def make_keyboard(keyboard_type):
    markup = ReplyKeyboardMarkup()
    if keyboard_type == 'main_menu':
        markup.add(bot_keyboard.settings)
        markup.add(bot_keyboard.start_mailing)
    if keyboard_type == 'settings':
        markup.add(bot_keyboard.text_settings)
        markup.add(bot_keyboard.timer_settings)
        markup.add(bot_keyboard.back)
    if keyboard_type == 'text_settings':
        markup.add(bot_keyboard.text_for_mailing)
        markup.add(bot_keyboard.text_for_users)
        markup.add(bot_keyboard.back)
    return markup


def run_admin_bot():
    markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(get_settings()['admin_id'], text='Бот успешно запущен. Напишите /start для начала работы',
                     reply_markup=markup)
    print('Admin bot is running')
    bot.infinity_polling()
