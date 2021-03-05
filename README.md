# Image Thumbnail Generator

Image thumbnail generator with django, celery, and redis.

## Requirements
It is necesary to install [redis](https://redis.io/download) (Mac OSX / Linux).

To run the django app use the python package manager [pipenv](https://pipenv-es.readthedocs.io/es/latest/).

## Installation

Once this repo is cloned, run in the root directory:

```bash
pipenv run server
```

In a different terminal run the celery program:
```bash
pipenv run celery -A image_parroter worker --loglevel=info
```

And in another terminal run the redis server (follow the instructions of the link on requirements section).
```bash
redis-server
```

## Usage
Now in the browser in http://127.0.0.1:8000/ you should be able to generate the thumbnail.
