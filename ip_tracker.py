import requests
import time
import csv

filein = open("log.txt", "r")
fileout = open('output.csv', 'w')


for line in filein:
    quick_list = line.strip().split('-')
    suspectip = quick_list[0].strip()

    #Retrieve the location from the API. Rate limit on API is 45 req/min.
    try:
        response = requests.get('http://ip-api.com/json/' + suspectip)
        a = response.json()
        time.sleep(3)
        print(response)

    except: 
        print("An error has occurred." )
        print(response)

    b = a['country']
    output = suspectip + "," + b + '\n'

    #Write to the CSV.
    fileout.write(output)
filein.close()
fileout.close()