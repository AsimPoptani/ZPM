import psutil
import requests
from configparser import *
import datetime
import json


def main():
    try:
        # Load the main config file
        config_parser = SafeConfigParser()
        config_parser.read('config.ini')
    except ParsingError:
        print("There is a problem with the config.ini file.")
        exit()
    # Try and load up all the config stuff
    try:
        server_url = config_parser.get('master', 'url')
        server_port = config_parser.get('master', 'port')
        server_key = config_parser.get('master', 'key')
    except Exception:
        print("There is an issue with the config file please make sure you have all the settings required.")
        exit()

    ### Try and get the usage space for all partitions
    disk_partitions=psutil.disk_partitions()
    disk_usage=[]
    for partition in disk_partitions:
        disk_usage.append(psutil.disk_usage(partition[1]))
    # Generate the JSON we want to send 
    data = {
        'cpu': {
            'percent': {
                'overall': psutil.cpu_percent(),
                'individual': psutil.cpu_percent(percpu=True),
            },
            'freq': {
                'overall': psutil.cpu_freq(),
                'individual': psutil.cpu_freq(percpu=True)
            }
        },
        'disk': {
            'usage': disk_usage,
            'partitions': psutil.disk_partitions()

        },
        'memory': {
            'swap': psutil.swap_memory(),
            'virtual' : psutil.virtual_memory(),
        },
        'sensors': {
            'temperature' : psutil.sensors_temperatures(),
            'fan': psutil.sensors_fans(),
            'battery' : psutil.sensors_battery()
        },
        'date': datetime.datetime.utcnow().isoformat()
    }

    # Verify the connection to the server is good
    requests.post('http://localhost:5000',data={"body":json.JSONEncoder().encode(data)})
    
    # Get data from our PC every X seconds and send to server based on config file


# Check if we are the main process
if __name__ == "__main__":
    main()
