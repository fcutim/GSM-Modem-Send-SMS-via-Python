#——————————————————
import time     # |
import serial   # |
import sys      # > Important modules for the program to work.
import os       # > These may NOT be deleted or changed!
import socket   # |
import random   # | 
#——————————————————


# Important: > Everything you can change is marked in the code. But if you want to avoid possible mistakes, just don't change anything.


# Info: > Further updates regarding the "status" command will follow. Updates will be automatically uploaded to the program in the future.
# If this is not the case in the future, please check out my GitHub. The latest updates will then be published there.

# Info: > If you get error codes, please also have a look at my GitHub. There you will find all the solutions for possible error codes.

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
    nummern = "01234567890" # You can include other symbols, letters, etc. here. You can change any number between the "". Not more!

    string = nummern
    length = 8 # Here you can change the length of the random password
    password = "".join(random.sample(string,length))
    print("""
    status: Get the status of the module

     smst: Send a text to a desired number

     sms: Send an 8-digit code to a desired number

     help: Get help
    """)
    ans=input("What do you want to do? \n > ")
    if ans=="status":
        phone = serial.Serial("COM7",  9600, timeout=5) # Here you have to change the COM port. Depending on where you plugged in the module.


        try: # If a connection could be established, continue from here
            time.sleep(0.5) # Wait
            phone.write(b'AT\r') # Here the program queries the status of the module. "OK" means that everything is ready and the module can now be used.
            time.sleep(0.5) # Wait
            phone.write(bytes([26])) # Number of Bytes 
            time.sleep(0.5) # Wait
            print(bcolors.OKGREEN + "Module is ready for use and all commands have been loaded successfully!" + bcolors.ENDC)
        finally:
            phone.close() # This completes our requested operation.

    elif ans=="smst": # command (this can be freely defined, but shouldn't)
        recipient = input("Number : ") # Here we ask for the number to send a text to
        message = input("Message : ") # Here we ask for the text to be sent to the number

        phone = serial.Serial("COM7",  9600, timeout=5) # Here you have to change the COM port. Depending on where you plugged in the module. 


        try: # If a connection could be established, continue from here
            time.sleep(0.5) # Wait
            phone.write(b'ATZ\r') # Status test / program could already fail here
            time.sleep(0.5) # Wait
            phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r') # Send SMS command / encode text to binary
            time.sleep(0.5) # Wait
            phone.write(message.encode() + b"\r") # encode message
            time.sleep(0.5) # Wait
            phone.write(bytes([26])) # Number of Bytes
            time.sleep(0.5) # Wait
        finally:
            phone.close() #This completes our requested process.
                
    elif ans=="sms": # Command (This can be freely defined, but shouldn't!)
        recipient = input("Number : ") # Here we ask for the number to which a text should be sent
        
        phone = serial.Serial("COM7",  9600, timeout=5) # Here you have to change the COM port. Depending on where you plugged in the module. 


        try: # If a connection could be established, continue from here
            time.sleep(0.5) # Wait
            phone.write(b'ATZ\r') # Status test / program could already fail here
            time.sleep(0.5) # Wait
            phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r') # Send SMS command / encode text to binary
            time.sleep(0.5) # Wait
            phone.write(password.encode() + b"\r") # encode message
            time.sleep(0.5) # Wait
            phone.write(bytes([26])) # Number of Bytes 
            time.sleep(0.5) # Wait
        finally:
            phone.close() #This completes our requested process.

    elif ans=="help": # Command (This can be freely defined, but shouldn't!)
        print("")
        print("")
        print("You can find help on my GitHub: ") # It's best to leave this message as it is
        print("https://github.com/fcutim/GSM-Modem-Send-SMS-via-Python/issues") # It is best to leave this link in case an error code should occur
        print("")
        print("")

        time.sleep(3) # Wait before the menu is displayed again. (Can also be set after each individual command)

    else:
        print("")
        print("")
        print("———————————————————————————————————————————————")
        print("")
        print("")
        print(bcolors.FAIL + "Error!" + bcolors.ENDC) # Error message if an error should occur. (Can be freely defined)
        print("")
        print("Error Code:", bcolors.FAIL + "0x8024043D" + bcolors.ENDC) # This error code must not be changed, otherwise the error may not be recognizable. You can find a list of all error codes on my GitHub. (https://github.com/fcutim/GSM-Modem-Send-SMS-via-Python/issues)
        print("")
        print(bcolors.UNDERLINE + "The menu will reload in 5 seconds" + bcolors.ENDC) # This message can be freely defined or deleted
        print("")
        print("")
        print("———————————————————————————————————————————————")
        print("")
        print("")
        time.sleep(5)

#—————————————————————————————
#recipient = "+4915906495433" > This was a test of the previous version.
#message = "Test"             > It can be safely deleted.
#—————————————————————————————

phone = serial.Serial("COM7",  9600, timeout=5) # Here you have to change the COM port. Depending on where you plugged in the module. 


