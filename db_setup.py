import sqlite3

def setup():

    conn = sqlite3.connect("med_script.db")
    c = conn.cursor()
    # Medicines table
    c.execute("""
        CREATE TABLE IF NOT EXISTS medicines (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand_name TEXT NOT NULl,
            generic_salt TEXT NOT NULL,

            uses TEXT NOT NULL,
            dosage_form TEXT,

            prescription_required INTEGER DEFAULT 1,
            manufacturer TEXT
        )
    """)
    # Drug interaction table
    c.execute("""
        CREATE TABLE IF NOT EXISTS interactions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            salt_1 TEXT NOT NULL,

            salt_2 TEXT NOT NULL,

            severity TEXT NOT NULL,

            description TEXT NOT NULL

        )
    """)

    conn.commit()
    conn.close()

    print("Database created successfully.")


if __name__ == "__main__":
    setup()