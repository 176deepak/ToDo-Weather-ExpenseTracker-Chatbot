from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/expense_tracker'
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    data = request.get_json()
    expense = {
        'amount': float(data['amount']),
        'category': data['category'],
        'description': data['description'],
        'date': datetime.now()
    }
    mongo.db.expenses.insert_one(expense)
    return jsonify({'message': 'Expense added successfully'})

@app.route('/get_expenses')
def get_expenses():
    expenses = list(mongo.db.expenses.find({}, {'_id': 0}))
    return jsonify({'expenses': expenses})

if __name__ == '__main__':
    app.run(debug=True)
