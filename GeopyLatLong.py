import pandas as pd
pd.set_option('display.max_columns', None)
from geopy.geocoders import Nominatim
import geopy
import time
dist=pd.read_csv("[4-006]SCHOOL_LAT_LONG.csv")


locationlist=[]
geolocator = Nominatim(user_agent="my-applmmmication-1")
for i in dist[16300:].index:
    try:
        strneed=str(dist["Latitude"][i])+", "+str(dist["Longitude"][i])
        location = "\""+str(dist["SCHOOL"][i])+"\""+"," +"\""+str(geolocator.reverse(strneed))+"\""
        with open('locationlist.txt', 'a') as file:
            file.write(location + '\n')
    except:
        geolocator = Nominatim(user_agent="my-applmmmication-1"+str(i))
        strneed=str(dist["Latitude"][i])+", "+str(dist["Longitude"][i])
        location = "\""+str(dist["SCHOOL"][i])+"\""+"," +"\""+str(geolocator.reverse(strneed))+"\""
        print(location)
        with open('locationlist.txt', 'a') as file:
            file.write(location + '\n')
