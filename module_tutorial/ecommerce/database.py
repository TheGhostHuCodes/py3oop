class Database():
    def __init__(self):
        print("Database has been initialized.")

database = None

def initialize_database():
    global database
    database = Database()
