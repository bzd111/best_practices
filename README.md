# best_practices

general python project config

# init

```
pipenv install black --dev --pre
pipenv install isort --dev
pipenv install flake8 --dev
pipenv install mypy --dev
pipenv install pytest --dev
pipenv install pre-commit --dev
```

# or

`pipenv run init`

## pre-commit install hooks

```
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push``

```

# refer

- https://sourcery.ai/blog/python-best-practices/
- https://github.com/asvetlov/us-pycon-2019-tutorial
