from threading import Thread

from src.AutoMailingBot import app, start_mailing
from src.AdminBot import run_admin_bot


def main():
    Thread(target=start_mailing).start()
    Thread(target=run_admin_bot).start()
    app.run()

if __name__ == '__main__':
    main()
