
from scripts.banner import banner2,banner,clear
from scripts.colors import ran,y,c,g,lg,r
import sys , os
try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    os.system("pip install colorama")
from phonenumbers import carrier,geocoder,timezone , NumberParseException
try:
    import phonenumbers
except ModuleNotFoundError:
    os.system("pip install phonenumbers")

try:
    import fontstyle
except ModuleNotFoundError:
    os.system("pip install fontstyle")

import os

clear()
banner()

def exit():
    sys.exit()



def program():


    try:
        mobile_number = input(ran+"\nType phone number with country code: " +Style.BRIGHT +Fore.LIGHTYELLOW_EX)
        mobile_number = mobile_number.replace(" ", "")
        try:
            mobile_number = phonenumbers.parse(mobile_number)

        except NumberParseException:
            print(r , "Wrong Input format")
            exit()
        print(c , "\nTime Zone for entered number: ")
        print(c , timezone.time_zones_for_number(mobile_number))
        print(y , "\nCarrier name: ")
        print(y , carrier.name_for_number(mobile_number, "en"))
        print(g ,"\nGeocoder Discripton: ")
        print(g , geocoder.description_for_number(mobile_number, "en"))
        print(r , "\nValid phone number: ")
        if phonenumbers.is_valid_number(mobile_number) == True:
            print(r , "Yeah the phonenumber is valid ")
        else:
            print(r , "No the number is not valid ")

        print(y , "\nChecking possible number: ")
        print(y , phonenumbers.is_possible_number(mobile_number))

    except ValueError:
        print(ran,"\nHey! What are doing man!")
    except KeyboardInterrupt:
        print(ran,"\nHave a good day dear :-) ")


no = ["no" , "n"]


yes = ["yes" , "y"]
cont =""

while cont not in no:
    program()

    cont = input(ran + "\nDo you want to continue? [y/n]:" + lg).lower()

    if cont in yes:
        os.system("clear")
        banner()
    elif cont in no:
        banner2()




