# Weather Forecast
 
 ### Python 3.6
    
 - ###### Instalação no Ubuntu
       sudo apt update
       sudo apt install software-properties-common
       sudo add-apt-repository ppa:deadsnakes/ppa
       sudo apt install python3.6
       python3.6 --version

 ### Virtualenv

 - ###### Instalação no Ubuntu:
       sudo apt install python3-venv	
       sudo apt install python-virtualenv
 - ###### Criando ambiente:
       sudo virtualenv --python=python3.6 venv
 - ###### Ativando ambiente:
       source venv/bin/activate


 ### Projeto Imports

 - ###### Instalando dependências
       sudo chmod 777 -R weather_backend
       pip install -r requirements.txt
 - ###### Iniciando serviço:
       python manage.py migrate
       python manage.py createsuperuser
       python manage.py runserver
