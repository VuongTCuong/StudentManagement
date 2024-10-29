import sqlite3

def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('student_management.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS attendance (
                student_id TEXT,
                student_name TEXT,
                class_name TEXT,
                subject_name TEXT,
                total_sessions INTEGER,
                absences INTEGER,
                absence_dates TEXT
            )
        ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("Database and users table created successfully.")

def add_user(username, password):
    # Connect to the database
    conn = sqlite3.connect('student_management.db')
    cursor = conn.cursor()

    # Insert a new user
    try:
        cursor.execute('''
            INSERT INTO users (username, password) VALUES (?, ?)
        ''', (username, password))
        conn.commit()
        print(f"User '{username}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"User '{username}' already exists.")

    # Close the connection
    conn.close()

def add_attendance():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('student_management.db')
    cursor = conn.cursor()
     # Sample data to insert
    sample_data = [
        ("S001", "John Doe", "Class A", "Math", 20, 4, "2024-01-15,2024-02-05,2024-02-10,2024-02-20"),
        ("S002", "Jane Smith", "Class A", "Math", 20, 2, "2024-01-10,2024-02-15"),
        ("S003", "Michael Johnson", "Class B", "Science", 22, 5, "2024-01-12,2024-01-25,2024-02-01,2024-02-08,2024-02-19"),
        ("S004", "Emily Davis", "Class C", "History", 18, 1, "2024-01-20"),
        ("S005", "William Brown", "Class A", "Math", 20, 3, "2024-01-18,2024-02-12,2024-02-20"),
        ("S006", "Elizabeth Wilson", "Class B", "Science", 22, 0, ""),
        ("S007", "James Taylor", "Class C", "History", 18, 6, "2024-01-05,2024-01-10,2024-01-15,2024-02-03,2024-02-14,2024-02-20"),
    ]
    
    # Insert sample data into the attendance table
    cursor.executemany('''
        INSERT INTO attendance (student_id, student_name, class_name, subject_name, total_sessions, absences, absence_dates)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', sample_data)
    conn.commit()
    conn.close()
    print("Attendance added successfully.")


# Run this to create the database and table
create_database()
#add_attendance()


