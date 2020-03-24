from flask import request, render_template
from flask import current_app as app

# render_template alows to separate presentation from controller
# it will render HTML pages
# notice Flask uses Jinja2 template engine for rendering templates

# url_for() to reference static resources. 
# For example, to refer to /static/js/main.js, 
# you can use url_for('static', filename='js/main.js')

# request is to hold requests from a client e.g request.headers.get('')

# in the dynamic routes we can use 4 Flask context global variables:
# current_app, g, request, session
# Further details can be found in the Flask documentation 

# URLs to be handled by the app route handler

import os
from .logicmodel import PandasDataModel

# dataset path
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
dataset_path = os.path.join(basedir,"data")
print(dataset_path)
datamodel = PandasDataModel(dataset_path)
print(datamodel.size)


@app.route('/', methods=['GET'])
def home():
    listing = datamodel.getListings()
    #print(listing)

    return render_template('home.html',
                            title='Big Data Visualization',
                            data=listing,
                            template='home-template'
                        )

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html',
                            title='Big Data Visualization',
                            template='about-template'
                        )

@app.route('/filtering', methods=['GET', 'POST'])
def filtering():
    countryregion = 'Portugal'
    if request.method == 'POST':
	    countryregion = request.form.get("countryregion")

    profiling = datamodel.getListingsByCountryRegion(countryregion)
   
    return render_template("home.html", 
                            title='Big Data Visualization',
                            data=profiling,
                            template='filtering-template'
                        )



