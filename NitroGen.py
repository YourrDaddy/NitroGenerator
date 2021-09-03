import random
import requests
import string
from colorama import Fore, Style, init

init(convert=True)

print(f"""{Fore.LIGHTYELLOW_EX}
                                        ╔╦╗╔═╗╔╦╗╔╦╗╦ ╦  ╔╗╔╦╔╦╗╦═╗╔═╗  ╔═╗╔═╗╔╗╔
                                         ║║╠═╣ ║║ ║║╚╦╝  ║║║║ ║ ╠╦╝║ ║  ║ ╦║╣ ║║║
                                        ═╩╝╩ ╩═╩╝═╩╝ ╩   ╝╚╝╩ ╩ ╩╚═╚═╝  ╚═╝╚═╝╝╚╝
""")
print()
Quantity = int(input("How many codes you want to generate : "))
print()

try:
    val = int(Quantity)
except ValueError:
    print("That's not an int!")


for i in range(Quantity):
    nitro = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase,k = 16))
    url = ("https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro)
    urltosee = ("https://discord.gift/" + nitro)
    check = requests.get(url)
    
    if check.status_code == 200:
        print("[VALID CODE] : " + urltosee)
        f = open("ValidCodes.txt", "a")
        f.write(f"{urltosee}")
        f.close()

    else:
        print("[INVALID CODE] : " + urltosee)

    
    
