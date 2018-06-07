
# coding: utf-8

# In[ ]:


import os
import urllib.request
import sys
import pandas as pd


""" Script for downloading data
    this function will download and then save a csv file 
    that has the required columns for our further calculations and plots.
    
Return:
    string: this is a string value that defines the *.csv file that was downloaded/stored.
"""
def download(stationid, year):
    print("Started downloading ...")
    print("Data for station with id {} for year {}".format(stationid, year))

    fname = "{}_{}_t.csv".format(stationid, year)
    url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(stationid)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"

    try:
        urllib.request.urlretrieve(url, fname)
    except FileNotFoundError as fnfe:
        print("File not found error")
        print("%s" % fnfe)
        return ""
    except Exception as e:
        print("%s" % e)
        return ""

    print("Download completed...")
    print("Extracting required columns...")

    data_frame = pd.read_csv(fname, skiprows=25, sep=",", encoding="ISO-8859-1")
    columns =range (0,10)
    df = data_frame.iloc[columns]
    df_rename = df.columns=["Date/Time","Year","Month","Day","Data Quality","Max Temp (°C)","Max Temp Flag","Min Temp (°C)","Min Temp Flag","Mean Temp (°C)"]
    new_fname =  os.path.dirname(os.path.realpath(__file__)) + "/../csv_data/{}_{}.csv".format(stationid, year)
    df_rename.to_csv(new_fname)
    print("File saved into: " + new_fname)

    # removing temporary saved file
    os.remove(fname)
    #print(df)
    print("File saved.")

