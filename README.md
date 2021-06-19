# Twitter_Django

Project created under Linux Ubuntu 64-bit using Python 3.8, pip 20.1.1 and Django 3.0.7

![Twitter Django image](TwitterDjango.png)

## Deployment (baremetal)

Install [python3.6](https://www.python.org/downloads/) and execute the commands:

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Before starting. Please rename the file `.env.default` to `.env`, and set in it your Secret credentials.<br />
(`Twitter_Django/` also has a `.env.default` file.)

Running the server:<br />

```
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
$ python3 manage.py test
$ python3 manage.py runserver
```

Open [localhost:8000](http://localhost:8000) in a browser.

## Deployment (docker)

Install [docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/).
Perform the changes mentioned above related to `.env.default` files.

Running the server:<br />

```
$ docker-compose up -d
$ docker logs twitter-django -tf # logging
```

Open [localhost:PORT](http://localhost:PORT) in a browser. Where `PORT` is the port set in root project `.env` file.

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
