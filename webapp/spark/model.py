"""
Spark read/write model
"""
from __future__ import print_function

from pyspark.sql.types import *

import numpy as np
import pandas as pd
import json
import glob
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#######################################################
# Data from EU Open Data portal
# 	dateRep, day, month, year, cases, deaths, 
# 	countriesAndTerritories, geoId, 
# 	countryterritoryCode, popData2018, continentExp
#######################################################
	
class Model:
	
	def read_data(self, spark, filename):
			
		self.rawconfirmed = spark.read.csv(filename, sep=",", inferSchema="true", header="true")
		
	
	def write_rawdata(self, spark, filename):
			
		self.rawconfirmed.write.csv(filename)

	
	def write_data(self, spark, filename):
			
		self.confirmed.write.csv(filename)
		

		
	def __init__(self, spark, filename):
			
		logger.info("Starting up Data Model from: "+filename)
		self.read_data(spark, filename)
		self.rawconfirmed.printSchema()
		self.rawconfirmed.show(10)

		# process dataframes then store outcome as a SQL table
		#conf = self.rawconfirmed.drop(['Province/State', 'Lat', 'Long'])
		# TODO: further processing, as wanted

		# register dataframes as a SQL temporary view
		self.confirmedtable = "confirmed"
		#conf.createOrReplaceTempView(self.confirmedtable)
		conf.createGlobalTempView(self.confirmedtable)
		logger.info("Data Model built.")

	
	def confirmed_table(self):
			
		return self.confirmedtable

	
	def confirmed_json(self):
		
		df = spark.sql("SELECT * FROM self.confirmedtable")
		return json.dumps(df, indent=2)

	# more processing ... as needed
	
	# more getters ... as needed
	



# Global temporary view is tied to a system preserved database `global_temp`
# spark.sql("SELECT * FROM global_temp.people").show()
# Global temporary view is cross-session
# spark.newSession().sql("SELECT * FROM global_temp.people").show()
