# djmenu - Django food menu
A simple solution for restaurants and pizzerias.

## Live demo
https://djmenu.herokuapp.com/

[![Updates](https://pyup.io/repos/github/tiagocordeiro/djmenu/shield.svg)](https://pyup.io/repos/github/tiagocordeiro/djmenu/)
[![Python 3](https://pyup.io/repos/github/tiagocordeiro/djmenu/python-3-shield.svg)](https://pyup.io/repos/github/tiagocordeiro/djmenu/)
[![codecov](https://codecov.io/gh/tiagocordeiro/djmenu/branch/master/graph/badge.svg)](https://codecov.io/gh/tiagocordeiro/djmenu)
[![Python 3.7.6](https://img.shields.io/badge/python-3.7.6-blue.svg)](https://www.python.org/downloads/release/python-376/)
[![Django 2.2.8](https://img.shields.io/badge/django-2.2.8-blue.svg)](https://www.djangoproject.com/download/)
[![Build Status](https://travis-ci.org/tiagocordeiro/djmenu.svg?branch=master)](https://travis-ci.org/tiagocordeiro/djmenu)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/tiagocordeiro/djmenu/blob/master/LICENSE)

### Como rodar o projeto

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/tiagocordeiro/djmenu.git
cd djmenu
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```


### Popular o banco de dados com produtos de exemplo
Para criar produtos, categorias e variações de exemplo, execute o comando abaixo
```
python manage.py loaddata products/fixtures/products.json
```


### Configurar administrador
Para cria um usuário administrador
```
python manage.py createsuperuser --username dev --email dev@foo.bar
```


### Rodar em ambiente de desenvolvimento
Para rodar o projeto localmente
```
python manage.py runserver
```


### Testes, contribuição e dependências de desenvolvimento
Para instalar as dependências de desenvolvimento
```
pip install -r requirements-dev.txt
```

Para rodar os testes
```
python manage.py test -v 2
```

Para rodar os testes com relatório de cobertura.
```
coverage run manage.py test -v 2
coverage html
```

Verificando o `Code style`
```
pycodestyle .
flake8 .
```
