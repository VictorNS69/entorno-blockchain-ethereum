#!/usr/bin/env python3

import os
import json



def parse_versions():
	with open("versions.json") as json_file:
		versions = json.load(json_file)
	for i in versions:
		if not versions[i]:
			pass
		else:
			versions[i] = "@" + versions[i]
	return versions


	
if __name__ == "__main__":
	# Some colours
	GREEN = "\033[10;30;92m"
	NORMAL = "\033[1;37;0m"

	print(GREEN + "Obteniendo versiones específicas de los paquetes" + NORMAL)
	versions = parse_versions()

	print(GREEN + "Añadiendo PPA de ethereum (ppa:ethereum/ethereum)" + NORMAL)
	os.system("sudo add-apt-repository -y ppa:ethereum/ethereum")

	print(GREEN + "Actualizando el sistema" + NORMAL)
	os.system("sudo apt -y update && sudo apt -y upgrade")

	print(GREEN + "Instalando curl"+ NORMAL)
	os.system("sudo apt install -y curl")

	print(GREEN + "Instalando npm"+ NORMAL)
	os.system("sudo apt install -y npm")

	print(GREEN + "Instalando nodejs"+ NORMAL)
	os.system("sudo apt install -y nodejs")

	print(GREEN + "Instalando ethereum"+ NORMAL)
	os.system("sudo apt install -y ethereum")

	print(GREEN + "Instalando git"+ NORMAL)
	os.system("sudo apt install -y git")
	
	print(GREEN + "Instalando truffle"+ NORMAL)
	os.system("sudo chmod 777 ~/.config") # Permission problem at installing in ~/.config
	os.system("sudo npm install -g truffle" + versions["truffle"])
	os.system("sudo chmod 755 ~/.config") # Revert permissions
	os.system("sudo chmod -R --silent 777 ~/.config/truffle") # Grant permissions for truffle

	print(GREEN + "Instalando ganache-cli"+ NORMAL)
	os.system("sudo npm install -g ganache-cli" + versions["ganache-cli"])
	
	print(GREEN + "Instalando remix-ide"+ NORMAL)
	os.system("sudo npm install -g remix-ide" + versions["remix-ide"])
	
	print(GREEN + "Instalando solc"+ NORMAL)
	os.system("sudo npm install -g solc" + versions["solc"])

	print(GREEN + "Instalación terminada")
