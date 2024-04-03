from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['Bank']
budgetManagment = db['budgetManagment']
users = db['User']





