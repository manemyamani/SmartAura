import sqlite3

def insert_assessment(assessment_id, images_folder, instructions_pdf):
    conn = sqlite3.connect("auraassist.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO assessments (assessment_id, candidate_images_folder, instructions_pdf) 
            VALUES (?, ?, ?)
        """, (assessment_id, images_folder, instructions_pdf))
        
        conn.commit()
        print(f"Assessment {assessment_id} added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Assessment ID already exists.")
    finally:
        conn.close()

insert_assessment("000001", "static/assesments/candidates/user1.jpg", "static/assesments/instructions/AURA001.pdf")
