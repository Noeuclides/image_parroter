# Image Thumbnail Generator

Image thumbnail generator with django, celery, and redis.

## Requirements
It is necesary to install [redis](https://redis.io/download) (Mac OSX / Linux).

To run the django app use the python package manager [pipenv](https://pipenv-es.readthedocs.io/es/latest/).

## Installation

Run the redis server (follow the instructions of the link on requirements section).
```bash
redis-server
```

Then, in another terminal, once this repo is cloned, in the root directory, first install the dependencies:

```bash
pipenv install
```

And then run the django server:

```bash
pipenv run migrate
pipenv run server
```
Note: The migrate and server commands are set in the Pipfile.

In a different terminal run the celery program:
```bash
pipenv run celery -A image_parroter worker --loglevel=info
```

## Usage
Now in the browser in http://127.0.0.1:8000/ you should be able to generate the image thumbnails.
