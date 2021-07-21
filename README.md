# Django Mysql with DOCKER

1. run
```
docker-compose -f mysql.yaml up
```
2. remove container
```
docker-compose -f mysql.yaml down
```

## reference
django use mysql<br>
https://docs.djangoproject.com/en/3.2/ref/databases/#mysql-notes

Control startup and shutdown order in Compose<br>
https://docs.docker.com/compose/startup-order/

Quickstart: Compose and Django<br>
https://docs.docker.com/samples/django/