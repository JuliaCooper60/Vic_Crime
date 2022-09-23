# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import json
from sqlalchemy import create_engine
import sqlite3 as sql
import pandas as pd
postgres_uri  = os.environ.get('DATABASE_URL')


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
DB_conn = "postgresql://yumurxqtwshjnx:fd683e2aa6f171ff752079e8833a7c447db446d1f2f363444e9a7647c1488e10@ec2-18-209-78-11.compute-1.amazonaws.com:5432/d6f887ofgg2ipi"

engine = create_engine (DB_conn)

# Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# from .models import offence_division_summary, offence_2022


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/crime_summary")
def crime_summary():

    offence_division_summary_df = pd.read_sql_query('select * from offence_division_summary', con=engine)
 
    payload = {}

    for lga in offence_division_summary_df['Local Government Area'].unique().tolist():
        df = offence_division_summary_df.loc[offence_division_summary_df['Local Government Area'] == lga].groupby\
                (['Local Government Area','Year']).agg(sum).reset_index().drop('Local Government Area',axis =1).set_index('Year')
    
        dataStackedBar = {'labels': df.index.tolist(),'datasets':[]}

        colors = ['#cbd4c2ff','#dbebc0ff','#c3b299ff','#815355ff','#523249ff','#000000']
        color = 0
        for col in df.columns:
            dataStackedBar['datasets'].append({
            'label': col,
            'data': df[col].values.tolist(),
            'backgroundColor': colors[color]
                })
            color += 1
        payload[lga] = dataStackedBar


    return jsonify(payload)


@app.route("/api/crime_2022")
def crime_2022():
    offence_2022_df = pd.read_sql_query('select * from offence_2022', con=engine)

    filter_df = offence_2022_df.groupby(["Offence Division","Offence Subdivision", "Offence Subgroup"])["Incidents Recorded"].sum()
    filter_df = filter_df.reset_index()

     

    flare = {"name": "flare", "children": []}

# iterate through dataframe values
    for row in  filter_df.values:

        level0 = row[0]
        level1 = row[1]
        level2 = row[2]
        value = row[3]
    
        # create a dictionary with all the row data
        d = {'name': level0,
                'children': [{'name': level1,
                        'children': [{'name': level2,
                                      'value': value}]}]}
    # initialize key lists
        key0 = []
        key1 = []

    # iterate through first level node names
        for i in flare['children']:
            key0.append(i['name'])

            # iterate through next level node names
            key1 = []
            for _, v in i.items():
                if isinstance(v, list):
                    for x in v:
                        key1.append(x['name'])

    # add the full row of data if the root is not in key0
        if level0 not in key0:
            d = {'name': level0,
                    'children': [{'name': level1,
                                    'children': [{'name': level2,
                                                'value': value}]}]}
            flare['children'].append(d)

        elif level1 not in key1:

        # if the root exists, then append only the next level children

            d = {'name': level1,
                'children': [{'name': level2,
                                'value': value}]}

            flare['children'][key0.index(level0)]['children'].append(d)

        else:

        # if the root exists, then only append the next level children
        
            d = {'name': level2,
                'value': value}

            flare['children'][key0.index(level0)]['children'][key1.index(level1)]['children'].append(d)

    return jsonify(flare)



    # create route that renders 2022crime data .html template
@app.route("/Crime 2022")
def Crime_2022():
    return render_template("index2022.html")

if __name__ == "__main__":
    app.run()