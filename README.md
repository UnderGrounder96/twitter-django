# Twitter_Django

Project created under Linux Ubuntu 64-bit using Python 3.8, pip 20.1.1 and Django 3.0.7

![Twitter Django image](TwitterDjango.png)

## Deployment

Install [python3.6](https://www.python.org/downloads/) and execute the commands:

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Before starting. Please rename the file '.env.default' to '.env', and set in it your Secret credentials.<br />
Running the server:<br />

```
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py test
$ python manage.py runserver
```

Open [localhost:8000](http://localhost:8000) in a browser.

## Versioning

Version 1.5 - Current version<br />
Version 5.0 (TBA) - Moderation algorithms

## Author

Lucio Afonso

## License

This project is licensed under the GPL License - see the LICENSE.md file for details

## Acknowledgments

Tutorials:

[Acumenus](https://stackoverflow.com/a/45474387/)<br />
[Corey Schafer](https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)<br />
[The Dumbfounds](https://youtube.com/playlist?list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM)
