#!/usr/bin/env python3

import os
import itertools
from colorama import Fore
print()
print(Fore.CYAN)
print("#############################################################")
print("#                                                           #")
print("#  ░█▀▄▀█ █▀▀█ █▀▀▄ 　 ░█─░█ █▀▀█ █▀▀ █──█ █▀▀ █▀▀█         #")
print("#  ░█░█░█ █▄▄█ █──█ 　 ░█▀▀█ █▄▄█ ▀▀█ █▀▀█ █▀▀ █▄▄▀         #")
print("#  ░█──░█ ▀──▀ ▀▀▀─ 　 ░█─░█ ▀──▀ ▀▀▀ ▀──▀ ▀▀▀ ▀─▀▀         #")
print("#                                                           #")
print("#############################################################")
print()
print(Fore.GREEN)
print()
print("Types of hash codes: md5sum, sha256sum, etc.")
print()
type = str(input("Enter Hash Type: "))
print()

for make in itertools.count(1,1):
    password = str(input(f"Enter Pasword#{make}: ")) 
    maker = os.system(f'echo -n "{password}" | {type} >> hashfile{type}.txt')