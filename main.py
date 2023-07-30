from pynput import keyboard
from threading import Thread

from src.AutoMailingBot import app, start_mailing
from src.AdminBot import run_admin_bot


def on_press(key, abortKey='esc'):    
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys    

    print('pressed %s' % (k))
    if k == abortKey:
        print('end loop ...')
        return False  # stop listener
    

def main():
    abortKey = 'esc'
    
    listener = keyboard.Listener(on_press=on_press, abortKey=abortKey)
    listener.start()

    Thread(target=start_mailing).start()
    Thread(target=run_admin_bot).start()
    app.run()

    listener.join()

if __name__ == '__main__':
    main()
