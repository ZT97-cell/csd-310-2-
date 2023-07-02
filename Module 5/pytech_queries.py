"""
Title: "pytech_queries.py"
Author: "Zachary Tharp"
Date: "July 1, 2023"
Description: "Test program for querying student collections"
"""

""" import statements """
from pymongo import MongoClient

# Mongo connection string
url = "mongodb+srv://admin:admin@cluster0.n3vdaik.mongodb.net/"

# connection to MongoDB cluster
client = MongoClient(url)

# connection to pytech database
db = client.pytech

# get student collections
students = db.students

# find all students in collections
student_list = students.find({})

#display message
print("\n -- DISPLAY DOCUMENTS FROM find() QUERY --")

# loop over the collection and output results
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# find document by student_id
Ted = students.find_one({"student_id": "1007"})

# output the results
print("\n -- DISPLAY STUDENT DOCUMENT FROM find_one() QUERY --")
print(" Student ID:" + Ted["student_id"] + "\n First Name:" + Ted["first_name"] "\n Last Name:" + Ted["last_name"] + "\n")

#exit message
input("\n\n End of Program, press any key to continue...")


