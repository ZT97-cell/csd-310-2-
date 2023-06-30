"""
Title: pytech_queries.py
Author:Zachary_Tharp
Date: 29 June 2020
Description:Test_program for Python and MongoDB
"""

"""import statements"""
from pymongo import MongoClient

#MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.n3vdaik.mongodb.net/"

#connect to the MongoDB cluster
client = MongoClient(url)

#connect pytech to database
db = client.pytech

#display the database
print(db.list_collection_names)
