#!/usr/bin/env python3

import os

def uninstall():
	print(GREEN + "Desinstalando truffle"+ NORMAL)
	os.system("sudo npm uninstall -g truffle")

	print(GREEN + "Desinstalando ganache-cli"+ NORMAL)
	os.system("sudo npm uninstall -g ganache-cli")
	
	print(GREEN + "Desinstalando remix-ide"+ NORMAL)
	os.system("sudo npm uninstall -g remix-ide")
	
	print(GREEN + "Desinstalando solc"+ NORMAL)
	os.system("sudo npm uninstall -g solc")


if __name__ == "__main__":
	# Some colours
	GREEN = "\033[10;30;92m"
	NORMAL = "\033[1;37;0m"
	RED = "\033[1;37;91m"

	yes = {'yes', 'y', 'ye', 'si', 's', ''}

	print(RED + "Se borrarán los siguientes paquetes:" + NORMAL)
	print("- solc\n- remix-ide\n- ganache-cli\n- truffle")
	opcion = input("¿Seguro que quieres borrar los paquetes? [S/n]: ").lower()

	if opcion in yes:	
		uninstall()
		print(GREEN + "Paquetes eliminados")

	print(GREEN + "Fin")

