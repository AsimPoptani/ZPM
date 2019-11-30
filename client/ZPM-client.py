import psutil
import requests
from configparser import *


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
    
    # Verify the connection to the server is good
    
    # Get data from our PC every X seconds and send to server based on config file


# Check if we are the main process
if __name__ == "__main__":
    main()
