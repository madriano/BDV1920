"""
Example of app: Covid19
"""

from flask import Flask, request, render_template, jsonify
import json
import os
import logging

# importing own code 
from spark.spark import init_spark_session, stop_spark_session
from spark.model.covid19 import Covid19Model

# sort of print
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# variables to hold/control information
datasource = os.path.abspath(os.path.dirname(__file__)) + "/datasource/covid19.csv"
datalatlng = os.path.abspath(os.path.dirname(__file__)) + "/datasource/latlng.csv"
logger.info(" Raw data filename will be: " + datasource)
model = None
spark = init_spark_session("BDVapp")
app = Flask(__name__)

# set routes to control the app

@app.route('/', methods=['GET'])
def home():
	logger.info(" ROUTE: / => Home")
	return render_template('home.html',
							title='Big Data Visualization',
							template='home-template'
						)

@app.route('/mod', methods=['GET'])
def model():
    # create model
	logger.info(" ROUTE: /mod => Create model")
	global spark, datasource, datalatlng, model
	model = Covid19Model(spark, datasource, datalatlng)

	return render_template('covid19/model.html',
							title='Big Data Visualization',
							template='model-template'
						)

@app.route('/vismod/<country>', methods=['GET'])
def vismodel(country):
    # provide a snapshot of the model 
	# ex: by filtering one country if given
	logger.info(" ROUTE: /vismod => Visualize the model")
	global spark, model
	listing = {}
	if model is not None:
		if country == 'all':
			listing = model.all(spark)
		else:
			listing = model.filtering_by_country(spark, country)
	
	return render_template('covid19/vismodel.html', 
							title='Big Data Visualization',
							data=listing,
							template='vismodel-template'
						)

@app.route('/about', methods=['GET'])
def about():
    # about ... kind of checking if app/routes are working
	logger.info(" ROUTE: /about => About")
	return render_template('about.html',
							title='Big Data Visualization',
							template='about-template'
						)
   
# run the app
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 8080))
	app.run(host='0.0.0.0', port=port)



########################################################
# ROUTES AND HTML TEMPLATES SO FAR
#
#	/							home.html	
#	/mod						covid19/model.html
#	/vis/<country>			    covid19/vismodel.html
#	/about						about.html

########################################################
# Some information
#
# render_template alows to separate presentation from controller
# it will render HTML pages
# notice Flask uses Jinja2 template engine for rendering templates
# url_for() to reference static resources. 
# For example, to refer to /static/js/main.js, 
# you can use url_for('static', filename='js/main.js')
# request is to hold requests from a client e.g request.headers.get('')
# URLs to be handled by the app route handler
