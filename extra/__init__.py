from colorama import Fore, Back, Style


print(f"""
 {Fore.RED}
 {Back.WHITE}
    Type this in the command line: {Fore.BLACK}python keylogger.py --name NAME

    {Back.BLACK} {Fore.WHITE}
    NAME Should be eqaul to input name otherwise this won't Work
        so be careful with that
        """)
    
print(Style.RESET_ALL)



def calling_function():
    return 'Completed'