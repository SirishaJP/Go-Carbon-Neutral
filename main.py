import re
from callApi import ApiQuery

def main():
    params = {
    #"category": "Road Travel",
    "query": "",
    #"region": "GB",
    "sector":"Transport",
    #"source": "",
    #"year":"",
    }

    query = "search"

    apiQuery = ApiQuery(query,params)
    res = apiQuery.makeApiCall()
    print(res)

if __name__ == '__main__':
    main()