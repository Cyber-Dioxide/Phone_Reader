import os
import platform

logo = f"""
██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗     
██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝     
██████╔╝███████║██║   ██║██╔██╗ ██║█████╗       
██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝       
██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗     
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝     
██████╗ ███████╗ █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝█████╗  ███████║██║  ██║█████╗  ██████╔╝
██╔══██╗██╔══╝  ██╔══██║██║  ██║██╔══╝  ██╔══██╗
██║  ██║███████╗██║  ██║██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                     
"""
from colorama import Fore,Style

from scripts import colors
c = colors
def banner():
    print(c.ran + logo)

    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/ ", "- " * 3+c.ran + "|")


def banner2():

    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/ ", "- " * 3+c.ran + "|")




def clear():
    s = platform.platform()
    if "Windows" in s:
        os.system("cls")
    else:
        os.system("clear")
