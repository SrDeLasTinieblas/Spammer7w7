import os
import keyboard
import time

def banner():
    os.system('clear')
    print( "Author : SrDeLasTinieblas")
    print('''

  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$  /$$      /$$ /$$$$$$$  /$$$$$$$$
 /$$__  $$| $$  / $$ /$$__  $$| $$__  $$ /$$__  $$|__  $$__//$$__  $$| $$$    /$$$| $$__  $$| $$_____/
| $$  \ $$|  $$/ $$/| $$  \ $$| $$  \ $$| $$  \ $$   | $$  | $$  \ $$| $$$$  /$$$$| $$  \ $$| $$      
| $$$$$$$$ \  $$$$/ | $$  | $$| $$$$$$$/| $$  | $$   | $$  | $$$$$$$$| $$ $$/$$ $$| $$$$$$$/| $$$$$   
| $$__  $$  >$$  $$ | $$  | $$| $$____/ | $$  | $$   | $$  | $$__  $$| $$  $$$| $$| $$__  $$| $$__/   
| $$  | $$ /$$/\  $$| $$  | $$| $$      | $$  | $$   | $$  | $$  | $$| $$\  $ | $$| $$  \ $$| $$      
| $$  | $$| $$  \ $$|  $$$$$$/| $$      |  $$$$$$/   | $$  | $$  | $$| $$ \/  | $$| $$  | $$| $$$$$$$$
|__/  |__/|__/  |__/ \______/ |__/       \______/    |__/  |__/  |__/|__/     |__/|__/  |__/|________/
-------------------   ----------------------------   -------------------------------------------------
''')
os.system('clear')
banner()
time.sleep(0.25)
os.system('clear')
banner()
time.sleep(0.25)
os.system('clear')
banner()
time.sleep(0.25)
os.system('clear')
banner()
m = (int(input(" 1 Mensaje o 2 mensajes? (1 or 2): ")))
if m == 1:
    print("\t \n*** 1 Mensaje ***\n")
    m1 = (str(input("ingrese el mensaje : ")))
    r = (int(input("ingrese la cantidad de mensajes : ")))

    print("Desde ahora tienes 5 segundos para darle click donde quieras el spam")
    time.sleep(5)

    for i in range(r):
        keyboard.write(m1)
        keyboard.press_and_release('enter')

    print("\t \n +++ Successful +++ \n")

elif m == 2:
    print("\t \n*** 2 Mensajes ***\n")
    m1 = (str(input("ingrese el primer mensaje : ")))
    m2 = (str(input("ingrese el segundo mensaje : ")))
    r = (int(input("ingrese la cantidad de mensaje : ")))

    print("\nDesde ahora tienes 5 segundos para darle click donde quieras el spam")

    time.sleep(5)

    for i in range(r):
        keyboard.write(m1)
        keyboard.press_and_release('enter')
        keyboard.write(m2)
        keyboard.press_and_release('enter')
    print("\t \n +++ Successful +++\n")
