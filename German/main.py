#——————————————————
import time     # |
import serial   # |
import sys      # > Wichtige Module, damit das Programm funktioniert.
import os       # > Diese dürfen NICHT gelöscht oder geändert werden!
import socket   # |
import random   # | 
#——————————————————


# Wichtig: > Alles was du ändern kannst ist im Code gekennzeichnet. Wenn du aber mögliche Fehler vermeiden willst, ändere einfach nichts.


# Info: > Weitere Updates bezüglich dem Command "status" folgen. Updates werden in zukunft Automatisch auf das Programm aufgespielt
#         Falls dies in Zukunft nicht der Fall ist, schaue bitte auf meinem GitHub vorbei. Dort werden dann die neusten Updates veröffentlicht.

# Info: > Solltest du Fehler Codes bekommen, schaue bitte ebenfalls auf meinem GitHub vorbei. Dort findest du alle Lösungen für mögliche Fehler Codes.

# Made by Tim B.

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ans=True
while ans:
    nummern = "01234567890" # Hier kannst du andere Symbole, Buchstaben etc. einbinden. Du kannst alle Zahlen zwischen den "" ändern. Mehr nicht!

    string = nummern
    length = 8 # Hier kannst du die länge des zufälligem Passwortes ändern 
    password = "".join(random.sample(string,length))
    print("""
    status: Erhalte den Status von dem Modul

    smst: Sende einen Text an eine gewünschte Nummer

    sms: Sende einen 8-Stelligen Code an eine gewünschte Nummer

    help: Erhalte Hilfe
    """)
    ans=input("Was möchtest du tun? \n > ")
    if ans=="status":
        phone = serial.Serial("COM7",  9600, timeout=5) # Hier musst du den COM Port ändern. Jenachdem, wo du das Modul angesteckt hast. 


        try: # Wenn eine Verbindung hergestellt werden konnte, wird ab hier weiter gemacht
            time.sleep(0.5) # Warten
            phone.write(b'AT\r') # Hier fragt das Program den Status von dem Modul ab "OK" bedeutet das alles bereit ist und das Modul nun genutzt werden kann.
            time.sleep(0.5) # Warten
            phone.write(bytes([26])) # Anzahl der Bytes 
            time.sleep(0.5) # Warten
            print(bcolors.OKGREEN + "Modul ist einsatzbereit und alle Befehle wurden erfolgreich geladen!" + bcolors.ENDC)
        finally:
            phone.close() # Hiermit schließen wir unseren angeforderten Vorgang ab. 

    elif ans=="smst": # Befehl (Dieser kann frei definiert werden, sollte aber nicht)
        recipient = input("Nummer : ") # Hier fragen wir nach der Nummer an die ein Text geschickt werden soll
        message = input("Nachricht : ") # Hier fragen wir nach dem Text der an die Nummer gesendet werden soll 

        phone = serial.Serial("COM7",  9600, timeout=5) # Hier musst du den COM Port ändern. Jenachdem, wo du das Modul angesteckt hast. 


        try:
            time.sleep(0.5) # Warten
            phone.write(b'ATZ\r') # Status Test / Programm könnte hier schon Failen
            time.sleep(0.5) # Warten
            phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r') # Befehl für SMS senden / Text zu Binary encodieren
            time.sleep(0.5) # Warten
            phone.write(message.encode() + b"\r") # Nachricht encodieren
            time.sleep(0.5) # Warten
            phone.write(bytes([26])) # Anzahl der Bytes 
            time.sleep(0.5) # Warten
        finally:
            phone.close() # Hiermit schließen wir unseren angeforderten Vorgang ab.
                
    elif ans=="sms": # Befehl (Dieser kann frei definiert werden, sollte aber nicht!)
        recipient = input("Nummer : ") # Hier fragen wir nach der Nummer an die ein Text geschickt werden soll
        
        phone = serial.Serial("COM7",  9600, timeout=5) # Hier musst du den COM Port ändern. Jenachdem, wo du das Modul angesteckt hast. 


        try:
            time.sleep(0.5) # Warten
            phone.write(b'ATZ\r') # Status Test / Programm könnte hier schon Failen
            time.sleep(0.5) # Warten
            phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r') # Befehl für SMS senden / Text zu Binary encodieren
            time.sleep(0.5) # Warten
            phone.write(password.encode() + b"\r") # Nachricht encodieren
            time.sleep(0.5) # Warten
            phone.write(bytes([26])) # Anzahl der Bytes 
            time.sleep(0.5) # Warten
        finally:
            phone.close() # Hiermit schließen wir unseren angeforderten Vorgang ab.

    elif ans=="help": # Befehl (Dieser kann frei definiert werden, sollte aber nicht!)
        print("")
        print("")
        print("Hilfe findest du auf meinem GitHub: ") # Diese Nachricht am besten so lassen
        print("https://github.com/fcutim/GSM-Modem-Send-SMS-via-Python/issues") # Diesen Link sollte man am besten lassen, falls es mal zu einem Fehlercode kommen sollte
        print("")
        print("")

        time.sleep(3) # Warten bevor das Menü wieder angezeigt wird. (Kann auch nach jedem einzelnden Command gesetzt werden)

    else:
        print("")
        print("")
        print("———————————————————————————————————————————————")
        print("")
        print("")
        print(bcolors.FAIL + "Fehler!" + bcolors.ENDC) # Fehler Nachricht, falls ein Fehler auftreten sollte. (Kann frei definiert werden)
        print("")
        print("Error Code:", bcolors.FAIL + "0x8024043D" + bcolors.ENDC) # Dieser Fehlercode darf nicht geändert werden, da er sonst möglicherweise der Fehler nicht wiedererkannt werden kann. Eine liste aller Fehlercodes findest du auf meinem GitHub. (https://github.com/fcutim/GSM-Modem-Send-SMS-via-Python/issues)
        print("")
        print(bcolors.UNDERLINE + "Das Menü wird in 5 Sekunden geladen!" + bcolors.ENDC) # Diese Nachricht kann frei definiert oder auch gelöscht werden
        print("")
        print("")
        print("———————————————————————————————————————————————")
        print("")
        print("")
        time.sleep(5)

#—————————————————————————————
#recipient = "+4915906495433" > Dies war ein Test der vorgänger Version.
#message = "Test"             > Es kann ohne bedenken gelöscht werden. 
#—————————————————————————————

phone = serial.Serial("COM7",  9600, timeout=5) # Hier musst du den COM Port ändern. Jenachdem, wo du das Modul angesteckt hast. 


