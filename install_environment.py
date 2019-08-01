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
	MAGENTA = "\033[1;35;95m"
	NORMAL = "\033[1;37;0m"

	print(MAGENTA + "Obteniendo versiones específicas de los paquetes" + NORMAL)
	versions = parse_versions()
	"""
	print(MAGENTA + "Añadiendo PPA de ethereum (ppa:ethereum/ethereum)" + NORMAL)
	os.system("sudo add-apt-repository -y ppa:ethereum/ethereum")

	print(MAGENTA + "Actualizando el sistema" + NORMAL)
	val = os.system("sudo apt -y update")
	print(val)
	#val = os.system("sudo apt -y upgrade --fix-missing")
	print(val) # TODO Comprobar si el código de salida es 0 ??

	print(MAGENTA + "Instalando curl"+ NORMAL)
	os.system("sudo apt install -y curl")

	print(MAGENTA + "Instalando npm"+ NORMAL)
	os.system("sudo apt install -y npm")

	print(MAGENTA + "Instalando nodejs"+ NORMAL)
	os.system("sudo apt install -y nodejs")

	print(MAGENTA + "Instalando ethereum"+ NORMAL)
	os.system("sudo apt install -y ethereum")

	print(MAGENTA + "Instalando git"+ NORMAL)
	os.system("sudo apt install -y git")
	"""
	print(MAGENTA + "Instalando ganache-cli"+ NORMAL)
	print("ganache", versions["ganache-cli"])
	os.system("npm install -g ganache-cli" + versions["ganache-cli"])

