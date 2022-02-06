# EMenu-API
API for managing menus and recipes

Python 3.10.2 was used to develop this app.

# Instruction
1. After cloning the project, go into the project directory and create and activate a virtual environment

```python3 -m venv venv```

```source venv/bin/activate``` Linux 

OR

```.\venv\Scripts\Activate.ps1``` Windows (Powershell)

2. Install requirements

```python -m pip install -r requirements.txt```

3. Go into emenuapi directory and run migrations

```python manage.py migrate```

4. Load intial data

```python manage.py loaddata menusapp/initial_data.json```

5. Run app

```python manage.py runserver```

