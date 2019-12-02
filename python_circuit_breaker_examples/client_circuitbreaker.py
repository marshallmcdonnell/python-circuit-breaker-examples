import requests
import time
from circuitbreaker import circuit, CircuitBreakerMonitor

from python_circuit_breaker_examples import mock_server

FAILURES=3
TIMEOUT=6

@circuit(failure_threshold=FAILURES, recovery_timeout=TIMEOUT)
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
    for x in CircuitBreakerMonitor.get_circuits(): 
        msg = "{} circuit state: {}. Time till open: {}"
        print(msg.format(x.name, x.state, x.open_remaining))

if __name__ == "__main__":
    print("Server is turned OFF...") 
    greetings_test()
         
    print("Server is turning ON...") 
    with mock_server.app.run("localhost", 5000):
        greetings_test()
