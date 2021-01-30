import csv
import urllib.request
from matplotlib import pyplot as plt
import json
import urllib

print("Fetching Data for Germany:")
country = "Germany"


def fetch():
    url = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/json'
    i = 0
    d= 0
    arrCases = []
    arrDeaths = []
    with urllib.request.urlopen(url) as url:
        s = url.read()
        reader = json.loads(s)

      #Join record data table
        for row in reader['records']:
            if row['countriesAndTerritories'] == country:
                i = i + 1
                d=  d + 1
                print(row['dateRep'], row['countriesAndTerritories'], "Cases: ", row['cases_weekly'], "Deaths: ",row["deaths_weekly"])
                arrCases.append(int(row['cases_weekly']))
                arrDeaths.append(int(row['deaths_weekly']))

    ############################################################################
    #testing
    testing = "https://opendata.ecdc.europa.eu/covid19/testing/json/"
    arrTesting = []
    t = 0
    with urllib.request.urlopen(testing) as url:
        s = url.read()
        reader = json.loads(s)

        # Join record data table
        for row in reader:
            if row['country'] == country:
                t = t + 1
                print(row['new_cases'])
                # print(row['tests_done'])
                # print(row['population'])
                arrTesting.append(int(row['tests_done']))

    arrCases.reverse()
    arrDeaths.reverse()
    #arrTesting.reverse()
    print(list(range(i)))
    x_data = list(range(i))
    x2_data = list(range(t))
    plt.plot(x_data, arrCases, c='r', label='Cases')
    plt.grid(x_data, arrDeaths, c='r', label='Deaths')
    #plt.plot(x2_data, arrTesting, c='r', label='Testing')
    plt.show()
    plt.title("Covid-19 Germany - All Time")
    plt.xlabel("Time (week)")
    plt.ylabel("Cases Per Week")
    plt.legend()

fetch()
def testing():
    testing ="https://opendata.ecdc.europa.eu/covid19/testing/json/"
    arrTesting =[]
    t=0
    with urllib.request.urlopen(testing) as url:
        s = url.read()
        reader = json.loads(s)

        # Join record data table
        for row in reader:
            if row['country'] == country:
                t=t+1
                print(row['new_cases'])
                #print(row['tests_done'])
                #print(row['population'])
                arrTesting.append(int(row['tests_done']))

testing()



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
