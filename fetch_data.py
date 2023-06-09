import requests
import json

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

fetch_temp_data(params_240718, "240718_70b3d580a01005fd")