

# Development Instruction

## Install dependencies

```
python3.8 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.lock
```

## Activate virtual environment

```
. venv/bin/activate
```

## Install a new package

```
. venv/bin/activate
pip install package_name
pip freeze | tee requirements.lock
```