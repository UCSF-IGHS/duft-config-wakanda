import time
import json
import sys
from data_task_tools import something

something()
from src.dte.dte_tools import assert_dte_tools_available, get_duft_config, get_resolved_parameters_for_connection, set_data_task_name, log_error, log_message  # noqa: E402


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
    
    set_data_task_name("Sample Data Task")
    resolved_parameters = get_resolved_parameters_for_connection("ANA")
    log_message("Using parameters: %s" % resolved_parameters)
    
    for i in range(10):
        # Simulate a long-running task
        time.sleep(params["sleep_time"])
        # Send intermediate update to the client
        
        log_message(f'Progress for %s: {i+1}/10' % params["name"])
    log_message('Script completed!')
        



assert_dte_tools_available()
sample_task()