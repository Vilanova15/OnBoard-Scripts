import random as rnd
import time as t

from datetime import date as d
from radiodata.radiodata import RadioData
from data_to_csv import data_to_csv

date = d.today()
time = t.ctime().split()[3]
filename = "buggyData.csv"

data_list = [rnd.randint(0, 100) for i in range(15)]
gps_list = [rnd.randint(0, 100), rnd.randint(0, 100)]

dataObj = RadioData(data_list, gps_list)
dataObj.OBC_time = dataObj.GSC_time = time
dataObj.OBC_date = dataObj.GSC_date = date

data_to_csv(dataObj, filename)