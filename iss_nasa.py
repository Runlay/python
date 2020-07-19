import urllib.request as urllib2
from datetime import datetime
from selenium import webdriver

import time, sys, json
from ipyleaflet import Map, Marker, basemaps, FullScreenControl, Icon, ScaleControl
import webbrowser

# import pyautogui


print("NASA ISS Current Location: ")
print("loading, please wait...")
driver = webdriver.FirefoxProfile()
driver = webdriver.Firefox(driver, executable_path=r'PATHTOYOURWEBDRIVER')
driver.get("PATHTOYOURLOCALWEBSITE");


while True:
    req = urllib2.Request("http://api.open-notify.org/iss-now.json")
    response = urllib2.urlopen(req)

    obj = json.loads(response.read())
    ts = int(obj['timestamp'])
    lat = obj['iss_position']['latitude']
    long = obj['iss_position']['longitude']

    sys.stdout.write("\r " + datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') + ": " + obj['iss_position']['latitude'] + " " + obj['iss_position']['longitude'])
    sys.stdout.flush()

    reqPassing = urllib2.Request("http://api.open-notify.org/iss-pass.json?lat=48.634566&lon=8.09760")
    responsePassing = urllib2.urlopen(reqPassing)
    fetchPassing = json.loads(responsePassing.read())
    passTime = int(fetchPassing['request']['datetime'])
    passTimeCounts = fetchPassing['request']['passes']


    for i in range(passTimeCounts):
        riseTime = int(fetchPassing['response'][i]['risetime'])
        print("ISS Overflight " +str(i+1)+": "+ datetime.utcfromtimestamp(passTime).strftime('%Y-%m-%d %H:%M:%S'))
        i=+1

    m = Map(basemap=basemaps.Esri.WorldImagery, center=(lat, long), zoom=2, scroll_wheel_zoom=True)
    m.add_layer(Marker(location=(lat, long), title="ISS", icon=Icon(icon_url="https://img.icons8.com/fluent/48/000000/gps-device.png", icon_size=[20,20])))
    m.add_control(FullScreenControl())
    m.add_control(ScaleControl(position='bottomleft'))
    m.save('current state.html', title="Space Radar")
    driver.refresh();
    time.sleep(30.0)
