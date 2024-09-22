## Process and Store data in a CSV file

import csv
from pymongo import MongoClient

class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses

def process_data():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['survey_db']
    collection = db['user_data']

    # Fetch data from MongoDB
    users = []
    for doc in collection.find():
        user = User(doc['age'], doc['gender'], doc['total_income'], doc['expenses'])
        users.append(user)

    # Write data to CSV
    with open('survey_record.csv', 'w', newline='') as csvfile:
        fieldnames = ['Age', 'Gender', 'Total Income', 'Utilities', 'Entertainment', 'School Fees', 'Shopping', 'Healthcare']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for user in users:
            writer.writerow({
                'Age': user.age,
                'Gender': user.gender,
                'Total Income': user.total_income,
                'Utilities': user.expenses.get('utilities', 0),
                'Entertainment': user.expenses.get('entertainment', 0),
                'School Fees': user.expenses.get('school_fees', 0),
                'Shopping': user.expenses.get('shopping', 0),
                'Healthcare': user.expenses.get('healthcare', 0)
            })

if __name__ == '__main__':
    process_data()