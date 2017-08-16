# Flask Boiler

Simple boiler plate for Flask test apps. It has nothin but a wrapper for running a hello world Flask app.

## Run server

	python manage.py run

Bydefault Flask dev server run on host `127.0.0.1` (`localhost`) and port `5000`. You configure default port and host in `config.py`.

You can also specify `port` and `host` as a commandline params while running the dev server.

	python manage.py run --host 0.0.0.0 --port 9000