#freedom_reborn
#jstfreenet
#vpnkacang
import sys, os, time, io, re, traceback, warnings, weakref, collections.abc
import linecache
from token import *
import tokenize
import logging
import time
import urllib3
import random
import threading
import itertools
import urllib.parse
import token
import requests
from random import randint
import os
import sys
os.system('clear')
#kodewarna_anjim
grey = '\x1b[90m'
red = '\x1b[91m'
green = '\x1b[92m'
yellow = '\x1b[93m'
blue = '\x1b[94m'
purple = '\x1b[95m'
cyan = '\x1b[96m'
white = '\x1b[37m'
flag = '\x1b[41;39m'
asem = '\x1b[47;30m'
bold = '\033[1m'
normal = '\033[0m'
off = '\x1b[m'
#logonya
logo = f"{blue}IIIII  TTTTTTT   SSSSS\n{purple} III     TTT    SS\n{cyan} III     TTT     SSSSS\n{white} III     TTT         SS\nIIIII    TTT     SSSSS"
bawah = f"{flag}     TOKEN GENERATOR     {off}"

#loading_njim
done = False

def animate():
    for c in itertools.cycle(['0%', '5%', '7%', '10%', '12%', '14%', '15%', '20%', '22%', '24%', '25%', '30%', '32%', '35%', '37%', '40%', '45%', '50%', '55%', '56%', '58%', '60%', '65%', '70%', '75%', '80%', '85%', '90%', '95%', '100%']):
        if done:
            break
        else:
            sys.stdout.write(f"\r{green}\rLoading {off}: " + c)
            sys.stdout.flush()
            time.sleep(0.1)
    else:
        sys.stdout.write('\rSELESAI     ')

t = threading.Thread(target=animate)
t.start()
time.sleep(3)
done = True
os.system('clear')
#mengetik_njim
time.sleep(0.8)

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.04)


mengetik(f"{green}SELAMAT DATANG SEMUANYA")
time.sleep(0.2)
mengetik(f"{yellow}Token ITS {purple}GRATIS!!")
time.sleep(0.2)
mengetik(f"{yellow}reset setiap satu jam sekali\n{green}Special thanks to :")
time.sleep(0.2)
mengetik(f"{purple}@sanzkking2 {off}[{green}sanzking{off}]")
time.sleep(0.1)
mengetik(f"{purple}@incorrect_cuy {off}[{green}Incorrect username or password vpn{off}]")
time.sleep(0.1)
mengetik(f"{purple}@EmIliaHikarY {off}[{green}DimasDm{off}]")
time.sleep(0.1)
mengetik(f"{purple}@fazone {off}[{green}fazone{off}]")
time.sleep(0.1)
mengetik(f"{purple}@RobertBetaica {off}[{green}Pikachu{off}]")
time.sleep(0.1)
mengetik(f"{purple}@ICIPERS {off}[{green}Galuh pawestri{off}]")
time.sleep(0.1)
mengetik(f"{yellow}@freedom_reborn {off}[{green}FREEDOM REBORN{off}]")
time.sleep(0.1)
mengetik(f"{white}@JSTFREENET {off}[{green}Jst-team{off}]")
time.sleep(0.1)
mengetik(f"{red}@configarea {off}[{green}vpnkacang{off}]")
time.sleep(0.1)
mengetik(f"")
time.sleep(1)
mengetik(f"{cyan}SELAMAT MENGGUNAKAN{off}")
time.sleep(2)
os.system('clear')
#menu_utama
print(logo)
print(bawah)
print()
print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print(f"{asem} Mainmenu :{off}")
print(f"{green}[{yellow}1{green}]{white}TOKEN ITS")
print(f"—————————————————————————")
print(f"{asem} Support us :{off}")
print(f"{green}[{yellow}2{green}]{white}Join group")
print(f"{green}[{yellow}3{green}]{white}Join channel")
print(f"{green}[{red}4{green}]{white}Subscribe YouTube")
print(f"{red}[{yellow}0{red}]{red}Keluar")
print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
inv = input(f"{purple}>>>{off} Pilih > ")
if inv == '1':
	print()
	print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
	print(f"\r{yellow}[{red}info{yellow}]{white}1x run = 2x generate")
	print(f"\r{yellow}[{red}info{yellow}]{white}Reset setiap 1 jam sekali")
	print(f"—————————————————————————————————")
	print()
	url = 'https://raw.githubusercontent.com/sanzking212/token/main/1(2).txt'
	r = requests.get(url)
	text = r.text
	individual_words = text.split()
	random_number = randint(0, len(individual_words))
	print(f"\r{green}[{blue}TOKEN 1{green}] {off}=> " + individual_words[random_number])
	print()
	print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
	print()
	print(f"{green}[{red}1{green}]{white}Generate")
	print(f"—————————————————————————")
	inv = input(f"{purple}>>>{white} Pilih > ")
	print(f"—————————————————————————")
	print()
	if inv == '1':
	    random_number = randint(0, len(individual_words))
	    print(f"\r{green}[{blue}TOKEN 2{green}] {off}=> " + individual_words[random_number])
	    print()
	    print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
	else:
		exit()
		
	exit(f"{green}[{yellow}✓{green}]{white}Terimakasih telah menggunakan layanan ini\n{green}[{yellow}✓{green}]{white}Nantikan update pada jam berikutnya\n{green}[{blue}!{green}]{white}Pantau terus channel kami\n{green}>> vpnkacang\n{cyan}>> JSTFREENET\n{yellow}>> freedom'x{off}")
elif inv == '2':
	print(f"{green}[{red}1{green}]{white}freedom reborn")
	print(f"{green}[{red}2{green}]{white}jst team")
	print(f"{green}[{red}3{green}]{white}vpnkacang")
	inv = input(f"{purple}>>>{white} Pilih > ")
	if inv == '1':
		os.system(f"xdg-open https://t.me/freedom_reborn")
	elif inv == '2':
		os.system(f"xdg-open https://t.me/JSTFREENET")
	elif inv == '3':
		os.system(f"xdg-open https://t.me/configarea")
elif inv == '3':
	print(f"{green}[{red}1{green}]{white}freedom'x channel")
	print(f"{green}[{red}2{green}]{white}jst freenet • channel")
	print(f"{green}[{red}3{green}]{white}vpnkacang channel")
	inv = input(f"{purple}>>>{white} Pilih > ")
	if inv == '1':
		os.system(f"xdg-open https://t.me/freedomx_channel")
	elif inv == '2':
		os.system(f"xdg-open https://t.me/channelJST")
	elif inv == '3':
		os.system(f"xdg-open https://t.me/cnfgfree")
elif inv == '4':
	print(f"{red}>>> {white} SUBSCRIBE CHANNEL JST {red}<<<{off}")
	os.system(f"xdg-open https://youtu.be/7f6PJB6V-Mo")
elif inv == '0':
	exit(f"{red}Terimakasih telah menggunakan tools kami")
	
#Jangan_lupa_join_grup_sama_channel_telenya_cuk
#SANZKING
