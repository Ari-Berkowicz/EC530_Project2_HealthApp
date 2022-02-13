# Receives a json file, parses it and sends it to the database location

import json
import datetime


def parse_json(filename):
    """
    Parses a json file and returns a list of dictionaries
    """
    # Create a time stamp and add it to the dictionary
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Open the file
    with open(filename, 'r') as f:
        # Read the file
        data = json.load(f)
        # Add the timestamp to the dictionary
        data['timestamp'] = timestamp
        # Return the data
        return data

# Log the data to the file in a folder
def log_to_folder(data):
    """
    Logs the data to a folder
    """
    # Create a file that goes into the folder

    with open(r'logs\logs.txt', 'w') as fp:
        fp.write(json.dumps(data) + '\n')
        pass

if __name__ == '__main__':
    # Get the data from the json file
    data = parse_json('data.json')
    # Log the data to the file
    log_to_folder(data)