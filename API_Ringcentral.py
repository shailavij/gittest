# API call to RingcentralEndpoint for Google Ads Project

import requests
import time

def api():

    # defining the api-endpoint
    API_ENDPOINT = "https://marketing.utilityswitchboard.com/getMonitorCount"

    # sending post request and saving response as response object
    response = requests.get(url=API_ENDPOINT)
    print(response.status_code)
    jsonresp = response.json()

    # Parse Json file from response
    for key,val in jsonresp.items():
        print(key ,":", val)

    Agentcount= jsonresp["availableCount"]
    queuecount = jsonresp["queueCount"]

    #print("Agent_Availablecount",Agentcount)
    #print("queuecount",queuecount)
    return(Agentcount,queuecount)

if __name__ == "__main__":
    api()
