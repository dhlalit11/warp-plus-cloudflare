#Huge thanks to ALIILAPRO for making the script
#Modified for Logging and Single line exection by dhlalit11 
import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
import duallog 
import logging
os.system("title WARP-PLUS-CLOUDFLARE By ALIILAPRO")
#Setup save location for log files
duallog.setup('/path/to/log/folder')
os.system('cls' if os.name == 'nt' else 'clear')
print('      _______ _      __________________       _______ _______ _______ _______\n'
'     (  ___  | \     \__   __|__   __( \     (  ___  |  ____ |  ____ |  ___  )\n'
'     | (   ) | (        ) (     ) (  | (     | (   ) | (    )| (    )| (   ) |\n'
'     | (___) | |        | |     | |  | |     | (___) | (____)| (____)| |   | |\n'
'     |  ___  | |        | |     | |  | |     |  ___  |  _____)     __) |   | |\n'
'     | (   ) | |        | |     | |  | |     | (   ) | (     | (\ (  | |   | |\n'
'     | )   ( | (____/\__) (_____) (__| (____/\ )   ( | )     | ) \ \_| (___) |\n'
'     |/     \(_______|_______|_______(_______//     \|/      |/   \__(_______)\n')
print ("[+] ABOUT SCRIPT:")
print ("[-] With this script, you can getting unlimited GB on Warp+.")
print ("[-] Version: 4.0.0")
print ("--------")
print ("[+] THIS SCRIPT CODDED BY ALIILAPRO") 
print ("[-] SITE: aliilapro.github.io") 
print ("[-] TELEGRAM: aliilapro")
print ("--------")
time.sleep(1.5)
#Change referrer id below to your id or you won't get free data ( dont delete quote marks)
referrer = 'f0b3ba5f-9dfd-44c6-803b-8839a00ad7c8'
#
def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		logging.error(f"error\n\n")		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		logging.error(f"error\n\n")
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
#
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print(error)	

g = 0
b = 0
e = 0
while True:
	result = run()
	if result == 200:
		g = g + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		logging.critical("WARP-PLUS-CLOUDFLARE (script)" + " By ALIILAPRO")
		print("[+] Preparing")
		time.sleep(0.4)
		logging.critical(f"[-] WORK ON ID: {referrer}")    
		logging.critical(f"[:)] {g} GB has been successfully added to your account.")
		logging.critical(f"[#] Total: {g} Good {b} Bad")
		logging.critical("[*] After 30 seconds, a new request will be sent.\n\n")
		e = 0
		time.sleep(30)
	elif e > 9:
		b = b + 1
		e = e + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		logging.error(f"Got back to back {e} errors, waiting 15 seconds before sending another request")
		logging.error(f"Total number of bad requests are {b}\n\n")
		time.sleep(15)
	else:
		b = b + 1
		e = e + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		logging.error(" WARP-PLUS-CLOUDFLARE (script)" + " By ALIILAPRO")
		logging.error("[:(] Error when connecting to server.")
		logging.error(f"[#] Total: {g} Good {b} Bad\n\n")	
		sys.stdout.flush()
