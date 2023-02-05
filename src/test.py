import unittest
from callApi import ApiQuery

class TestGetApiCall(unittest.TestCase):
    def runTest(self):

        params = {
        "query": "",
        "region": "DE",
        "sector":"Agriculture/Hunting/Forestry/Fishing",
        "source": "EXIOBASE",
        "year":"2021"
        }

        query = "search"
#Function call to print desired results
        apiQuery = ApiQuery(query,params)
        
        self.assertEqual(apiQuery.makeApiSearchCall(), "Request succeeded - please check logs for more info", "test success")

unittest.main()        