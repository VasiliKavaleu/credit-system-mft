## Credit System App

##### Main entities:

- Contract | Контракт
- CreditApplication | Кредитная заявка
- Item | Товар
- Manufacturer | Производитель

##### Test
Currently, the Test task is deployd to the server.

So, you can see available contracts at [this link](http://159.89.105.161/api/v1/contracts/)

And get manufacturer's unique identifiers by adding contract id to url params [like this](http://159.89.105.161/api/v1/contracts/1)

Also, you can add you own rows to the Entities using the admin panel, which is temporarily available [here](http://159.89.105.161/admin/) with credentials:

```commandline
user: john
password: password123
```

### Steps to reproduce
Clone repo.

Create virtualenv:
```commandline
pip3 -m venv env
```

Install requirements:
```commandline
pip3 install -r requirements.txt
```

Install the git hook scripts:
```commandline
pre-commit install --hook-type pre-commit --hook-type pre-push
```

Create .env file (or rename and modify src/example.env) in project root and set environment variables for application:

```commandline
touch .env
echo DEBUG=True >> .env
echo DATABASE_URL=postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB >> .env
echo SECRET_KEY=$(openssl rand -hex 32) >> .env
echo ALLOWED_HOSTS=127.0.0.1,192.168.1.1 >> .env
```

Run application

```commandline
python3 src/manage.py runserver
```
