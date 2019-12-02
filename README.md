| CI | License | Compatibility |
|----|---------|---------------|
| [![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fmarshallmcdonnell%2Fpython-circuit-breaker-examples%2Fbadge%3Fref%3Dmaster&style=flat)](https://actions-badge.atrox.dev/marshallmcdonnell/python-circuit-breaker-examples/goto?ref=master) | [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) | ![python compability](.images/python-compatibility-badge.svg) |

# python-circuit-breaker-examples

Working examples of using different Python Circuit Breaker packages, with a Flask mock server using [http-server-mock](https://github.com/ezequielramos/http-server-mock)

The main purpose is to show how a Cicuit Breaker pattern will work
using these packages:

 * [circuitbreaker](https://github.com/fabfuel/circuitbreaker)
 * [pybreaker](https://github.com/danielfm/pybreaker)
 * [python-circuit](https://github.com/edgeware/python-circuit)
 

The client codes calls against a "REST" API service on an "unreliable" mock server.
We have a mock Flask server that we can spin up or down inline
using the [http-server-mock](https://github.com/ezequielramos/http-server-mock) package
to control whether our client responses are successful or not
in order to test how the circuit breaker works for an un-responsive service (ie the mocker server).



# Installation

Clone repository and then install using [pipenv](https://pipenv.readthedocs.io/en/latest/): `pipenv install --dev`

# Usage


After installation, you can run the following circuit breaker examples.

Each have the same scenario:
 * Start with a "closed" circuit
 * Start with a "down" REST API service (server is OFF)
 * Have a maximum of 3 tries to connect till the circuit pops "open"
 * Have a 6 second delay till the circuit is tested again in "half-open" state
 * Issue 10 API calls on 1 second delays to the endpoint till the server comes back ON
 * Issue 10 more API calls with the API service back up to show the change over to a "closed" state

## [circuitbreaker](https://github.com/fabfuel/circuitbreaker)

**Run**
```
pipenv run python python_circuit_breaker_examples/client_circuitbreaker.py
```

**Output**
```
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
 * Serving Flask app "python_circuit_breaker_examples.mock_server" (lazy loading)
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

## [PyBreaker](https://github.com/danielfm/pybreaker)

**Run**
```
pipenv run python python_circuit_breaker_examples/client_pybreaker.py
```

**Output**
```
Server is turned OFF...
get_greeting circuit state: closed. Time till open: 6
get_greeting circuit state: closed. Time till open: 6
get_greeting circuit state: open. Time till open: 5.999963
get_greeting circuit state: open. Time till open: 4.999796
get_greeting circuit state: open. Time till open: 3.998742
get_greeting circuit state: open. Time till open: 2.998512
get_greeting circuit state: open. Time till open: 1.9983659999999999
get_greeting circuit state: open. Time till open: 0.9972519999999996
get_greeting circuit state: open. Time till open: 5.999966
get_greeting circuit state: open. Time till open: 4.999445
Server is turning ON...
 * Serving Flask app "python_circuit_breaker_examples.mock_server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://localhost:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [02/Dec/2019 15:53:41] "PUT /cc77db26-1545-11ea-9309-a08cfd9fd53c/cc77db27-1545-11ea-9309-a08cfd9fd53c HTTP/1.1" 200 -
get_greeting circuit state: open. Time till open: 3.986439
get_greeting circuit state: open. Time till open: 2.985255
get_greeting circuit state: open. Time till open: 1.9841490000000004
get_greeting circuit state: open. Time till open: 0.9830350000000001
127.0.0.1 - - [02/Dec/2019 15:53:45] "GET / HTTP/1.1" 200 -
get_greeting circuit state: closed. Time till open: -0.022205999999999726
127.0.0.1 - - [02/Dec/2019 15:53:46] "GET / HTTP/1.1" 200 -
get_greeting circuit state: closed. Time till open: -1.027672
127.0.0.1 - - [02/Dec/2019 15:53:47] "GET / HTTP/1.1" 200 -
get_greeting circuit state: closed. Time till open: -2.0347880000000007
127.0.0.1 - - [02/Dec/2019 15:53:48] "GET / HTTP/1.1" 200 -
get_greeting circuit state: closed. Time till open: -3.039009
127.0.0.1 - - [02/Dec/2019 15:53:49] "GET / HTTP/1.1" 200 -
get_greeting circuit state: closed. Time till open: -4.043248
127.0.0.1 - - [02/Dec/2019 15:53:50] "GET / HTTP/1.1" 200 -
get_greeting circuit state: closed. Time till open: -5.049541
```

## [python-circuit]()

**Run**
```
pipenv run python python_circuit_breaker_examples/client_python_circuit.py
```

**Output**
```
Server is turned OFF...
get-greeting circuit state: closed. Time till open: 6
get-greeting circuit state: closed. Time till open: 6
got error ConnectionError(MaxRetryError("HTTPConnectionPool(host='localhost', port=5000): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f47d864d518>: Failed to establish a new connection: [Errno 111] Connection refused',))",),) - opening circuit
get-greeting circuit state: open. Time till open: 5.999971866607666
get-greeting circuit state: open. Time till open: 4.99871563911438
get-greeting circuit state: open. Time till open: 3.997462511062622
get-greeting circuit state: open. Time till open: 2.996232032775879
get-greeting circuit state: open. Time till open: 1.995251178741455
get-greeting circuit state: open. Time till open: 0.9939932823181152
got error ConnectionError(MaxRetryError("HTTPConnectionPool(host='localhost', port=5000): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f47d864dba8>: Failed to establish a new connection: [Errno 111] Connection refused',))",),) - opening circuit
get-greeting circuit state: open. Time till open: 5.999970436096191
get-greeting circuit state: open. Time till open: 4.998587608337402
Server is turning ON...
 * Serving Flask app "python_circuit_breaker_examples.mock_server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://localhost:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [02/Dec/2019 17:18:03] "PUT /95645fa4-1551-11ea-9309-a08cfd9fd53c/95645fa5-1551-11ea-9309-a08cfd9fd53c HTTP/1.1" 200 -
get-greeting circuit state: open. Time till open: 3.941380500793457
get-greeting circuit state: open. Time till open: 2.940016746520996
get-greeting circuit state: open. Time till open: 1.9387359619140625
get-greeting circuit state: open. Time till open: 0.9375171661376953
127.0.0.1 - - [02/Dec/2019 17:18:07] "GET / HTTP/1.1" 200 -
get-greeting circuit state: closed. Time till open: -0.0850987434387207
127.0.0.1 - - [02/Dec/2019 17:18:08] "GET / HTTP/1.1" 200 -
get-greeting circuit state: closed. Time till open: -1.0990118980407715
127.0.0.1 - - [02/Dec/2019 17:18:09] "GET / HTTP/1.1" 200 -
get-greeting circuit state: closed. Time till open: -2.1185436248779297
127.0.0.1 - - [02/Dec/2019 17:18:10] "GET / HTTP/1.1" 200 -
get-greeting circuit state: closed. Time till open: -3.138019561767578
127.0.0.1 - - [02/Dec/2019 17:18:11] "GET / HTTP/1.1" 200 -
get-greeting circuit state: closed. Time till open: -4.158687353134155
127.0.0.1 - - [02/Dec/2019 17:18:12] "GET / HTTP/1.1" 200 -
get-greeting circuit state: closed. Time till open: -5.178531169891357
```

Authors
-------

`python-circuit-breaker-examples` was written by [Marshall McDonnell](https://github.com/marshallmcdonnell)

