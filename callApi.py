#!/usr/bin/env python

import urllib3
import json
import logging

import config as cfg

http = urllib3.PoolManager()
logging.basicConfig(filename="log.txt", level=logging.DEBUG,
                    format="%(asctime)s %(message)s")
class ApiQuery:
    def __init__(self, query, params):
        self.query = query
        self.params = params
        self.key = cfg.apiRequest["apiKey"]
        self.authHeaders  = {"Authorization":  f"Bearer: {self.key}"}
        
    def makeApiCall(self): 
        url = cfg.apiRequest["baseUrl"]+'/'+self.query
    
        try:
            req = http.request('GET', url, fields=self.params, headers=self.authHeaders)
            res = req.data
        except Exception as e:
            logging.error(f"Request failed\n{e}")
            raise e
        finally:
            if (req.status == 201 or req.status == 200): 
                resData = json.loads(res.decode('utf-8'))
                if resData["total_results"] != 0:
                    logging.info("GET request success")
                    logging.info(json.dumps(resData, indent=4))
                else:
                    logging.info("No results found for the query") 
                return "Request succeeded - please check logs for more info"
            else:  
                logging.error(f"Request failed\n{e}")
                return "Request failed"
            