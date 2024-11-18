import json
import requests
import pandas as pd

def lambda_handler(event, context):
	print(event)
	res = requests.get("https://www.google.com")
	print(res.text)

	d = {"Col1": [1,2], "Col2": [3,4]}
	df = pd.DataFrame(Data=d)
	print(df)
	print("Demo Completed")
