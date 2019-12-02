import requests
import time
import pybreaker

from python_circuit_breaker_examples import mock_server

circuit = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=6, name="get_greeting")

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
    msg = "{} circuit state: {}. Time till open: {}"
    print(msg.format(circuit.name, circuit._state_storage.state, circuit._state_storage.opened_at))

if __name__ == "__main__":
    print("Server is turned OFF...") 
    greetings_test()
         
    print("Server is turning ON...") 
    with mock_server.app.run("localhost", 5000):
        greetings_test()
