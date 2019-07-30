import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "iQxshB9s7JEVAMDzfNKDpxXjvoZYS8lN"

while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API status: " + str(json_status) + " = A successuful route call.\n")
