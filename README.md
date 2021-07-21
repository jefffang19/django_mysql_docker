# Django Mysql with DOCKER

## How to run

1. run
```
docker-compose -f mysql.yaml up
```
2. remove container
```
docker-compose -f mysql.yaml down
```

## Note

1. django container needs to wait for mysql to ready
```
# mysql.yaml

web:
        build: .
        command: ['/app/wait_for_it.sh', 'db:3306', '--', '/app/run.sh']
```
wait_for_it.sh checks for mysql to ready

2. db user can be save in `my.cnf`
```
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'my.cnf'),
        },
    }
}
```
note that `HOST` is same in `mysql.yaml`
```
services:
    db:
        image: mysql:8.0
        restart: always
        ports:
            - 3306:3306
```

3. 
```
django.db.utils.OperationalError: (2061, 'RSA Encryption not supported - caching_sha2_password plugin was built with GnuTLS support')
```

solutiion:
```
# mysql.yaml

db:
	command: --default-authentication-plugin=mysql_native_password --mysqlx=0
```

4. in .yaml file, each services can only have 1 command
if you want to run many command, you can run a shell script
```
# mysql.yaml

command: ['/app/wait_for_it.sh', 'db:3306', '--', '/app/run.sh']
```

## reference
django use mysql<br>
https://docs.djangoproject.com/en/3.2/ref/databases/#mysql-notes

Control startup and shutdown order in Compose<br>
https://docs.docker.com/compose/startup-order/

Quickstart: Compose and Django<br>
https://docs.docker.com/samples/django/