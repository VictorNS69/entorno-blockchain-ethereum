# Script de instalación de paquetes básicos para trabajar en una blockchain

## Requisitos
- Python 3.6 o superior
- Conexión a internet
## Ficheros 
- **versions.json**: Archivo que especifica las versiones a instalar de algunos paquete.
**No se debe modificar** si se desean instalar las últimas versiones disponibles de los paquetes.
- **install_environment.py**: Script que instalará todos los paquetes necesarios para trabajar en una blockchain, además de algunas herramientas básicas para el sistema.
- **uninstall_npm_packages.py**: Script que eliminará del sistema los paquetes necesarios para trabajar en una blockchain.
- **git_config.py**: Script que configurará los datos de usuario de git, además de que (si se desea) añadirá al prompt la rama actual en la que se trabaje.
## Especificar versiones
Para que se instale una versión específica, es tan sencillo como añadir la versión en el documento `versions.json`.

Por ejemplo, para añadir la versión de _truffle_ _4.1.15_ y la versión _0.4.25_ de _solc_, se tendrá que modificar el archivo de la siguiente manera:
```json
{
	"ganache-cli": "",
	"truffle": "4.1.15",
	"remix-ide": "",
	"solc": "0.4.25"
}
```
## Ejecución
Los archivos son scripts escritos en python. La manera de ejecutarlos son:
- Si los archivos tienen permisos de ejecución:
```sh
./install_environment.py
./git_config.py
./uninstall_npm_packages.py
```
- o bien:
```sh
python3 install_environment.py
python3 git_config.py
python3 uninstall_npm_packages.py
```

## Notas
**Es posible** que falten algunos paquetes. Esta instalación solo añade lo **más básico** para trabajar en la blockchain.
## Autor
[Victor Nieves Sánchez](https://github.com/VictorNS69)
