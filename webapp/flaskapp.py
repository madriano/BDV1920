from flask import Flask, flash
from flask import request, render_template
from flask import jsonify, request
import json
import os
import logging

from spark.spark import init_spark_session, stop_spark_session
from spark.model import Model

# sort of print
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# variables to hold information
# if needed move to a new Python module so we can use 
# them across Python modules
datasource = os.path.abspath(os.path.dirname(__file__)) + "/datasource/covid19.csv"
model = None
simulation = None

# at runtime
# __name__ is flaskapp
# __file__ is /home/bdvapp/webapp/flaskapp.py
logger.info("Raw data filename " + datasource)
# get Spark session
#try:

#except:
#app.logger.error('Unable to start Spark")
spark = init_spark_session("BDVapp")

app = Flask(__name__)

# set routes to control the app
@app.route('/', methods=['GET'])
def home():
	logger.info("ROUTE: home")
	return render_template('home.html',
							title='Big Data Visualization',
							template='home-template'
						)

@app.route('/mod', methods=['GET'])
def model():
	logger.info("ROUTE: create model and visualize it ...")
	# create model and provide snapshot
	global datasource, model
	model = Model(spark, datasource)
	listing = model.confirmed_json
	return render_template('model.html',
							title='Big Data Visualization',
							data=listing,
							template='model-template'
						)

@app.route('/sim', methods=['GET', 'POST'])
def simulation():
	logger.info("ROUTE: perform simulation ...")
	# create simulation
	return render_template('simulation.html',
							title='Big Data Visualization',
							template='simulation-template'
						)

@app.route('/vismod', methods=['GET'])
def vismodel():
	logger.info("ROUTE: visualize the model ...")
	global model
	listing = {}
	if model is not None:
		listing = model.confirmed_json
	# provide snapshot
	return render_template('vismodel.html',
							title='Big Data Visualization',
							data=listing,
							template='vismodel-template'
						)

@app.route('/vissim', methods=['GET'])
def vissimulation():
	logger.info("ROUTE: visualize the simulation ...")
	# provide snapshot
	return render_template('vissimulation.html',
							title='Big Data Visualization',
							template='vissimulation-template'
						)

@app.route('/about', methods=['GET'])
def about():
	logger.info("ROUTE: about ...")
	return render_template('about.html',
							title='Big Data Visualization',
							template='about-template'
						)
   
# run the app
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 8080))
	app.run(host='0.0.0.0', port=port)


###################################
# ROUTES and HTML TEMPLATES SO FAR
#
#	/			home.html	
#	/mod		model.html
#	/sim		simulation.html
#	/vismod		vismodel.html
#	/vissim		vissimulation.html
#	/about		about.html

###################
# Some information

# render_template alows to separate presentation from controller
# it will render HTML pages
# notice Flask uses Jinja2 template engine for rendering templates
# url_for() to reference static resources. 
# For example, to refer to /static/js/main.js, 
# you can use url_for('static', filename='js/main.js')
# request is to hold requests from a client e.g request.headers.get('')
# URLs to be handled by the app route handler
