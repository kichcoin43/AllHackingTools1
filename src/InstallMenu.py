import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools1 && bash src/LiteLogo.sh")

print("")
print("  \033[1;34m[01] \033[1;36;40mDefault  -  Standart installing and default")
print("  \033[1;34m[02] \033[1;36;40mCoded  -  Install via encoded code NOT RECOMMENDED")
print("  \033[1;34m[02] \033[1;36;40mQuit  -  Exit and do not download AllHackingTools1")

op=int(input("1nStall: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools1 && bash Files/Modules.sh")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools1 && bash Files/CodedModules.sh")
elif(op==2):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting AllHackingTool1 Installer...")
 sys.exit()
else:
 print("\033[1;31;40mInvalid input. Quiting AllHackingTools1 Installer") 
 time.sleep(0.8)
