import sqlite3

def create_database():
    conn = sqlite3.connect("auraassist.db")
    cursor = conn.cursor()


    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id INTEGER NOT NULL,  -- Added assessment_id column
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            answer TEXT NOT NULL,
            subject TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()



    cursor.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id INTEGER NOT NULL,
            user_id TEXT NOT NULL,
            response1 TEXT,
            response2 TEXT,
            response3 TEXT,
            response4 TEXT,
            response5 TEXT,
            response6 TEXT,
            response7 TEXT,
            response8 TEXT,
            response9 TEXT,
            response10 TEXT,
            response11 TEXT,
            response12 TEXT,
            response13 TEXT,
            response14 TEXT,
            response15 TEXT,
            response16 TEXT,
            response17 TEXT,
            response18 TEXT,
            response19 TEXT,
            response20 TEXT,
            response21 TEXT,
            response22 TEXT,
            response23 TEXT,
            response24 TEXT,
            response25 TEXT,
            response26 TEXT,
            response27 TEXT,
            response28 TEXT,
            response29 TEXT,
            response30 TEXT
        )
    ''')
    conn.commit()
    conn.close()



    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            mobile TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            gender TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assessments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id TEXT UNIQUE NOT NULL,
            candidate_images_folder TEXT NOT NULL,
            instructions_pdf TEXT NOT NULL
        )
    """)



if __name__ == "__main__":
    create_database()
    print("Database and table created successfully.")
