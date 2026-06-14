import sqlite3

def read_data():
    try:
        with sqlite3.connect("med_script.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM medicines")
            
            for row in c.fetchall():
                print(row)
                
    except Exception as e:
        print(e)

if __name__ == "__main__":
    read_data()