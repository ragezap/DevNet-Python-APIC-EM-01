import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "iQxshB9s7JEVAMDzfNKDpxXjvoZYS8lN"

while True:
    #print("\n")
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API status:      " + str(json_status) + " = A successuful route call.\n")
        print("Directions from  " + orig + " to " + dest)
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.2f}".format(json_data["route"]["distance"]*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format(json_data["route"]["fuelUsed"]*3.78))+"\n")