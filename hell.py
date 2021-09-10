import discord
import colorama
from colorama import Fore
from colorama import Back
from colorama import Style
import os
os.system("mode con cols=77 lines=27")
import requests
import time
import random
import init
import sys
import subprocess

import asyncio
import datetime
import functools
import io
import json
import os

cmd = 'mode 70,20'
os.system(cmd)
import random
import re
import string
import urllib.parse
import urllib.request
import time
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4
from os import system
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("ℍ𝕖𝕝𝕝𝕤 ℂ𝕠𝕣𝕡")
import aiohttp
import colorama
import discord
import numpy
import requests
from PIL import Image
from colorama import Fore
from discord.ext import commands
from discord.utils import get
from gtts import gTTS


#made by el peaky and el pacho#0002


with open('hellscorbottool') as f:



  client = discord.Client()

def Clear():
    os.system('')
Clear()


print(f"""{Fore.GREEN}{Style.BRIGHT}


 __   __  _______  ___      ___      _______    _______  _______  ______    _______ 
|  | |  ||       ||   |    |   |    |       |  |       ||       ||    _ |  |       |
|  |_|  ||    ___||   |    |   |    |  _____|  |       ||   _   ||   | ||  |    _  |
|       ||   |___ |   |    |   |    | |_____   |       ||  | |  ||   |_||_ |   |_| |
|       ||    ___||   |___ |   |___ |_____  |  |      _||  |_|  ||    __  ||    ___|
|   _   ||   |___ |       ||       | _____| |  |     |_ |       ||   |  | ||   |    
|__| |__||_______||_______||_______||_______|  |_______||_______||___|  |_||___|    


""")  

token = input(f"{Fore.GREEN}{Style.BRIGHT}~HellsCorp{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}token{Fore.WHITE}> ")
head = {'Authorization': str(token)}
headers = {'Authorization': token, 'Content-Type': 'application/json'} 
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head) 

if src.status_code == 401:
        print(f"{Fore.GREEN}{Style.BRIGHT}~token{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}invalid{Fore.WHITE}... ")
        exit()
elif src.status_code == 200:
        print(f"{Fore.GREEN}{Style.BRIGHT}~token{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}accepted{Fore.WHITE}... ")
else:
        print(f"{Fore.GREEN}{Style.BRIGHT}~internal{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}error{Fore.WHITE}: ")
        input()
        exit()

while True:
    T = input(f"{Fore.GREEN}{Style.BRIGHT}~HellsCorp{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}message{Fore.WHITE}> ")
    if T=="text":
        exit(0)
    else:
        print(f"{Fore.GREEN}{Style.BRIGHT}~HellsCorp{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}loading{Fore.WHITE}... ")
        break

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send (T)
      print(f"{Fore.GREEN}{Style.BRIGHT}~tbk{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}sentmsg{Fore.WHITE}: {user.name}")
    except:
       print(f"{Fore.GREEN}{Style.BRIGHT}~tbk{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}failedmsg{Fore.WHITE}: {user.name}")

time.sleep(2)

print(f'''{Fore.GREEN}{Style.BRIGHT}                                                      



  o                        o    o                                       
 <|>                      <|>  <|>                                      
 / >                      / \  / \                                      
 \o__ __o      o__  __o   \o/  \o/      __o__     \o_ __o     o      o  
  |     v\    /v      |>   |    |      />  \       |    v\   <|>    <|> 
 / \     <\  />      //   / \  / \     \o         / \    <\  < >    < > 
 \o/     o/  \o    o/     \o/  \o/      v\    o   \o/     /   \o    o/  
  |     <|    v\  /v __o   |    |        <\  <|>   |     o     v\  /v   
 / \    / \    <\/> __/>  / \  / \  _\o__</  < >  / \ __/>      <\/>    
                                                  \o/            /      
                                                   |            o       
                                                  / \        __/>      
    
    ''')


print(f"{Fore.GREEN}{Style.BRIGHT}~HellsCorp{Fore.WHITE}@{Fore.GREEN}{Style.BRIGHT}loading{Fore.WHITE}... ")

