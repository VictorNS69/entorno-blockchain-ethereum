#!/usr/bin/env python3

import os
from pathlib import Path


def git_config():
	'''Script de configuración del entorno de git'''

	nombre_completo = input("Escribe tu nombre completo: ")
	email = input("Escribe tu email: ")
	username = input("Escribe tu username: ")

	comando_nombre = "git config --global user.name \"" + nombre_completo + "\""
	comando_email = "git config --global user.email " + email
	comando_username = "git config --global credential.username " + username

	os.system(comando_nombre)
	os.system(comando_email)
	os.system(comando_username)
	
	print("Fichero ~/.gitconfig modificado")


def modificar_prompt():
	'''Añade el nombre de la rama actual de Git al prompt'''

	string = "git_branch() { \n\
	git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\\1)/'\n}\
	\n\nexport PS1=\"${PS1:0:${#PS1}-3}\$(git_branch)\$ \""
	
	with open(str(Path.home()) + "/.bashrc", "a+") as bashrc: 
		bashrc.write(string)
	
	print("Fichero ~/.bashrc modificado")

if __name__ == "__main__":
	yes = {'yes', 'y', 'ye', 'si', 's', ''}

	opcion = input("¿Quieres modificar tus datos de git globales? [S/n]: ").lower()
	if opcion in yes:	
		git_config()

	opcion = input("¿Quieres añadir el nombre de la rama actual al prompt? [S/n]: ").lower()
	if opcion in yes:
		modificar_prompt()
