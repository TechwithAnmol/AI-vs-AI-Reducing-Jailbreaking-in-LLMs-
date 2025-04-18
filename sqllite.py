import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("contact_manager.db")

# Create a cursor object
cursor = connection.cursor()

# Create Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL
);
""")

# Create Contacts table (Each contact belongs to a specific user)
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
""")

# Insert sample users
users = [
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Charlie', 'charlie@example.com'),
    ('David', 'david@example.com'),
    ('Emma', 'emma@example.com'),
    ('Frank', 'frank@example.com'),
    ('Grace', 'grace@example.com'),
    ('Hannah', 'hannah@example.com')
]

cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)

# Insert sample contacts for users
contacts = [
    (1, 'John Doe', '123-456-7890', 'johndoe@example.com'),
    (1, 'Jane Smith', '987-654-3210', 'janesmith@example.com'),
    (1, 'Samuel Adams', '555-123-4567', 'samueladams@example.com'),
    
    (2, 'Mike Johnson', '555-666-7777', 'mikejohnson@example.com'),
    (2, 'Sarah Lee', '444-333-2222', 'sarahlee@example.com'),

    (3, 'Peter Parker', '999-888-7777', 'spidey@example.com'),
    (3, 'Mary Jane', '888-777-6666', 'mj@example.com'),
    (3, 'Harry Osborn', '777-666-5555', 'harryosborn@example.com'),

    (4, 'Clark Kent', '111-222-3333', 'clarkkent@example.com'),
    (4, 'Lois Lane', '222-333-4444', 'loislane@example.com'),

    (5, 'Bruce Wayne', '123-321-4567', 'brucewayne@example.com'),
    (5, 'Alfred Pennyworth', '321-456-7890', 'alfred@example.com'),
    
    (6, 'Tony Stark', '555-987-6543', 'tonystark@example.com'),
    (6, 'Pepper Potts', '666-999-8888', 'pepper@example.com'),

    (7, 'Steve Rogers', '123-987-6543', 'cap@example.com'),
    (7, 'Bucky Barnes', '789-654-3210', 'bucky@example.com'),

    (8, 'Natasha Romanoff', '654-321-9876', 'blackwidow@example.com'),
    (8, 'Clint Barton', '222-111-9999', 'hawkeye@example.com')
]

cursor.executemany("INSERT INTO contacts (user_id, name, phone, email) VALUES (?, ?, ?, ?)", contacts)

# Function to get contacts for a specific user
def get_contacts_by_user(user_id):
    cursor.execute("SELECT * FROM contacts WHERE user_id = ?", (user_id,))
    return cursor.fetchall()

# Display all users
print("Users:")
cursor.execute("SELECT * FROM users")
for user in cursor.fetchall():
    print(user)

# Display contacts for a specific user (e.g., user_id = 1)
print("\nContacts for User ID 1:")
for contact in get_contacts_by_user(1):
    print(contact)

# Commit changes and close the connection
connection.commit()
connection.close()
