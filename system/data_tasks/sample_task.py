import time
import sys

from data_task_helpers import something

something()
from src.dte.dte_tools import assert_dte_tools_available, get_resolved_parameters_for_connection, initialise_data_task, log_error, log_message, find_json_arg  # noqa: E402


params = {}

if __name__ == "__main__":
    
    json_args = find_json_arg(sys.argv)
    initialise_data_task("Sample Data Task", params=json_args)
    
    params["name"] = json_args.get("name", "No parameters given!")
    params["sleep_time"] = json_args.get("sleep_time", 0.2)
    
    if not json_args:
        log_error("No parameters given!")
        

def sample_task():
    resolved_parameters = get_resolved_parameters_for_connection("ANA")
    log_message('Script starting!')
    log_message("Using Data Connection Parameters: %s" % resolved_parameters)
    
    for i in range(10):
        # Simulate a long-running task
        time.sleep(params["sleep_time"])
        # Send intermediate update to the client
        
        log_message(f'Progress for %s: {i+1}/10' % params["name"])
    log_message('Script completed!')
        



assert_dte_tools_available()
sample_task()