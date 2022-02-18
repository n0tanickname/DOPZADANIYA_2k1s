import requests
import sys

def a():

    acttype = str(input("TYPE - "))
    if acttype != "":
        acttype = "type=" + acttype + "&"

    actprice = str(input("PRICE - "))
    if actprice != None:
        actprice = "price=" + actprice + "&"

    actpeople = str(input("PEOPLE - "))
    if actpeople != None:
        actpeople = "people=" + actpeople

    link = "http://www.boredapi.com/api/activity?" + acttype + actprice + actpeople

    open("activities.txt", "w").close()

    for i in range(5):
        response = requests.get(link)
        data = response.json()
        if data.get("error") != None:
            print("No activities found")
            sys.exit()

        line = data.get("activity") + " [" + data.get("type") + "]. Price - " + str(data.get("price"))
        print(line)
        with open("activities.txt", "a") as file:
            file.write(str(line))
            file.write("\n")

a()
