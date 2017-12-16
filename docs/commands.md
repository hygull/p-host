# Commands

### 1
```
django-amdin startproject pmt_hostel_site 

django-admin.py startproject pmt_hostel_site 
```

### 2

```
C(venv) MacBook-Pro-2:src admin$ pwd
/Users/admin/projects/Python/Django/git/PmtHostel/src
(venv) MacBook-Pro-2:src admin$ 
(venv) MacBook-Pro-2:src admin$ ls
db.sqlite3	manage.py	pmt_hostel_site
(venv) MacBook-Pro-2:src admin$
```

```
python manage.py runserver

python manage.py runserver 9000

python manage.py runserver localhost:9000

python manage.py runserver 127.0.0.1:9000
```	

```
python manage.py runserver 0:8000
python manage.py runserver 0.0.0.0:8000
```

```
(venv) MacBook-Pro-2:src admin$ python manage.py runserver :9000
CommandError: ":9000" is not a valid port number or address:port pair.
```

```
(venv) MacBook-Pro-2:src admin$ python manage.py runserver 1.2.2.2:9000
Performing system checks...

System check identified no issues (0 silenced).
December 16, 2017 - 14:40:27
Django version 2.0, using settings 'pmt_hostel_site.settings'
Starting development server at http://1.2.2.2:9000/
Quit the server with CONTROL-C.
Error: That IP address can't be assigned to.
```

### 3

```
python3 manage.py migrate
```

### 4

```
python3 manage.py startapp pmt_hostel_app
```

```
(venv) MacBook-Pro-2:src admin$ ls
db.sqlite3	manage.py	pmt_hostel_site
(venv) MacBook-Pro-2:src admin$ 
(venv) MacBook-Pro-2:src admin$ python3 manage.py startapp pmt_hostel_app
(venv) MacBook-Pro-2:src admin$ 
(venv) MacBook-Pro-2:src admin$ pwd
/Users/admin/projects/Python/Django/git/PmtHostel/src
(venv) MacBook-Pro-2:src admin$ 
(venv) MacBook-Pro-2:src admin$ ls
db.sqlite3	manage.py	pmt_hostel_app	pmt_hostel_site
(venv) MacBook-Pro-2:src admin$ 
```

### 5

```
python manage.py makemigrations pmt_hostel_app
```

### 6

```
python3 manage.py sqlmigrate pmt_hostel_app 0001
```

### 7

```
python3 manage.py check
```

### 8

```
python manage.py createsuperuser
```