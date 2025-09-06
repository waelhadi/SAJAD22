import requests,random,datetime,binascii,os,threading,names,secrets,sys
import hashlib
import json
import time
from urllib.parse   import urlencode
import requests,sys,os,time
import requests
import sys
import time
import pyfiglet
from termcolor import colored
from colorama import init, Fore, Style
import requests
from colorama import init, Fore
import re
session = requests.Session()
soso = []
loop = []
tar = []
x_ = []
ls = []
sisn = []  # نبدأ بقائمة فارغة


# ألوان الطرفية
import os
import pyfiglet
from termcolor import colored

# مسح الشاشة
os.system('cls' if os.name == 'nt' else 'clear')

# طباعة الشعار
hakm_logo = pyfiglet.figlet_format("NASR")
print(colored(hakm_logo, "cyan"))
print(colored("معرّف المطوّر: @NASR101", "cyan"))
# قراءة السيزنات من الملف
file_path = '1.txt'
if os.path.isfile(file_path):
    with open(file_path, 'r') as f:
        sisn = [line.strip() for line in f if line.strip()]
else:
    sisn = []
    print("⚠️ File not found!")
