# Project: Brewing Automation System - Capstone Project
# Purpose Details: To provide a sample code of how to delete records from a ServiceNow table
# Course: IST 440W - 001
# Author: Nahara
# Date Developed: 3/5/2020
# Last Date Changed: 3/11/2020
# Rev 3

#DELETE

#Need to install requests package for python
#easy_install requests
import requests

# Set the request parameters
# The long string at the end (after recipe/) is the SYS_ID of the record you want to delete

url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_recipe/a6313ebedbd3c010b42f51735e961902'

# User name="IST440", Password="IST440" for this code sample.
user = 'IST440'
pwd = 'IST440'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.delete(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)