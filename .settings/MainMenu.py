import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools1")
os.system("bash Logo.sh")
os.system("bash src/MenuOps1.sh")

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"

g="\033[1;32m"
r="\033[1;31m"
w="\033[0m"
b="\033[1;34m"
o="\033[1;33m"
bl="\033[1;36;40m"

op=int(raw_input("Options: "))
if(op==1):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools1 && python3 .check/IpMenuConfig.py")
elif(op==2):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python3 Files/RouterMenu.py")
elif(op==3):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python3 Files/MailMenu.py")
elif(op==4):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python3 Files/WebMenu.py")
elif(op==5):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python3 Files/CamHackMenu.py")
elif(op==6):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python3 Files/AndroidMenu.py")
elif(op==7):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python3 Files/SQLinjectionMenu.py")
elif(op==8):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python3 Files/SocialMenu.py")
elif(op==9):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python3 Files/SpamMenu.py")
elif(op==10):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python3 Files/AnalistickMenu.py")
elif(op==11):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python3 Files/DarkSearchMenu.py")
elif(op==12):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python3 Files/PhishingMenu.py")
elif(op==13):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("python3 Files/PassworldMenu.py")
elif(op==14):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools1 && python3 Files/WordlistGeneratorMenu.py")
elif(op==15):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools1 && python3 Files/XSSAttackMenu.py")
elif(op==16):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools1 && python3 Files/discordMenu.py")
elif(op==17):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools1 && python3 Files/telegramMenu.py")
elif(op==18):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools1 && python3 .check/OtherToolConfig.py")
elif(op==19):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools1 && python3 .check/TermuxPanelConfig.py")
elif(op==20):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools1 && python3 .settings/settingsMenu.py")
elif(op==21):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("clear && cd && cd AllHackingTools1 && bash .settings/LICENSE.sh && cd && cd AllHackingTools1 && python3 src/Timer2.py && python3 MainMenu.py")
elif(op==22):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 time.sleep(1)
 os.system("cd && cd AllHackingTools1 && python3 .check/UpdaterConfig.py")
elif(op==23):
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("bash src/About.sh")
elif(op==13324715):
 print("[DEBUG] Developer mode successfully enabled!")
 time.sleep(0.8)
 os.system("cd && cd AllHackingTools1 && cd .settings && mv DesingLogo.py /data/data/com.termux/files/home/AllHackingTools1/.temp/ && mv DesingMenu.py /data/data/com.termux/files/home/AllHackingTools1/.temp/")
 print("[DEBUG] Please restart AllHackingTools1!")
 os.system("cd && cd AllHackingTools1 && mv MainMenu.py /data/data/com.termux/files/home/AllHackingTools1/.temp/temp && cd .settings && cd debug && cp MainMenu.py /data/data/com.termux/files/home/AllHackingTools1/")
 print("[DEBUG] Warning! Customization has been disabled.")
elif(op==24):
 os.system("clear && cd && cd AllHackingTools1 && bash Logo.sh")
 print("\033[1;31;40mExiting System...")
 time.sleep(0.7)
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTool1")
 os.system("python2 MainMenu.py")
