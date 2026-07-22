import sqlite3
from rapidfuzz import process, fuzz


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


def suggest_similar_medicines(brand_name):
    try:
        with sqlite3.connect("med_script.db") as conn:
            c = conn.cursor()

            c.execute("SELECT brand_name FROM medicines")

            medicine_names = [row[0] for row in c.fetchall()]

            similar = process.extract(
                brand_name,
                medicine_names,
                scorer=fuzz.WRatio,
                limit=5
            )
            filtered = []

            for medicine, score, _ in similar:

                if score >= 70:
                    filtered.append((medicine, round(score, 2)))

            return filtered

    except Exception as e:
        print(e)