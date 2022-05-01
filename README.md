# URL Shortener

This app has functionality like existing shorteners like bitly

## Funcionalities

- One accepts a URL via a POST request and returns a shortcode
- The other one accepts a shortcode via a GET request and returns the original URL

## Setting environment variables

Before running service setting environment variables, copy env.example and rename to .env

```
cp .env.example .env
```

## Running

### Server

```
docker-compose build
docker-compose up
```

### Tests
Before performing the tests, it is necessary to enter the container to execute them.

```
docker-compose exec app /bin/bash
```

```shell
pytest tests/unit 
pytest tests/functional
```
