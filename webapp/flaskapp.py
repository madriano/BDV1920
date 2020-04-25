from flask import Flask, request, render_template, jsonify
import json
import os
import logging

# importing own spark code 
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
logger.info(" Raw data filename will be: " + datasource)

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
	logger.info(" ROUTE: /mod => Create model.")
	global model, spark, datasource
	model = Model(spark, datasource)
	return render_template('model.html',
							title='Big Data Visualization',
							template='model-template'
						)

@app.route('/sim', methods=['GET', 'POST'])
def simulation():
	logger.info(" ROUTE: /sim => Create simulation.")
	# create simulation
	return render_template('simulation.html',
							title='Big Data Visualization',
							template='simulation-template'
						)

@app.route('/vismod/<country>', methods=['GET'])
def vismodel(country):
    # provide a snapshot of the model 
	# ex: by filtering one country if given
	logger.info(" ROUTE: /vismod => Visualize the model.")
	global model
	listing = {}
	if model is not None:
		if country == 'all':
			listing = model.all(spark)
		else:
			listing = model.filtering_by_country(spark, country)


		#listing = model.filtering_by_country(spark, "Portugal")
	return render_template('vismodel.html', 
							title='Big Data Visualization',
							data=listing,
							template='vismodel-template'
						)

@app.route('/vissim', methods=['GET'])
def vissimulation():
    # provide a snapshot of the simulation
	logger.info(" ROUTE: /vissim => Visualize the simulation.")
	return render_template('vissimulation.html',
							title='Big Data Visualization',
							template='vissimulation-template'
						)

@app.route('/about', methods=['GET'])
def about():
    # about ... kind of checking if app/routes are working
	logger.info(" ROUTE: /about => About.")
	return render_template('about.html',
							title='Big Data Visualization',
							template='about-template'
						)
   
# run the app
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 8080))
	app.run(host='0.0.0.0', port=port)



########################################################
# ROUTES and HTML TEMPLATES SO FAR
#
#	/							home.html	
#	/mod						model.html
#	/sim						simulation.html
#	/vismod/<country>			vismodel.html
#	/vissim						vissimulation.html
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
