import sys
import os
import getpass


class c:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


type = sys.argv[1]
os.chdir(f"/home/{getpass.getuser()}/.local/")


def main():
    if type == "add":
        with open("bcpip.mods", "a") as file:
            moduleName = sys.argv[2]
            file.write(f"pip install {moduleName}\n")
            print(
                f"{c.OKGREEN}Successfully added {moduleName} to the Install list.{c.ENDC}")
    if type == "clear-list":
        with open("bcpip.mods", "w") as file:
            file.write("")
            print(
                f"{c.OKGREEN}Successfully removed all packages from the Install list.{c.ENDC}")
    if type == "commit":
        with open("bcpip.mods", "r") as file:
            leng = 0
            for line in file.readlines():
                leng += 1
                if len(line) > 2:
                    try:
                        os.system(line)
                    except Exception:
                        print(
                            f"{c.FAIL}Failed to install package {leng}.{c.ENDC}")
                else:
                    pass
        with open("bcpip.mods", "w") as file:
            file.write("")
            print(f"{c.OKGREEN}Cleared the Install list.{c.ENDC}")
    if type == "list-install":
        with open("bcpip.mods", "r") as file:
            text = file.readlines()
            count = 0
            for line in text:
                count += 1
                if (count % 2) == 0:
                    sys.stdout.write(c.OKBLUE+line+c.ENDC)
                else:
                    sys.stdout.write(c.OKGREEN+line+c.ENDC)
