# How to run tests

> with TOX

```shell
tox

```

> or with pytest

```shell
pytest -vv --cov app
pytest -vv --cov apis
pytest -vv --cov core
```

#### or

```shell
pytest -v
```

> Using pipenv

```shell
python3 -m pip install pipenv
cd project-dir
pipenv shell
pipenv lock --pre
pipenv sync
```
