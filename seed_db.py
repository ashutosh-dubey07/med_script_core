import sqlite3

def seed():
    try:
        with sqlite3.connect("med_script.db") as conn:
            c = conn.cursor()
            
            dummy_data = [
                ('Dolo 650', 'Paracetamol', 0),
                ('Corex Cough Syrup', 'Codeine', 1),
                ('Vicks Action 500', 'Paracetamol + Caffeine', 1),
                ('Combiflam', 'Ibuprofen + Paracetamol', 0)
            ]
            
            c.executemany('''
                INSERT INTO medicines (brand_name, salt_name, is_banned)
                VALUES (?, ?, ?)
            ''', dummy_data)
            
            conn.commit()
            print("data seeded")
            
    except Exception as e:
        print(e)

if __name__ == "__main__":
    seed()