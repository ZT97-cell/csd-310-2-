"""
Title: "pytech_insert.py"
Author: "Zachary  Tharp"
Date: July 1 2023
Description: A program to insert documents into student collections
"""

""" import statement """
from pymongo import MongoClient

# Mongo connection string
url = "mongodb+srv://admin:admin@cluster0.n3vdaik.mongodb.net/"

# connect to Mongo cluster
client = MongoClient(url)

#connect to pytech database
db =client.pytech
""" three student documents """
#Ted Shields Profile
Ted -{
    "student_id": "1007",
    "first_name": "Ted",
    "last_name": "Shields"
}
{
    "enrollments": [
            {
                "term": "Session 3",
                "gpa": "4.0",
                "start_date": "June 5, 2023",
                "end_date": "August 8, 2023"
            }
    ]
}
# in courses
{
    "courses": [
            {
                    "course_id": "MA321",
                    "description": "College Algebra",
                    "instructor": "Prof. Presley",
                    "grade": "A+"
                },
                {
                    "course_id": "SC147",
                    "description": "Biology",
                    "instructor": "Prof. Kelly",
                    "grade": "B-"
                }
            ]
        }
    


# Achilles Barber Profile
Achilles -{
#in students
    "student_id": "1008",
    "first_name": "Achilles",
    "last_name": "Barber"
}
#in enrollments
{
    "enrollments": [
        {
            "terms": "Session 3",
            "gpa": "3.5",
            "start_date": "June 5, 2023",
            "last_name": "August 8, 2023"
        }
    ]
}
     # in courses
{
         "courses": [
                {
                     "course_id": "PS108",
                     "description": "Psychology",
                     "instructor": "Prof. Harrell",
                     "grade": "A-"
                },
                {
                    "course_id": "PS109"
                    "description": "Philosophy"
                    "instructor": "Prof. Anthony"
                    "grade": "B+"
                }
            ]
}
    

# Stacy Williams Profile
Stacy-{
    "student_id": "1009",
    "first_name": "Stacy",
    "last_name": "Williams"
    }
    # in enrollments
{
        "enrollments": [
        {
            "terms": "Session 3",
            "gpa": "3.0",
            "start_date": "June 5, 2023",
            "last_date": "August 8, 2023"
        }
        ]
    }
        # in courses
{
            "courses": [
                {
                    "course_id": "BU203",
                    "description": "Business Law",
                    "instructor": "Prof. Morgan",
                    "grade": "C+"
                },
                {
                    "course_id": "BU258",
                    "description": "Business Communications",
                    "instructor": "Prof. Erickson",
                    "grade": "A+"
                }
            ]
}
    


# get student collection
students = db.students

# insert statements with output
print("\n -- INSERT STATEMENTS --")
tim_student_id = students.insert_one(Ted).inserted_id
print(" Inserted student record Ted Shields into the students collection with document_id" + str(tim_student_id))

achilles_student_id = students.insert_one(Achilles).inserted_id
print(" Inserted student record Achilles Barber into the students collection with document_id" + str(achilles_student_id))

stacy_student_id = students.insert_one(Stacy).inserted_id
print(" Inserted student record Stacy Williams into the students collection with document_id" + str(stacy_student_id))

input("\n\n End of program, press any key to exit...")





