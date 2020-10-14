import requests
from colorama import Fore, Back, init
from datetime import datetime
import subprocess
import os


f = open('result/live.txt','w')
a = input('')
f.write('answer:'+str(a))
f.close()

time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')



print(Fore.RED + """
 			       ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████  ▄███████▄   ▄██████▄  ███▄▄▄▄   
                               ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ██▀     ▄██ ███    ███ ███▀▀▀██▄ 
                               ███    ███ ███   ███   ███   ███    ███       ▄███▀ ███    ███ ███   ███ 
                               ███    ███ ███   ███   ███   ███    ███  ▀█▀▄███▀▄▄ ███    ███ ███   ███ 
                             ▀███████████ ███   ███   ███ ▀███████████   ▄███▀   ▀ ███    ███ ███   ███ 
                               ███    ███ ███   ███   ███   ███    ███ ▄███▀       ███    ███ ███   ███ 
                               ███    ███ ███   ███   ███   ███    ███ ███▄     ▄█ ███    ███ ███   ███ 
                               ███    █▀   ▀█   ███   █▀    ███    █▀   ▀████████▀  ▀██████▀   ▀█   █▀  
                                                                           
                     				Amazon VAILD EMAIL CHECKER    |   Full VERSION v1     |  Coded by Ahmed Tahoon  [ X E O N ] """)


print(Fore.GREEN + """                           				                [+] Telegram: @xe0on[+]
		           				                        [+] Basem Elwazer @xeon_support[+]
		           				                        [+] Thats Free Tool In GitHub  [+]
		           				                        [+]https://github.com/XEON-LORD/amz-vaild-python-3 [+]


            					                +-------- With Great Power Comes Great Toolz! --------+  
                                     +-------------------------------------- XEON-------------------------------+

       """)
def GetUUID():
   cmd = 'wmic csproduct get uuid'
   uuid = str(subprocess.check_output(cmd))
   pos1 = uuid.find("\\n")+2
   uuid = uuid[pos1:-15]
   return uuid
print(Fore.LIGHTMAGENTA_EX + 'Hello There Your Api is verifyng by our system now ...... ''' )
print('==============================================================================================================================')
print('YOUR API IS VAILD ! :- ' +Fore.LIGHTBLACK_EX + GetUUID())
with open(input(Fore.RED + 'Enter Your Combo Path : '), 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.read().split('\n')
for line in lines:
    if len(line.split(':')) == 1:
        email = line.split(':')[0]
        url = f'http://maxcheckers.pw/app/amz-x.php?email={email}'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
        ch = requests.get(url, headers=headers).text

        if """status":"invalid""" in ch:
            print(Fore.RED + f'[+] ' + time + ' - DIE - ' + email + ' - [AMAZON Email Checker - 1.1]')
            amz_die = open('result/die.txt', 'a')
            amz_die.write(email + '\n')
        elif """status":"live""" in ch:
            print(Fore.GREEN + f'[+] ' + time + ' - LIVE - ' + email + ' - [AMAZON Email Checker - 1.1]')
            Amaz_Valid = open('result/live.txt', 'a')
            Amaz_Valid.write(email + '\n')
            pass
        else:
            print(Fore.YELLOW + f'[-] {email} --- [ Error ]')
            amz_unk = open('result/unknown.txt', 'a')
            amz_unk.write(email + '\n')

            print("""
            
            """)
