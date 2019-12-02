import logging
import requests
import time
from circuit import breaker 

from python_circuit_breaker_examples import mock_server

FAILURES = 2
TIMEOUT = 6

circuit_breaker = breaker.CircuitBreakerSet(
    time.time,
    logging.getLogger('python-circuit'),
    maxfail=FAILURES,
    reset_timeout=TIMEOUT)

circuit_breaker.handle_error(requests.exceptions.ConnectionError)

def get_greeting(url, port):
    ''' Get the main index page response '''
    response = requests.get("http://{}:{}/".format(url, port))
    return response.text

def greetings_test(iterations=10, delay=1, url="localhost", port=5000):

    for i in range(iterations):
        try:
            with circuit_breaker.context('get-greeting'):
                get_greeting(url, port) 
        except Exception as e:
            pass
 
        print_summary()
        time.sleep(delay) 
 
def print_summary():
    for name in circuit_breaker.circuits:
        cb = circuit_breaker.circuits[name]
        time_left = TIMEOUT
        if cb.last_change:
            time_left = TIMEOUT - (cb.clock() - cb.last_change)
        msg = "{} circuit state: {}. Time till open: {}"
        print(msg.format(name, cb.state, time_left))

if __name__ == "__main__":
    print("Server is turned OFF...") 
    greetings_test()
         
    print("Server is turning ON...") 
    with mock_server.app.run("localhost", 5000):
        greetings_test()
