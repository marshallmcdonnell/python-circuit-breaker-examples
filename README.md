| CI | License | Compatibility |
|----|---------|---------------|
| [![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fmarshallmcdonnell%2Fcircuitbreaker-flask-example%2Fbadge%3Fref%3Dmaster&style=flat)](https://actions-badge.atrox.dev/marshallmcdonnell/circuitbreaker-flask-example/goto?ref=master) | [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) | ![python compability](.images/python-compatibility-badge.svg) |

circuitbreaker-flask-example
==========

Working example of using [circuitbreaker](https://github.com/fabfuel/circuitbreaker) package
with a Flask mock server using [http-server-mock](https://github.com/ezequielramos/http-server-mock)

The main purpose is to show how a Cicuit Breaker pattern will work
using the [circuitbreaker](https://github.com/fabfuel/circuitbreaker) package
on "client" calls against a REST API service on an "unreliable" mock server.
We have a mock Flask server that we can spin up or down inline
using the [http-server-mock](https://github.com/ezequielramos/http-server-mock) package
to control whether our client responses are successful or not
in order to test how the circuit breaker works for an un-responsive service (ie mocker server).



Installation
------------

Clone repository and then install using pipenv: `pipenv install --dev`

Usage
-----

After installation, can run example of circuit breaker working via `pipenv run python circuitbreaker_flask_example/client.py`

**Output**
```python
Server is turned OFF...
get_greeting circuit state: closed. Time till open: 5.99578
get_greeting circuit state: closed. Time till open: 4.956267
get_greeting circuit state: open. Time till open: 5.999928
get_greeting circuit state: open. Time till open: 4.998572
get_greeting circuit state: open. Time till open: 3.997259
get_greeting circuit state: open. Time till open: 2.995893
get_greeting circuit state: open. Time till open: 1.994597
get_greeting circuit state: open. Time till open: 0.993119
get_greeting circuit state: open. Time till open: 5.999976
get_greeting circuit state: open. Time till open: 4.998959
Server is turning ON...
 * Serving Flask app "circuitbreaker_flask_example.mock_server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://localhost:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [02/Dec/2019 12:35:07] "PUT /0ed229fc-152a-11ea-9309-a08cfd9fd53c/0ed229fd-152a-11ea-9309-a08cfd9fd53c HTTP/1.1" 200 -
get_greeting circuit state: open. Time till open: 3.93516
get_greeting circuit state: open. Time till open: 2.933744
get_greeting circuit state: open. Time till open: 1.932458
get_greeting circuit state: open. Time till open: 0.93114
127.0.0.1 - - [02/Dec/2019 12:35:11] "GET / HTTP/1.1" 200 -
get_greeting circuit state: closed. Time till open: -0.089294
127.0.0.1 - - [02/Dec/2019 12:35:12] "GET / HTTP/1.1" 200 -
get_greeting circuit state: closed. Time till open: -1.093669
127.0.0.1 - - [02/Dec/2019 12:35:13] "GET / HTTP/1.1" 200 -
get_greeting circuit state: closed. Time till open: -2.111054
127.0.0.1 - - [02/Dec/2019 12:35:14] "GET / HTTP/1.1" 200 -
get_greeting circuit state: closed. Time till open: -3.115754
127.0.0.1 - - [02/Dec/2019 12:35:15] "GET / HTTP/1.1" 200 -
get_greeting circuit state: closed. Time till open: -4.122443
127.0.0.1 - - [02/Dec/2019 12:35:16] "GET / HTTP/1.1" 200 -
get_greeting circuit state: closed. Time till open: -5.134389
```

Requirements
------------

Authors
-------

`circuitbreaker-flask-example` was written by [Marshall McDonnell](https://github.com/marshallmcdonnell)

