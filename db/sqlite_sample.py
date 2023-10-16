#       TAKEN FROM: CIS 226, Fall 2023
#       This is an example of a sqlite command line program
# -------------------------------------------------------------------------------------------------

import sqlite3


def create_tables(conn, c):
    c.execute("CREATE TABLE IF NOT EXISTS fruit (name text, quantity integer)")

    c.execute("INSERT INTO fruit VALUES ('Apple', 0), ('Orange', 0)")
    conn.commit()  # Save work so far


def print_fruit(conn, c):
    print(" -- Current fruit in db --")
    for row in c.execute("SELECT * FROM fruit"):
        name = row[0]  # First column
        quantity = row[1]  # Second column
        print('{}: {}'.format(name, quantity))
    print(' --')


def get_fruit(conn, c, fruit):
    c.execute("SELECT name, quantity FROM fruit WHERE name=?", [fruit])
    row = c.fetchone()  # Get first row from result
    return row


def lookup_fruit(conn, c):
    fruit = input("Please enter the fruit you would like to lookup: ")
    found = get_fruit(conn, c, fruit)
    if found:
        name, quantity = found
        print('{}: {}'.format(name, quantity))
    else:
        print("Unable to find {}".format(fruit))


def add_update_fruit(conn, c):
    fruit = input("Please enter the fruit you would like to add/update: ")
    quantity = input("What is the quantity? ")
    # TODO: you should catch ValueError and reprompt if they give an invalid number
    quantity = int(quantity.strip() or '0')  # Default to 0

    found = get_fruit(conn, c, fruit)
    if found:
        # Do an UPDATE
        c.execute("UPDATE fruit SET quantity=? WHERE name=?",
                  [quantity, fruit])
    else:
        # Do an INSERT
        # notice arguments are reversed!
        c.execute("INSERT INTO fruit VALUES (?, ?)", [fruit, quantity])

    conn.commit()  # Save work so far
    print("{} has been added with quantity={}".format(fruit, quantity))


def remove_fruit(conn, c):
    fruit = input("Please enter the fruit you would like to remove: ")

    found = get_fruit(conn, c, fruit)
    if found:
        c.execute("DELETE FROM fruit WHERE name=?", [fruit])
        conn.commit()  # Save work so far
        print("{} has been removed".format(fruit))
    else:
        print("Unable to find {}".format(fruit))


def menu(conn, c):
    running = True
    while running:
        print("    1) Show all fruit")
        print("    2) Lookup fruit")
        print("    3) Add/Update fruit")
        print("    4) Remove fruit")
        print("    0) Quit")
        response = input("\n> ")
        if response == '1':
            print_fruit(conn, c)
        elif response == '2':
            lookup_fruit(conn, c)
        elif response == '3':
            add_update_fruit(conn, c)
        elif response == '4':
            remove_fruit(conn, c)
        elif response.lower() in ['0', 'quit', 'exit']:
            print("Goodbye")
            running = False

        if running:
            # Wait for user to press Enter before showing menu again
            input("Press Enter to see Menu")


def main():
    with sqlite3.connect(':memory:') as conn:
        c = conn.cursor()
        create_tables(conn, c)
        menu(conn, c)


main()
