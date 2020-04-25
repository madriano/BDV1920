"""
Spark read/write model
"""
from __future__ import print_function

from pyspark.sql.types import *

#import numpy as np
import pandas
import json
#import glob
#import os
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
			
		self.rawcovid19 = spark.read.csv(filename, sep=",", inferSchema="true", header="true")
		
	
	def write_rawdata(self, spark, filename):
			
		self.rawcovid19.coalesce(1).write.csv(filename)  # all together as one file

	
	def write_data(self, spark, filename):
			
		self.covid19.write.csv(filename)
		
		
	def __init__(self, spark, filename):
			
		logger.info(" Data model will be from: "+filename)
		# recall that Spark follows lazy computation
		
		self.read_data(spark, filename)
		
		# process dataframes then store outcome as a SQL table
		# (further processing, if wanted)
		self.covid19 = self.rawcovid19.drop("day", "month", "year", "geoId", "countryterritoryCode", "continentExp")
		#self.covid19.cache
		# register dataframes as a SQL temporary view
		self.covid19.createOrReplaceTempView("covid19")
		#self.covid19.createGlobalTempView(self.covid19table)
		
		logger.info(" Data Model built.")


	def all(self, spark):
		# df = self.covid19
		# then using dataframe operators
		# or else ...
		df = spark.sql("SELECT dateRep AS day, cases, deaths, countriesAndTerritories AS country FROM covid19")
		# collect toPandas - records, columns, or index
		listing = df.toPandas().to_dict(orient='records') 
		# converts Python dictionary to final json string
		jsonlisting = json.dumps(listing, indent=2)
		#logger.info(jsonlisting)
		return jsonlisting

	def filtering_by_country(self, spark, country):
    		
		df = spark.sql("SELECT dateRep AS day, cases, deaths, countriesAndTerritories AS country FROM covid19")
		# some tests ...
		df = df.filter(df.country.like(country))
	
		listing = df.toPandas().to_dict(orient='records') 
		jsonlisting = json.dumps(listing, indent=2)
		#logger.info(jsonlisting)
		return jsonlisting


	# more processing ... as needed
	
	# more getters ... as needed
	