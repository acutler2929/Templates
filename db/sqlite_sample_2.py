#       TAKEN FROM: CIS 226, Fall 2023
#       This is an example of a sqlite command line program using a class
# -------------------------------------------------------------------------------------------------

import random
import sqlite3

print("\033c")

# Fix this SELECT statement to get the vegetable with the highest quantity.
# Use an aggregate to do so.
SQL_MAX = 'SELECT MAX(quantity), NAME FROM vegetable'


class Vegetables:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()

    def setup(self):
        self.c.execute("CREATE TABLE vegetable (quantity INTEGER, name TEXT)")
        self.conn.commit()

    def show_all(self):
        for row in self.c.execute("SELECT * FROM vegetable"):
            print(row)

    def add_vegetable(self, name, quantity):
        self.c.execute("INSERT INTO vegetable VALUES (?, ?)", [quantity, name])

    def find_vegetable(self, name):
        self.c.execute("SELECT * FROM vegetable WHERE name=?", [name])
        row = self.c.fetchone()  # Get first row
        return row

    def get_max_vegetable(self):
        self.c.execute(SQL_MAX)
        row = self.c.fetchone()  # Get first row
        return row

    def close(self):
        self.conn.close()

# --- Code Checker Suffix ---

# --- Setting Up Test Data ---


random1 = random.randint(1, 99)
random2 = random.randint(1, 99)
random3 = random.randint(1, 99)

# --- Executing Test ---
print("-=-=-=-=-=-")
v = Vegetables()
v.setup()
print("Carrot:", v.find_vegetable("Carrot"))
v.add_vegetable("Carrot", random1)
print("Carrot:", v.find_vegetable("Carrot"))
v.add_vegetable("Broccoli", random2)
v.add_vegetable("Zucchini", random3)
print("All:")
v.show_all()
v.c.execute("SELECT * FROM vegetable WHERE name='Carrot'")
# assert v.c.fetchone() == v.find_vegetable("Carrot"), "Unable to get carrot!"

# veg!r breaks the program- undeclared variable
# assert {veg!r} in v.get_max_vegetable(), "Unable to get max vegetable!"
v.c.execute(SQL_MAX)
# assert {veg!r} in v.c.fetchone(), "Unable to get max vegetable with query!"
print("OK-random-number")
