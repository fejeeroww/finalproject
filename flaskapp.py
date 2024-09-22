from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['survey_db']
users = db['users']

@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        user_data = {
            'age': int(request.form['age']),
            'gender': request.form['gender'],
            'total_income': float(request.form['total_income']),
            'expenses': {
                'utilities': float(request.form.get('utilities', 0)),
                'entertainment': float(request.form.get('entertainment', 0)),
                'school_fees': float(request.form.get('school_fees', 0)),
                'shopping': float(request.form.get('shopping', 0)),
                'healthcare': float(request.form.get('healthcare', 0))
            }
        }
        users.insert_one(user_data)
        return redirect(url_for('thank_you'))
    return render_template('survey.html')

@app.route('/thank_you')
def thank_you():
    return "Thank you for participating in the survey!"

if __name__ == '__main__':
    app.run(debug=True)