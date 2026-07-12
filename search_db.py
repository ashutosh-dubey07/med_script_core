import sqlite3


def search_medicine(brand_name):
    try:
        with sqlite3.connect("med_script.db") as conn:
            c = conn.cursor()

            c.execute(
                "SELECT * FROM medicines WHERE brand_name = ?",
                (brand_name,)
            )

            medicine = c.fetchone()

            return medicine

    except Exception as e:
        print(e)