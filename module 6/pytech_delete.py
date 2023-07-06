"""
Title: pytech_delete.py
Author: Zachary Tharp
Date: July 5, 2023
Description: Test program for deleting documents from pytech
"""

""" import statement """
from pymongo import MongoClient

# MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.n3vdaik.mongodb.net/"

# connect to the MongoDB cluster
client = MongoClient(url)

# connect to pytech database
db = client.pytech

# get the students collection
students = db.students

# find all students in the collection
student_list = students.find({})

# display message
print("\n -- DISPLAY STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over collection and display results
for doc in student_list:
    print("Student ID:" + doc["student_id"] + "\n First Name:" + doc["first_name"] + "\n Last Name:" + doc["last_name"] + "\n")

# test document
test_doc = {
    "student_id": "1010",
    "first_name": "Fernando",
    "last_name": "Tatis"
}

# insert the test document into MongoDB atlas
test_doc_id = students.insert_one(test_doc).inserted_id

#insert statements with outputs
print("\n -- INSERT STATEMENTS --")
print("Inserted student record into the students collection with document_id " + str(test_doc_id))

# calling the find_one() method for student_id: "1010"
student_test_doc = students.find_one({"student_id": "1010"})

# display results
print ("\n -- DISPLAYING STUDENT TEST DOC --")
print("Student ID:" + student_test_doc["student_id"] + "\n First Name:" + student_test_doc["first_name"] + "\n Last Name:" + student_test_doc["last_name"] + "\n")

# calling the delete_one() method to remove student_test_doc
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

# find all students in collection
new_student_list = students.find({})

# display message
print("\n -- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --")

# loop over collection and output the results
for doc in new_student_list:
    print("Student ID:" + doc["student_id"] + "\n First Name:" + doc["first_name"] + "\n Last Name:" + doc["last_name"] + "\n")

# exit message
input("\n\n End of program, press any key to continue...")
    
