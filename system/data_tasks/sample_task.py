import time
import json
import sys

params = {}

if __name__ == "__main__":
    # Read parameters from the command line argument
    try:
        params = json.loads(sys.argv[1])
        params["name"] is not None
        params["sleep_time"] is not None
    except (IndexError, KeyError):
        params = {"name": "No Param Given!!", "sleep_time": 0.2}
        
    

def sample_task():
    for i in range(10):
        # Simulate a long-running task
        time.sleep(params["sleep_time"])
        # Send intermediate update to the client
        
        print(f'Sample Data Task Progress for %s: {i+1}/10' % params["name"])
    print('Script completed!')
        
sample_task()