#imports necessary libraries
import subprocess
import time
from pynput.keyboard import Controller

#type the name of your printers in printer1 and printer2
#if you have more printers just add printer3 and so on
printer1 = ""
printer2 = ""
#set number of printers you have
numberOfPrinters = 2
printer = ""
key = Controller()

#reads which printer needs to be switched to
f = open(r".\printers.txt")
x = int(f.read())

#increments to the next printer and writes it to txt file
x += 1
if x > numberOfPrinters: 
    x = 1

f = open(r".\printers.txt", "w")
f.write(str(x))

#checks which printer needs to be switched to
if x == 1:
    printer += printer1
if x == 2:
    printer += printer2

#changes the default printer
subprocess.run(["start"], shell=True)
time.sleep(0.1)
key.type(f'wmic printer where name="{printer}" call setdefaultprinter & exit\n')


#Charles Dahl, 2022.
