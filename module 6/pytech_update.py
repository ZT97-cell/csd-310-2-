"""
Title: pytech_updates.py
Author: Zachary Tharp
Date: July 4, 2023
Description: Test program for updating a document in the pytech collection
"""

""" import statement """
from pymongo import MongoClient

# Mongo connection string
url = "mongodb+srv://admin:admin@cluster0.n3vdaik.mongodb.net/"

# connect to the Mongo cluster
client = MongoClient(url)

# connect to pytech database
db = client.pytech

# get the students collection
students = db.students

# find all students in the collection
student_list = students.find({})

# display message
print("\n -- DISPLAY STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n + First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# update student ID: 1007
result =  students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Tkachuk"}})

# find updated student document
ted = students.find_one({"student_id": "1007"})

# display message
print("\n -- DISPLAY STUDENT DOCUMENT 1007 --")

# output the updated data
print(" Student ID:" + ted["student_id"] + "\n First Name:" + ted["first_name"] + "\n Last Name:" + ted["last_name"] + "\n")

# exit message
input("\n\n End of program, press any key to continue...")

