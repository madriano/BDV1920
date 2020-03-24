##############
# Logic layer
##############

import numpy as np
import pandas as pd
import json
import glob
import os
import logging

# sort of print
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# dealing with data computation 

class PandasDataModel:

	def __init__(self, path):
		logger.info("Starting up Data Model...")
		all_files = glob.glob(os.path.join(path, "*.csv"))
		df_from_each_file = (pd.read_csv(f) for f in all_files)
		self.data = pd.concat(df_from_each_file, ignore_index=True)
		self.data_dict = self.data.to_dict(orient='records')
		self.size = len(self.data)
		logger.info(self.data.head())
		logger.info("Data Model built.")
		

	# return the listings dataframe but in json format
	def getListings(self):
		return json.dumps(self.data_dict, indent=2)

	# return the filtered listings dataframe but in json format
	def getListingsByCountryRegion(self, countryregion):
		return json.dumps(self.data[self.data['Country/Region']==countryregion], indent=2)
	



#{
#    "Province/State": "Shaanxi",
#    "Country/Region": "Mainland China",
#    "Last Update": "2020-02-17T11:43:01",
#    "Confirmed": 240.0,
#    "Deaths": 0.0,
#    "Recovered": 79.0
#}
  