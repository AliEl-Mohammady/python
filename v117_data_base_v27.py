# """Databases"""

# # v117 :Databases => Intro --
# # - Database Is A Place Where We Can Store Data
# # - Database Organized Into Tables (Users, Categories)
# # - Tables Has Columns (ID, Username, Password)
# # - There's Many Types Of Databases (MongoDB, MySQL, SQLite)
# # - SQL Stand For Structured Query Language
# # - SQLite => Can Run in Memory or in A Single File
# # - You Can Browse File With https://sqlitebrowser.org/
# # - Data Inside Database Has Types (Text, Integer, Date)


# # v118: Databases => SQLite => Create Database And Connect 
# # - Connect
# # - Execute
# # - Close
# import sqlite3
# # create data base and connect
# db=sqlite3.connect("ali.db")
# # create the table and fields
# db.execute("create table if not exists skills(name text,progres integer,user_id integer)")


# # v119: Databases => SQLite => Insert Data Into Database --
# # cursor => All Operation in SQL Done By Cursor Not The Connection Itself
# # - commit => Save All Changes
# cr=db.cursor()
# cr.execute("create table if not exists skill(name text,progres integer,user_id integer)")
# # cr.execute("insert into skill(name,progres,user_id) values ('ali',90,1)")
# # cr.execute("insert into skill(name,progres,user_id) values ('ahmed',90,2)")
# mytuple=('ziad',85555555555,3)
# # cr.execute("insert into skill values (?,?,?)",mytuple)
# # example
# mylist=["Ali","Ahmed"]
# cr.execute("create table if not exists user(id integer ,name text)")
# # for num ,key in enumerate(mylist):
# #     cr.execute(f"insert into user(id,name) values ({num+1},'{key}')")

# db.commit()

# # v120: Databases => SQLite => Retrieve Data From Database 
# # - fetchone => returns a single record or None if no more rows are available.
# # - fetchall => fetches all the rows of a query result. It returns all the rows
# #               as a list of tuples. An empty list is returned if there is no record to fetch.
# # - fetchmany(size) =>

# cr.execute("select * from skill order by name")
# # cr.execute("select * from skill where name='ali'")
# print(cr.fetchone())
# # print(cr.fetchall())
# print(cr.fetchmany(2))

# # v122: Databases => SQLite => Update and Delete 
# cr.execute("update user set id=7 where id =1")
# cr.execute("update user set id=8 where name ='Ali'")
# cr.execute("select * from user where id >1  ")
# cr.execute("delete from user where name ='Ali'")
# cr.execute("select * from user limit 3 offset 1")
# print(cr.fetchall())

# # close table
# db.close()


# # v123:v128 Databases => SQLite => Create Skills App Part 4 --

# # Import SQLite Module
# import sqlite3

# # Create Database And Connect
# db = sqlite3.connect("app.db")

# # Setting Up The Cursor
# cr = db.cursor()

# def commit_and_close():
#   """Commit Changes and Close Connection To Database"""
#   db.commit()  # Save (Commit) Changes
#   db.close()  # Close Database
#   print("Connection To Database Is Closed")


# # My User ID
# uid = 1

# # Input Big Message
# input_message = """
# What Do You Want To Do ?
# "s" => Show All Skills
# "a" => Add New Skill
# "d" => Delete A Skill
# "u" => Update Skill Progress
# "q" => Quit The App
# Choose Option:
# """
# # Input Option Choose
# user_input = input(input_message).strip().lower()
# # Command List
# commands_list = ["s", "a", "d", "u", "q"]

# # Define The Methods
# def show_skills():
#   cr.execute(f"select * from skills where user_id = '{uid}'")
#   results = cr.fetchall()
#   print(f"You Have {len(results)} Skills.")

#   if len(results) > 0:
#     print("Showing Skills With Progress: ")

#   for row in results:
#     print(f"Skill => {row[0]},", end=" ")
#     print(f"Progress => {row[1]}%")
#   commit_and_close()

# def add_skill():
#   sk = input("Write Skill Name: ").strip().capitalize()
#   cr.execute(f"select name from skills where name = '{sk}' and user_id = '{uid}'")
#   results = cr.fetchone()

#   if results == None:  # Theres No Skill With This Name In Database
#     prog = input("Write Skill Progress ").strip()
#     cr.execute(f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{uid}')")

#   else:  # Theres A Skill With This Name in Database
#     print("You Cannot Add It")
#   commit_and_close()

# def delete_skill():
#   sk = input("Write Skill Name: ").strip().capitalize()
#   cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")
#   commit_and_close()

# def update_skill():
#   sk = input("Write Skill Name: ").strip().capitalize()
#   prog = input("Write The New Skill Progress ").strip()
#   cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")
#   commit_and_close()

# # Check If Command Is Exists
# if user_input in commands_list:
#   # print(f"Command Found {user_input}")
#   if user_input == "s":
#     show_skills()

#   elif user_input == "a":
#     add_skill()

#   elif user_input == "d":
#     delete_skill()

#   elif user_input == "u":
#     update_skill()

#   else:
#     print("App Is Closed.")
#     commit_and_close()

# else:
#   print(f"Sorry This Command \"{user_input}\" Is Not Found")



# assignment 28
# import sqlite3,datetime 
# db=sqlite3.connect("ass.db")
# cr=db.cursor()
# cr.execute("create table  if not exists user_ids (id integer primary key,name text ,dob text ,email text,UNIQUE(name, dob,email))")
# cr.execute(f"insert into user_ids(id,name,dob,email) values (1,'Ali','7/4/200','ali@gmail.com')")
# cr.execute(f"insert into user_ids(id,name,dob,email) values (2,'Ahned','6/4/200','Ahned@gmail.com')")
# cr.execute(f"insert into user_ids(id,name,dob,email) values (3,'mahmoud','5/4/200','mahmoud@gmail.com')")
# cr.execute(f"insert into user_ids(id,name,dob,email) values (4,'mohamed','4/4/200','mohamed@gmail.com')")
# db.commit()
# db.close()

# import v128_advanced_v12

# v128_advanced_v12.say()









