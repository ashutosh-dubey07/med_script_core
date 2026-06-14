import sqlite3

def setup():
    conn = sqlite3.connect("med_script.db")
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS medicines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand_name TEXT,
            salt_name TEXT,
            is_banned INTEGER DEFAULT 0
        )
    ''')
    
    conn.commit()
    conn.close()
    print("db created")

if __name__ == "__main__":
    setup()