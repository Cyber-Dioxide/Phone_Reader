import random
import sys
from colorama import Fore,Style
from phonenumbers import carrier,geocoder,timezone
import phonenumbers
import fontstyle
import os


all_col= [Style.BRIGHT+Fore.RED,Style.BRIGHT+Fore.CYAN,Style.BRIGHT+Fore.LIGHTCYAN_EX, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX]

ran = random.choice(all_col)



ban = """
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


def banner():
    os.system("clear")

    print(ran, ban)
    print(ran + "\n\t\tV_2.0.0 'Latest_12/26/2021'\t\n")
    print("*" * 63)

    print(Style.BRIGHT + Fore.LIGHTCYAN_EX, "\n", "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
    print(Style.BRIGHT + Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)
    print("\n", "*" * 63)


banner()


def exit():
    sys.exit()


l = [Style.BRIGHT+Fore.RED, Style.BRIGHT+Fore.YELLOW, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX]


def cyanBold(n):
        n = fontstyle.apply(n, "bold")
        print(f"{Fore.LIGHTCYAN_EX} {n}")


def redBold(n):
        n = fontstyle.apply(n, "bold")
        print(f"{Fore.LIGHTRED_EX} {n}")

def greenBold(n):
        n = fontstyle.apply(n, "bold")
        print(f"{Fore.LIGHTGREEN_EX} {n}")

def randomcolors(n):
        c = random.choice(l)
        print(f"{c} {fontstyle.apply(n, 'bold')}")

def program():


    try:
        mobile_number = input(ran+"\nType phone number with country code: " +Style.BRIGHT +Fore.LIGHTYELLOW_EX)
        mobile_number = phonenumbers.parse(mobile_number)
        randomcolors("\nTime Zone for entered number: ")
        greenBold(timezone.time_zones_for_number(mobile_number))
        randomcolors("\nCarrier name: ")
        redBold(carrier.name_for_number(mobile_number, "en"))
        randomcolors("\nGeocoder Discripton: ")
        cyanBold(geocoder.description_for_number(mobile_number, "en"))
        randomcolors("\nValid phone number: ")
        if phonenumbers.is_valid_number(mobile_number) == True:
            cyanBold("\nYeah the phonenumber is valid ")
        else:
            redBold("\nNo the number is not valid ")

        randomcolors("\nCheacking possible number: ")
        cyanBold(phonenumbers.is_possible_number(mobile_number))


    except ModuleNotFoundError:
        print(ran + "\nInstallng modules")
        os.system("pip install phonumbers")
        os.system("pip install fontstyle")
        os.system("pip install colorama")

    except ValueError:
        print(ran+"\nHey! What are doing man!")
    except KeyboardInterrupt:
        print(ran+"\nHave a good day dear :-) ")


no = ["no" , "n"]


yes = ["yes" , "y"]
cont =""

while True:
    program()


    cont = input(ran + "\nDo you want to continue? [y/n]:").lower()

    if cont in yes:
        os.system("clear")
        banner()
    elif cont in no:
        print(ran + "\n\tDont Forget to do following tasks :-)\t\n")
        print(Fore.CYAN, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)
        exit()




