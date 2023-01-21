import requests
import time
import utils

from time import sleep
from utils import user, SlowPrint
from colorama import Fore, Back, Style
from dhooks import Webhook, File, Embed


utils.webhoopktoolasciiintro()
SlowPrint(Fore.RED + "Webhook url \n")
webhook = input (Fore.CYAN + Style.BRIGHT + "    |\n" + "    └─ " + user + " → " + Style.RESET_ALL + Fore.RESET)
hook = Webhook(webhook)

utils.webhoopkcheck()
check = requests.get(webhook)
if check.status_code == 404:
    SlowPrint(Fore.RED + Style.BRIGHT + "\nWebhook not existing!\nPlease put a valid wehbook." + Style.RESET_ALL + Fore.RESET)
    time.sleep(3)
elif check.status_code == 200:
    SlowPrint(Fore.GREEN + Style.BRIGHT + "\nCorrect Webhook!" + Style.RESET_ALL + Fore.RESET)
    
    def main():
        utils.webhoopktoolasciiintro()
        SlowPrint(Fore.RED +"\nIf you want to delete the webhook press 1,\nIf you want to spam the webhook press 2,\n\n")
        choice = input (Fore.CYAN + Style.BRIGHT + "                |\n" + "                └─ " + user + " → " + Style.RESET_ALL + Fore.RESET)
        if choice == "1":
            utils.deletingwebhook()
            SlowPrint("Deleting webhook in 1, 2, 3 ...")
            SlowPrint(Fore.RED + "\nDeleting the webhhook " + Fore.RESET + Fore.GREEN + "." + Fore.RESET + Fore.BLUE + "."+ Fore.RESET + Fore.CYAN + "." + Fore.RESET + Fore.MAGENTA +"." + Fore.RESET + Fore.RED + "!" + Fore.RESET)
            hook.send("Webhook got deleted by https://github.com/kizza2")
            requests.delete(webhook)
            checker = requests.get(webhook)
            if checker.status_code == 404:
                SlowPrint(Fore.GREEN + "\nWebhook get sucessfully deleted!" + Fore.RESET)
                time.sleep(4)
        elif choice == "2":
            embed = Embed(
            description='STOP SENDING LOGGERS SKID  GAY :sunglasses:',
            color=0x5CDBF0,
            timetamp='now'
            )
            image2 = 'https://i.imgur.com/K7hZxcm.png'
            image3 = 'https://pbs.twimg.com/media/Bpvdm-QIgAAsoX5.jpg'
            image4 = 'https://i.imgur.com/uAP2Ctf.jpg'
            image5 = 'https://i.imgur.com/IY3kK8M.jpg'
            embed.set_author(name='By|kizzouille#6969| You are CLOWN ', icon_url=image4)
            embed.add_field(name='YOURE A FUCKING CLOWN', value='NOOBY NULLOS SOUS MERDE')
            embed.set_footer(text='FUCK YOU', icon_url=image3)
            embed.set_footer(text='ur so bad', icon_url=image5)
            embed.set_thumbnail(image2)
            embed.set_image(image5)
            ##
            utils.spammingwebhook()
            SlowPrint("Spamming webhook in 1, 2, 3 ...\n")
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            SlowPrint("\u001b[32mSucessfully spammed 5 times!\n")
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            SlowPrint("\u001b[31mSucessfully spammed 10 times!\n")
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            SlowPrint("\u001b[32mSucessfully spammed 15 times!\n")
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            SlowPrint("\u001b[31mSucessfully spammed 20 times!\n")
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            SlowPrint("\u001b[32mSucessfully spammed 25 times!\n")
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            hook.send(embed=embed)
            SlowPrint("\u001b[31mSucessfully spammed 30 times!\n")
            SlowPrint(f"{Fore.RESET}Credit to kizzouille#6969//kizzouille#3606 \n")
            time.sleep(1)
            utils.webhoopktoolasciiintro()
            SlowPrint(Fore.RED + "If you want to spam more press Y\nIf you want to stop the program press N\n" + Fore.RESET)
            morespamrequest = input (Fore.CYAN + Style.BRIGHT + "\n                |\n" + "                └─ " + user + " → " + Style.RESET_ALL + Fore.RESET)
            if morespamrequest =="Y":
                main()
            elif morespamrequest =="N":
                time.sleep(1)
                exit()

    main()
main()