# Desolate County - Data Parser
Converts a CSV to a JSON for the Desolate County Project.

## Running

`pipenv run python src/main.py data/Name.csv`

## Contributing

- Install pyenv

```bash
brew install pyenv
```

- Add pyenv ENV to profile

```bash
echo "export PYENV_ROOT="$HOME/.pyenv"" >> ~/.zshrc
echo "export PATH="$PYENV_ROOT/bin:$PATH"" >> ~/.zshrc
```

- Install pipenv

```bash
brew install pipenv
```

- Add this environment variable so pipenv uses pyenv selected version when no version is specified

```bash
echo "export PIPENV_PYTHON="$PYENV_ROOT/shims/python"" >> ~/.zshrc
```

-  Install environment
```bash
pipenv install --dev
```

