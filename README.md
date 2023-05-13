# interstellr
2022-23 TSA Webmaster, Team 2009-901

## About
This application uses the Flask framework in the Python language.

## Install

1. Install Python from https://www.python.org/downloads/

2. Install the dependencies
    ```bash
    pip install -r requirements.txt
    ```

## Run app in production
```bash
gunicorn main:app
```

## Run app in development
```bash
python debug.py
```
