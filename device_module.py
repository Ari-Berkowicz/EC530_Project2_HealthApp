# Receives a json file, parses it and sends it to the database location

import json
import datetime

from numpy import append
import mysql.connector


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


def errors():
    """
    Returns a list of errors
    """
    errors = []
    # Check if the data is a dictionary
    if not isinstance(data, dict):
        errors.append('The data is not a dictionary')
    # Check if the data has the correct keys
    if not all(
            key in data
            for key in ['timestamp', 'temperature', 'humidity', 'pressure']):
        errors.append(
            'The data is missing the following keys: timestamp, temperature, humidity, pressure'
        )
    # Check if the data has the correct values
    if not all(
            isinstance(data[key], (int, float))
            for key in ['temperature', 'humidity', 'pressure']):
        errors.append(
            'The data has the following values that are not numbers: temperature, humidity, pressure'
        )
    # Check if the data has the correct values
    if not isinstance(data['timestamp'], str):
        errors.append(
            'The data has the following values that are not strings: timestamp'
        )
    # Return the errors list
    return errors


    # grab data from mysql database
def grab_data():
    """
    Grabs data from the database
    """
    # Connect to the database
    cnx = mysql.connector.connect(
        host="",
        user="",
        password="")
    # Create a cursor
    cursor = cnx.cursor()
    # Create a query
    query = "SELECT * FROM health_data"
    # Execute the query
    cursor.execute(query)
    # Fetch the data
    data = cursor.fetchall()
    # Close the cursor
    cursor.close()
    # Close the connection
    cnx.close()
    # Return the data
    return data


# Insert data from json file into the database
def insert_data(data):
    """
    Inserts data into the database
    """
    # Connect to the database
    cnx = mysql.connector.connect(
        host="",
        user="",
        password="",
        database="")
    # Create a cursor
    cursor = cnx.cursor()
    # append the data to the database
    
    # Execute the query
    # print(data["users"][0])
    # print(data["timestamp"])
    dataTimestamp = data["timestamp"]
    # query = "INSERT INTO health_data (timestamp) VALUES (%s)"
    # query = "INSERT INTO health_data (%d, %d,  %s, %s) VALUES (%s,%s,%s,%s)"
    # cursor.execute(query, [data["timestamp"]])
    # queryTemperature = "INSERT INTO health_data (temperature) VALUES (%f)"
    
    # cursor.execute(queryTemperature, [55.0])
    index = 0 
    for item in data["users"]:
        # print(item['temperature'])
        # cursor.execute("INSERT INTO table VALUES (%s, %s, %s)", (var1, var2, var3))
        # cursor.execute("INSERT INTO health_data (timestamp, temperature) VALUES (%s,%s)", ((datetime.datetime.now() + datetime.timedelta(days=4)), 0))
        # cursor.execute(query, [data["timestamp"]], item["temperature"], item["humidity"], item["pressure"])
        print("ID: ",item["id"],"\n")
        y = json.dumps(str(item["conversations"]))
        print(y)
        cursor.execute("INSERT INTO health_data (id,timestamp, temperature ,name, email, password, role, family_member_id, doctor_id, converstations) VALUES (%s,%s, %s,%s,%s, %s,%s,%s, %s, %s)", (item["id"],data["timestamp"], item["temperature"], item["name"], item["email"], item["password"], item["role"], item["family_member_id"], item["doctor_id"],y))
        index +=1

    # for item in data["users"]:
    #     print( item["temperature"], item["humidity"], item["pressure"])
    # cursor.execute(query, item["timestamp"], item["users"]["temperature"], item["users"]["humidity"], item["users"]["pressure"])
    # Commit the changes
    cnx.commit()
    # Close the cursor
    # Close the cursor
    cursor.close()
    # Close the connection
    cnx.close()
    # Return the data
    return data


# Create a database
def create_database():
    """
    Creates a database
    """
    # Connect to the database
    cnx = mysql.connector.connect(
        host="",
        user="",
        password="")
    # Create a cursor
    cursor = cnx.cursor()
    # Create a query
    query = "CREATE DATABASE IF NOT EXISTS healthapplicationdb"
    # Execute the query
    cursor.execute(query)
    # Commit the changes
    cnx.commit()
    # Close the cursor
    cursor.close()
    # Close the connection
    cnx.close()
    # Return the data
    return data

# create a table in the database
def create_table():
    """
    Creates a table in the database
    """
    # Connect to the database
    cnx = mysql.connector.connect(
        host="",
        user="",
        password="",
        database="")
    # Create a cursor
    cursor = cnx.cursor()
    # A comment.
    query = "CREATE TABLE health_data (timestamp DATE NOT NULL,id INT NOT NULL, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, role VARCHAR(255) NOT NULL, family_member_id VARCHAR(255) NOT NULL, doctor_id VARCHAR(255) NOT NULL, patient_id VARCHAR(255) NOT NULL, nurse_id VARCHAR(255) NOT NULL, admin_id VARCHAR(255) NOT NULL, location_id VARCHAR(255) NOT NULL, blood_pressure FLOAT(10,2) NOT NULL, heart_rate FLOAT(10,2) NOT NULL, temperature FLOAT(10,2) NOT NULL,weight FLOAT(10,2) NOT NULL, height FLOAT(10,2) NOT NULL, bmi FLOAT(10,2) NOT NULL, pulse_rate FLOAT(10,2) NOT NULL, oximeter FLOAT(10,2) NOT NULL, glucometer FLOAT(10,2) NOT NULL, converstations JSON NOT NULL, PRIMARY KEY (id))"
    # Execute the query
    cursor.execute(query)
    # Commit the changes
    cnx.commit()
    # Close the cursor
    cursor.close()
    # Close the connection
    cnx.close()
    # Return the datas
    return data


if __name__ == '__main__':
    # Get the data from the json file
    data = parse_json('data.json')
    # Log the data to the file
    log_to_folder(data)
    # create_database()
    create_table()

    insert_data(data)
    # grab_data()