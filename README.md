# Software de postulación U-Zave
## Tecnologías utilizadas

1. python 3.6.9
2. Sqlite

## Instrucciones para instalación

1. Puedes crear un ambiente virtual o instalarlo globalmente.
2. Para instalar las dependencias ejecutar desde el directorio del proyecto
`$ pip3 install -r requirements.txt`
3. Para ejecutar los test correr el desde el directorio raiz del proyecto debes correr el comando: `$ pytest src/`
4. El programa funciona sobre un servidor local, para ejecutarlo debes correr en el directorio del proyecto el comando : `$ uvicorn src.main:app --reload`

