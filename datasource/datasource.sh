#!/usr/bin/env bash

# make sure wget is installed, as well as xlsx2csv
# $ apt-get install wget (Linux)
# $ brew install wget  (Mac)
# $ pip install xlsx2csv

# EU Open Data Portal
euopendata="https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide.xlsx"
wget ${euopendata} -O "covid19.xlsx" -o logfile
# dateRep, day, month, year, cases, deaths, countriesAndTerritories, geoId, 
# countryterritoryCode, popData2018, continentExp

# pip install xlsx2csv

xlsx2csv covid19.xlsx > covid19.csv
