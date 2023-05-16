# Project branch for MGS 406 final 

Use the requirements.txt file to install all necessary packages for this project  

`pip install -r requirements.txt`

## If you don't have a Python virtual environment, or you just created a new work directory, you will need to create it

If you have a Python virtual environment, activate it with the following command:

`source venv/bin/activate`

the below files handle the MySQL database, table, connectivity, and creating a local user

`create_user.py` `create_db.py` `create_table.py` `connect_db.py` 

Run the Flask app:

`python manage.py`

The Flask app will be running locally

in order to deploy the app with gunicorn use the command

`gunicorn	-w 4 --bind 0.0.0.0:5000	wsgi:app`

The Flask app will be running on http://127.0.0.1:5000.
