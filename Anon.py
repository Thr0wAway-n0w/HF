import time
import os
os.system("git fetch")
os.system("git pull")
os.system("sudo apt install pipenv")
os.system("pipenv run pip3 install termcolor")
os.system("pipenv run pip3 install colorama")
os.system("pipenv run pip3 install ascii_magic")
os.system("pipenv run pip3 install pillow")
os.system("pipenv run pip3 install tabulate")
import colorama
from colorama import Fore
import subprocess
from colorama import Back
import tabulate
import re
import sys
import subprocess
import termcolor
from termcolor import colored
from time import sleep
from PIL import ImageEnhance
from ascii_magic import AsciiArt

def ascii_banner():
    try:
        my_art = AsciiArt.from_url('https://i.postimg.cc/Jhbhr2hT/Screenshot-2024-04-21-at-05-13-59-e21459f8019688f030e3fd2ddf70830b-jpg-JPEG-Image-338-600-pixels.png')
    except OSError as e:
        print(f'Could not load the image, server said: {e.code} {e.msg}')
    my_art.to_terminal()

def clear_screen():
    subprocess.run('clear' if os.name == 'posix' else 'cls')


def change():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

def main():
    ascii_banner()
    print(colored("Starting AnonGT", "red", attrs=["reverse", "blink", "bold"]))
    time.sleep(3)
    os.system("git clone https://github.com/gt0day/AnonGT.git")
    os.chdir("AnonGT")
    os.system("sudo chmod +x install.py")
    os.system("sudo python3 ./install.py install")
    main_menu()

def main_menu():
    os.system("sudo python3 AnonGT.py")
    choice = input("Select Option: ")
    if choice == "start":
        os.system("sudo python3 AnonGT.py start")
        main_menu()
    if choice == "start+":
        os.system("sudo python3 AnonGT.py start+")
        main_menu()
    if choice == "stop":
        os.system("sudo python3 AnonGT.py stop")
        main_menu()
    if choice == "status":
        os.system("sudo python3 AnonGT.py status")
        time.sleep(5)
        main_menu()
    if choice == "myip":
        os.system("sudo python3 AnonGT.py myip")
        time.sleep(5)
        main_menu()
    if choice == "chngid":
        os.system("sudo python3 AnonGT.py chngid")
        main_menu()
    if choice == "autochng":
        os.system("sudo python3 AnonGT.py autochng")
        main_menu()
    if choice == "antimitm":
        os.system("sudo python3 AnonGT.py antimitm")
        main_menu()
    if choice == "chngmac":
        os.system("sudo python3 AnonGT.py chngmac")
        main_menu()
    if choice == "rvmac":
        os.system("sudo python3 AnonGT.py rvmac")
        main_menu()
    if choice == "oniongen":
        os.system("sudo python3 AnonGT.py oniongen")
        main_menu()
    if choice == "checko":
        os.system("sudo python3 AnonGT.py checko")
        main_menu()
    if choice == "share":
        os.system("sudo python3 AnonGT.py share")
        main_menu()
    if choice == "receive":
        os.system("sudo python3 AnonGT.py receive")
        main_menu()
    if choice == "chat":
        os.system("sudo python3 AnonGT.py chat")
        main_menu()
    if choice == "website":
        os.system("sudo python3 AnonGT.py website")
        main_menu()
    if choice == "wipe":
        os.system("sudo python3 AnonGT.py wipe")
        main_menu()
    if choice == "fix":
        os.system("sudo python3 AnonGT.py fix")
        main_menu()
    if choice == "checku":
        os.system("sudo python3 AnonGT.py checku")
        main_menu()
    if choice == "about":
        os.system("sudo python3 AnonGT.py about")
        main_menu()
    elif choice == "6":
        exit()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        change()
        main_menu() 

if __name__ == "__main__":
    main()    
