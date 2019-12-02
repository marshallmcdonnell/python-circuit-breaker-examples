import datetime
import requests
import time
import pybreaker

from python_circuit_breaker_examples import mock_server

TIMEOUT = 6
circuit = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=TIMEOUT, name="get_greeting")
@circuit
def get_greeting(url, port):
    ''' Get the main index page response '''
    response = requests.get("http://{}:{}/".format(url, port))
    return response.text

def greetings_test(iterations=10, delay=1, url="localhost", port=5000):
    for i in range(iterations): 
        try: 
            get_greeting(url, port) 
        except: 
            pass
 
        print_summary()
        time.sleep(delay) 
 
def print_summary():
    name = circuit.name
    state = circuit._state_storage.state
    time_left = TIMEOUT
    if circuit._state_storage.opened_at:
        elapse_time = datetime.datetime.utcnow() - circuit._state_storage.opened_at
        time_left = TIMEOUT - elapse_time.total_seconds()
    print("{} circuit state: {}. Time till open: {}".format(name, state, time_left))

if __name__ == "__main__":
    print("Server is turned OFF...") 
    greetings_test()
         
    print("Server is turning ON...") 
    with mock_server.app.run("localhost", 5000):
        greetings_test()
