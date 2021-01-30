import csv
import json
import urllib.request
from matplotlib import pyplot as plt
import json
import urllib

print("Fetching Data for Germany:")
country = "Germany"


def fetch():
    url = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/json'
    with urllib.request.urlopen(url) as url:
        s = url.read()
        reader = json.load(url)
        for row in reader:
            if row['countriesAndTerritories'] == country:
                print(row['dateRep'], row['countriesAndTerritories'], "Cases: ", row['cases'])
        print(row)


def analyze():
    i = 0
    arrCases = []
    with open('covid19.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['countriesAndTerritories'] == country:
                i = i + 1
                print(row['dateRep'], row['countriesAndTerritories'], "Cases: ", row['cases'])
                arrCases.append(int(row['cases']))
    arrCases.reverse()
    print(list(range(i)))
    x_data = list(range(i))
    plt.plot(x_data, arrCases, c='r', label='data')
    plt.show()
    plt.title("Covid-19 Germany - All Time")
    plt.xlabel("Time (d)")
    plt.ylabel("Cases")
    plt.legend()

fetch()
