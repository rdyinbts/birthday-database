import json
import datetime

# def search_birthday():
#     # open the json file
#     database = load_database()
#
#     # look for the name as a key in the dictionary
#     if name in database.keys():
#         # if found return the date
#         print("we found "+name+'\'s birthday, it is',database[name])
#     else:
#         # if not return an error
#         print("no birthday found for", name)
#
# def write_birthday():
#     # writing to the database
#     # input a name
#     name = val
#
#     # input a date
#     date_string  = input("please enter your birthday, format is dd/mm/yyyy")
#     date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
#
#     database = load_database()
#
#     # add to the json file
#     with open("database.json",'w') as f:
#         database[name] = date_string
#         json.dump(database,f)

#    print('thank you,'+name+'\'s birthday was added to the database.', date_string,'is a great birthday.')

# def load_database():
#     with open('database.json','r') as d:
#         database = json.load(d)
#     return database

while True:

    # ask the user
    name = input("please enter your name")

    # open the json file
    with open('database.json', 'r') as d:
        database = json.load(d)

    # search in database
    if name in database.keys():
        # if found return the date
        print("we found " + name + '\'s birthday, it is', database[name])

    else:
        print("Name is not in the database. We will add them for you.")

        date_string = input("Please enter your birthday, with format as dd/mm/yyyy")
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y")

        with open("database.json", 'w') as f:
            database[name] = date_string
            json.dump(database, f)
        print("We have just added "+name+'\'s birthday', date_string)

# json.load(f) #loads from a file previously opened
# json.loads(s) #loads from a string
# json.dump(obj, f) #write obj to file
# json.dumps(obj) #returns a string from obj