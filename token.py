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
#tai
#logonya
logo = f"{blue}____________________ _______________   __\n{purple}___  __/_  __ \__  //_/__  ____/__  | / /\n{cyan}__  /  _  / / /_  ,<  __  __/  __   |/ / \n{white}_  /   / /_/ /_  /| | _  /___  _  /|  /  \n/_/    \____/ /_/ |_| /_____/  /_/ |_/   "
bawah = f"{flag}     TOKEN ITS DAN UNSRAT GENERATOR     {off}"

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

#def mengetik(s):
    #for c in s + '\n':
        #sys.stdout.write(c)
        #sys.stdout.flush()
       # time.sleep(random.random() * 0.04)


#mengetik(f"{green}SELAMAT DATANG SEMUANYA")
#time.sleep(0.1)
#mengetik(f"{yellow}Token ITS & UNSRAT {purple}GRATIS!!")
#time.sleep(0.1)
#mengetik(f"{yellow}reset setiap satu jam sekali\n{green}Special thanks to :")
#time.sleep(0.1)
#mengetik(f"{purple}@sanzkking2 {off}[{green}sanzking{off}]")
#time.sleep(0.1)
#mengetik(f"{purple}@incorrect_cuy {off}[{green}Incorrect username or password vpn{off}]")
#time.sleep(0.1)
#mengetik(f"{purple}@EmIliaHikarY {off}[{green}DimasDm{off}]")
#time.sleep(0.1)
#mengetik(f"{purple}@fazone {off}[{green}fazone{off}]")
#time.sleep(0.1)
#mengetik(f"{purple}@RobertBetaica {off}[{green}Pikachu{off}]")
#time.sleep(0.1)
#mengetik(f"{purple}@ICIPERS {off}[{green}Galuh pawestri{off}]")
#time.sleep(0.1)
#mengetik(f"{yellow}@freedom_reborn {off}[{green}FREEDOM REBORN{off}]")
#time.sleep(0.1)
#mengetik(f"{white}@JSTFREENET {off}[{green}Jst-team{off}]")
#time.sleep(0.1)
#mengetik(f"{red}@configarea {off}[{green}vpnkacang{off}]")
#time.sleep(0.1)
#mengetik(f"")
#time.sleep(1)
#mengetik(f"{cyan}SELAMAT MENGGUNAKAN{off}")
#time.sleep(2)
#os.system('clear')
#menu_utama
print(logo)
print(bawah)
print()
print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print(f"{green}[{yellow}1{green}]{white}BILLING ITS 1JAM   {green}[{yellow}2{green}]{white}TOKEN ITS 48JAM\n{green}[{yellow}3{green}]{white}BILLING UNSRAT")
print(f"————————————————————————————————————————")
print(f"{cyan}[{yellow}4{cyan}]{white}CREATE SSH GRATIS")
print(f"{green}[{yellow}5{green}]{white}JOIN GROUP {green}TELE{off}")
print(f"{green}[{yellow}6{green}]{white}JOIN CHANNEL {green}TELE{off}")
print(f"{green}[{red}7{green}]{white}SUBCRIBE YOUTUBE")
print(f"{red}[{yellow}0{red}]{red}Keluar{off}")
print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
inv = input(f"{purple}>>>{off} Pilih > ")
if inv == '1':
	print()
	print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
	print(f"\r{yellow}[{red}info{yellow}]{white}1x run = 2x generate")
	print(f"\r{yellow}[{red}info{yellow}]{white}Reset setiap 1 jam sekali")
	print(f"————————————————————————————————————————")
	print()
	url = 'https://raw.githubusercontent.com/sanzking212/token/main/1(2).txt'
	r = requests.get(url)
	text = r.text
	individual_words = text.split()
	random_number = randint(0, len(individual_words))
	print(end=f"\r{white}Mengambil token 1Jam...")
	time.sleep(2)
	print(f"\r{green}[{blue}1jam{green}]{yellow}" + individual_words[random_number])
	print(f"{off}")
	print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
	print()
	exit(f"{green}[{yellow}✓{green}]{white}Terimakasih telah menggunakan layanan ini\n{green}[{yellow}✓{green}]{white}Nantikan update pada jam berikutnya\n{green}[{blue}!{green}]{white}Pantau terus channel kami\n{green}>> VPNKACANG\n{cyan}>> JSTFREENET\n{yellow}>> FREEDOM'X{off}")
elif inv == '5':
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
elif inv == '6':
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
elif inv == '7':
	print(f"{red}>>> {white} SUBSCRIBE CHANNEL JST {red}<<<{off}")
	os.system(f"xdg-open https://youtu.be/7f6PJB6V-Mo")
elif inv == '0':
	exit(f"{red}Terimakasih telah menggunakan tools kami")
elif inv == '4':
	print(f"{green}\rFREE SSH: AZURE, AWS")
	print(f"{yellow}\rSERVER : SG , US")
	print(f"{purple}\rRESET TIME 22:00")
	print(end=f"\r{white}Sedang dialihkan ke browser...")
	time.sleep(2)
	os.system(f"xdg-open http://jstssh.computer/")
elif inv == '3':
	print()
	print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
	print(f"\r{yellow}[{red}info{yellow}]{white}Token billing UNSRAT")
	print(f"\r{yellow}[{red}info{yellow}]{white}Reset setiap 2 hari sekali")
	print(f"————————————————————————————————————————")
	print()
	url = 'https://raw.githubusercontent.com/tokenits/billing-unsrat/main/Billing.txt'
	r = requests.get(url)
	text = r.text
	individual_words = text.split()
	random_number = randint(0, len(individual_words))
	print(end=f"\r{white}Mengambil token...")
	time.sleep(2)
	print(f"\r{green}[{blue}TOKEN UNSRAT{green}] {off}=>{yellow} " + individual_words[random_number])
	print()
	print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
	exit(f"{green}[{yellow}✓{green}]{white}Terimakasih telah menggunakan layanan ini\n{green}[{yellow}✓{green}]{white}Nantikan update pada 48 jam berikutnya\n{green}[{blue}!{green}]{white}Pantau terus channel kami\n{green}>> VPNKACANG\n{cyan}>> JSTFREENET\n{yellow}>> FREEDOM'X{off}")
elif inv == '2':
	print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
	print(f"\r{yellow}[{red}info{yellow}]{white}Token ITS 48Jam")
	print(f"\r{yellow}[{red}info{yellow}]{white}Reset setiap 2 hari sekali")
	print(f"————————————————————————————————————————")
	print()
	url = 'https://raw.githubusercontent.com/tokenits/billing-unsrat/main/48jam'
	r = requests.get(url)
	text = r.text
	individual_words = text.split()
	random_number = randint(0, len(individual_words))
	print(end=f"\r{white}Mengambil token...")
	time.sleep(2)
	print(f"\r{green}[{blue}48jam{green}] {off}=>{yellow} " + individual_words[random_number])
	print()
	print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
	exit(f"{green}[{yellow}✓{green}]{white}Terimakasih telah menggunakan layanan ini\n{green}[{yellow}✓{green}]{white}Nantikan update pada 48 jam berikutnya\n{green}[{blue}!{green}]{white}Pantau terus channel kami\n{green}>> VPNKACANG\n{cyan}>> JSTFREENET\n{yellow}>> FREEDOM'X{off}")
#Jangan_lupa_join_grup_sama_channel_telenya_cuk
#SANZKING
