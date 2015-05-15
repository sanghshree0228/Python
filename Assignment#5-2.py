import urllib.request
import json
from pprint import pprint

page = urllib.request.urlopen("https://restcountries.eu/rest/v1/alpha/co")
content=page.read()
content_string = content.decode("utf-8")

json_data = json.loads(content_string)
countryCode = input("Please enter country code: ")
altspellings=json_data["altSpellings"]
found = False
for i,quote in enumerate(altspellings):
	found_at=quote.find(countryCode)
	if(found_at>=0):
		print("Country name is = ", json_data["name"])
		print("Capital is = ", json_data["capital"])
		found=True
if(found!=True):
	print("Sorry the code doesnot exists")
