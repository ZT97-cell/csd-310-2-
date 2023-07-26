"""
Title: pysports_update_and_delete.py
Author: Zachary Tharp
Date: July 26, 2023
Description: Test program for updating, deleting, and inserting with the pysports database
"""

""" import statements """
import mysql.connector
from mysql.connector import errorcode


""" database configuration """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


def show_players(cursors,title):
    """ method to execute inner join on the player and the team table, 
    iterate over the dataset and output the results in the terminal window.
    """

    # inner join query
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # get the results
    players = cursor.fetchall()

    print("\n --{}--".format(title))

    # iterate the player dataset and show results
    for player in players:
        print("Player ID: {} \n First Name: {} \n Last Name: {} \n Team Name: {} \n".format(player[0], player[1], player[2], player[3]))

try:
    """ try/catch block for handling potential MySQL database errors """

    db = mysql.connector.connect(**config) # connecting to pysports database

    # get cursor object
    cursor = db.cursor()

    # insert player query
    add_player = ("INSERT INTO player (first_name, last_name, team_id"
                  "VALUES (%s, %s, %s)")
    
    # player data fields
    player_data = ("Anakin", "Sith", 1)

    # insert a new player record
    cursor.execute(add_player, player_data)

    # commit the insert to the database
    db.commit()

    # show all records in the player table
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    # update newly inserted record
    update_player = ("UPDATE player set team_id = 2, first_name = 'Luke', last_name = 'Skywalker' WHERE first_name = 'Anakin'")

    # execute update query
    cursor.execute(update_player)

    # show all records in the player tables
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    # delete query 
    delete_player = ("DELETE FROM player WHERE first_name = 'Anakin'")

    cursor.execute(delete_player)

    # show all records in player table
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n Press any key to continue")

except mysql.connector.Error as err:
    """ handle errors """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or passwords are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """
    
db.close()

    