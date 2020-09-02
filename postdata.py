import requests as req
import json
import time as t
import queue
from datetime import datetime
from radiodata.radiodata import RadioData
from radio_to_csv.csv_script_test import generate_random_positions, generate_random_data

def post_data(json_input, data_queue):

        url = "http://localhost:3000/api/"
        headers = {'content-type': 'application/json'}

        data_received = json.loads(json_input.decode('utf-8')) # dict
        data_to_post = data_received["data"] # dict

        url = url + data_received["buggy_name"] + '/' # str

        print(req.post(url, data=json.dumps([data_to_post]), headers=headers))

        # try:
        #         r = req.getAll()  
        #         if not data_queue.empty():  
        #                 for i in range(data_queue.qsize()):
        #                         d = data_queue.get()  
        #                         req.post(url, data=json.dumps([d]), headers=headers)
        #         else:
        #                 req.post(url, data=json.dumps([data_to_post]), headers=headers) 
        #                 t.sleep(3)
        # except:
        #         print("No connection! Queueing data...")
        #         data_queue.put(data_to_post)
        #         t.sleep(3)
