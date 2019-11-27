import requests
import time
from circuitbreaker import circuit, CircuitBreakerMonitor

from circuitbreaker_flask_example import mock_server

@circuit(failure_threshold=3, recovery_timeout=6)
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
