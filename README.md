| CI |
|----|
| [![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fmarshallmcdonnell%2Fcircuitbreaker-flask-example%2Fbadge%3Fref%3Dmaster&style=flat)](https://actions-badge.atrox.dev/marshallmcdonnell/circuitbreaker-flask-example/goto?ref=master) |

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



Usage
-----

Installation
------------

Clone repository and then install using pipenv: `pipenv install --dev`


Requirements
------------

Compatibility
-------------

Licence
-------

Authors
-------

`circuitbreaker-flask-example` was written by `Marshall McDonnell <mcdonnellmt@ornl.gov>`_.

