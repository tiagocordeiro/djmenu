# djmenu
Django food menu

### Como rodar o projeto?

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
