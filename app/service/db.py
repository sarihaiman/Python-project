from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['Bank']
managment = db['budgetManagment']
users = db['User']






