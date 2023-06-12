import requests
import json
import os

def create_folder(folder_path):
    exist = os.path.exists(folder_path)
    if not exist:
        os.makedirs(folder_path)
        print(f"{folder_path} created")

params_240718 = {
    "horodate__lt": "2018-07-24%2011:05:05",
    "horodate__gt": "2018-07-24%2009:55:05",
    "deveui__eq": "70b3d580a01005fd",
    "maxfeatures": 1200
}

def fetch_temp_data(params, file_name):

    url = "https://download.data.grandlyon.com/ws/timeseries/biotope.temperature/all.json?"

    for param, value in params.items():
        url += f"{param}={value}&"

    print(url)

    # Send GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON data
        data = response.json()

        nb_results = data["nb_results"]
        print(f"{nb_results} results")

        # Specify the output file name
        output_file = f"{file_name}.json"

        # Write the JSON data to the output file
        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)
        
        print("Data saved to", output_file)
    else:
        print("Failed to fetch data from the API")

# fetch_temp_data(params_240718, "240718_70b3d580a01005fd")

def fetch_data_period(folder, period):
    """Fetch all data from a period and store them into multiple files
        it divides the data into 3 parts of the day : 
        Morning : 9h-14h
        Afternoon : 14h-19h
        Evening : 19h-00h
    """
    
    create_folder(folder)

    for day in period:
        morning_params = {
            "horodate__lt": f"{day}%2014:00:00",
            "horodate__gt": f"{day}%2009:00:00",
        }
        afternoon_params = {
            "horodate__lt": f"{day}%2019:00:00",
            "horodate__gt": f"{day}%2014:00:00",
        }
        evening_params = {
            "horodate__lt": f"{day}%2023:59:00",
            "horodate__gt": f"{day}%2019:00:00",
        }
        fetch_temp_data(morning_params, f"{folder}/{day}_morning")
        fetch_temp_data(afternoon_params, f"{folder}/{day}_afternoon")
        fetch_temp_data(evening_params, f"{folder}/{day}_evening")

period = ["2018-05-23", "2018-05-24", "2018-05-25", "2018-05-26", "2018-05-27"]

fetch_data_period("./data/output/may_2018", period)