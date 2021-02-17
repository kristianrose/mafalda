import platform
import os
import sys
import time
import random
import getpass

goodstr = "module.exports = require('./core.asar');"
cookie = open(".mafalda_cookie","w+")
badstrs = ["4n4rchy", "inject", "hook", "modDir"]

banner = """\033[1m\033[94m

                               _.._
                             .'    '.
                            (____/`\ \
                           (  |' ' )  )
                           )  _\= _/  (
                 __..---.(`_.'  ` \    )
                `;-""-._(_( .      `; (
                /       `-`'--'     ; )
               /    /  .    ( .  ,| |(
_.-`'---...__,'    /-,..___.-'--'_| |_)
'-'``'-.._       ,'  |   / .........'
         ``;--"`;   |   `-`
             `'..__.'\033[00m\033[1m

             \033[1m\033[95mDesenvolvido por: Kristian\033[00m\033[1m
                   \033[1m\033[95mCarregando...\033[00m\033[1m
"""


try:
	users = ["Kris", "free"]
	clear = "clear"
	sys.stdout.write("\x1b]2;M a f a l d a\x07")
	os.system (clear)
	username = getpass.getpass ("[❀] Usuário: ")
	if username in users:
		user = username
	else:
		print ("\033[1m\033[91m[❀] Incorreto, usuário inexistente\033[1m\033[91m")
		exit()
except KeyboardInterrupt:
	print ("\nCTRL-C foi apertado")
	exit()
try:
	passwords = ["lindo123", "free"]
	password = getpass.getpass ("[❀] Senha: ")
	if user == "Kris":
		if password == passwords[0]:
			print ("\033[1m\033[92m[❀] Logado com sucesso\033[1m\033[92m")
			cookie.write("DIE")
			time.sleep(1)
			os.system (clear)
			try:
				os.system ("clear")
				sys.stdout.write("\x1b]2;M a f a l d a\x07")
				print (banner)
				time.sleep(5)
				os.system (clear)
			except KeyboardInterrupt:
				print ("\n[\033[91mMafalda\033[00m] CTRL foi apertado")

		else:
			print ("\033[1m\033[91m[❀] Incorreto, usuário inexistente\033[1m\033[91m")
			exit()
	if user == "free":
		if password == passwords[1]:
			print ("\033[1m\033[92m[❀] Logado com sucesso\033[1m\033[92m")
			print ("\033[1m\033[91m[❀] As atualizações no cliente não estarão disponíveis para você\n[❀] Contacte: Kris#6969 para adquirir a versão paga\033[1m\033[91m")
			time.sleep(5)
			os.system (clear)
			try:
				os.system ("clear")
				print (banner)
				time.sleep(5)
				os.system (clear)
			except KeyboardInterrupt:
				print ("\n[\033[91mMafalda\033[00m] CTRL foi apertado")

		else:
			print ("\033[1m\033[91m[❀] Incorreto, usuário inexistente\033[1m\033[91m")
			exit()
except KeyboardInterrupt:
	exit()



def get_all_versions(dirs):
	versions = []
	for dir in dirs:
		if dir.startswith("0"):
			versions.append(dir)
	return versions


def check_version(path, name):
	with open(path+"/modules/discord_desktop_core/index.js") as f:
		content = f.read()
		badcount = 0
		for badstr in badstrs:
			if badstr in content:
				badcount+=1
		if badcount>0:
			print("\033[1m\033[91m[Mafalda]  Erro: Discord "+name+" esta infectado com AnarchyGrabber, "+str(badcount)+" assinaturas foram encontradas!\033[91m\033[0m")
		elif content == goodstr:
			print("\033[1m\033[92m[Mafalda]  Sucesso: Discord "+name+" esta sem vestígios do AnarchyGrabber!\033[92m\033[0m")
		else:
			print("\033[93m[Mafalda]  Aviso: Discord "+name+" index.js conteúdo desconhecido. Se você não tiver um cliente modificado, isso pode ser um infecção do AnarchyGrabber!")


def check_discord(path, name):
	dirs = os.listdir(path)
	versions = get_all_versions(dirs)
	for version in versions:
		print("\033[1m\033[95mVersão é "+version+"\033[95m\033[1m")
		check_version(path+"/"+version, name)



osname = platform.system()

discordbase = ""

if osname == "Darwin":
	homedir = os.path.expanduser("~")
	discordbase = homedir+"/Library/Application Support"
	print("Você esta usando Mac OS X")

elif osname == "Windows":
	homedir = os.path.expanduser("~")
	discordbase = homedir+"/AppData/Roaming"
	print("Você esta usando Windows")

else:
	print("Esta ferramenta não suporta atualmente "+osname+"!")
	sys.exit(1)

print("\n\033[93m[Mafalda]  Procurando por Discord Stable...\033[00m")
if os.path.exists(discordbase+"/discord"):
	print("\033[1m\033[92mDiscord encontrado em "+discordbase+"/discord\033[1m\033[92m")
	check_discord(discordbase+"/discord", "Stable")
else:
	print("\n\033[93mDiscord Stable não encontrado.\033[1m\033[91m")

print("\n\033[93m[Mafalda]  Procurando por Discord PTB...\033[00m")
if os.path.exists(discordbase+"/discordptb"):
	print("\033[1m\033[92mDiscord encontrado em "+discordbase+"/discordptb\033[1m\033[92m")
	check_discord(discordbase+"/discordptb", "PTB")
else:
	print("\033[1m\033[91mDiscord PTB não encontrado.\033[1m\033[91m")

print("\n\033[93m[Mafalda]  Procurando por Canary...\033[00m")
if os.path.exists(discordbase+"/discordcanary"):
	print("\033[1m\033[92mDiscord encontrado em "+discordbase+"/discordcanary\033[1m\033[92m")
	check_discord(discordbase+"/discordcanary", "Canary")
else:
	print("\033[1m\033[91mDiscord Canary não encontrado.\033[1m\033[91m")
