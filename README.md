# FoodOrderingApp

Backend implementation of a food ordering system with Django REST framework.

## Cloning and Installing Dependencies

Open terminal and write the following command:
```
$ git clone https://github.com/nebHailemariam/FoodOrderingApp.git
$ cd FoodOrderingApp/
$ pip3 install -r requirements.txt 
```

## Making migrations and applying migrations to the database

Open terminal and write the following command:
```
$ python manage.py makemigrations
$ python manage.py migrate auth
$ cd users/
$ python groups.py
$ python manage.py migrate
```

## Creating a SuperUser
A superuser user account has control over everything on the site.

```
$ Python manage.py createsuperuser
Username:John
Password:********
```

## Deploying server

To deploy the application type the command:
```
$ python manage.py runserver
```

## API List

## Contributing
Pull requests are welcome.

## License
[MIT](https://choosealicense.com/licenses/mit/)
