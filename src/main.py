#ProjectGoCarbonNeutral
# Query to search, emission factors by adding filters for "region","sector","source","year" 
# changes can be made based on what data you would like to query. 
#In this project, we focus on calculating total CO2 emission (kg/EUR) 
# for every activity in Germany in the year 2021.
#The data source suggests that the factors were calculated based on 2019 data.

#import the built-in package re to work with RegEx
import re 
#Import the class ApiQuery from python file callApi
from callApi import ApiQuery
def main():
# Define Dictionary 'params' for search query 
# To know more about data source visit https://www.exiobase.eu/
    params = {
    "query": "",
    "region": "DE",
    "sector":"",
    "source": "EXIOBASE",
    "year":""
    }

    query = "search"
#Function call to print desired results
    searchApiQuery = ApiQuery(query,params)
    res = searchApiQuery.makeApiSearchCall()
    print(res)
    
    estimateQuery = "estimate"
    estimateParams = {
      "emission_factor": {
        "activity_id": "heat-and-steam-type_purchased"
       },
      "parameters": {
        "energy": 100,
        "energy_unit": "kWh"
      }
  }
    estimateApi = ApiQuery(estimateQuery,estimateParams)
    estimatedRes= estimateApi.makeApiEstimateCall()
    print(estimatedRes)


if __name__ == '__main__':
    main()
