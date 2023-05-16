# Project branch for MGS 406 final 

Use the requirements.txt file to install all necessary packages for this project  

`pip install -r requirements.txt`

If you have a Python virtual environment, activate it with the following command:

`source venv/bin/activate`

If you don't have a Python virtual environment, or you just created a new work directory, use the following commands to create a new virtual environment:

You may need to use python3 to replace python depending on your system settings 

`python -m venv venv`

the below files handle the MySQL database, table, connectivity, and creating a local user

`create_user.py` `create_db.py` `create_table.py` `connect_db.py` 

Run the Flask app:

`python manage.py`

The Flask app will be running on http://127.0.0.1:5000.
