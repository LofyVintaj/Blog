# Website template for Developmentg

## Run locally

```bash
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

## Build

```bash
docker-compose -f docker-compose.yml -f docker-compose.dev.yml build

## Exec command in container

```bash
docker-compose -f docker-compose.yml -f docker-compose.dev.yml exec server ./manage.py shell
```
