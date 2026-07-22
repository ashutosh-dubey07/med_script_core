import sqlite3
def check_interactions(medicines):

    try:
        with sqlite3.connect("med_script.db") as conn:
            c = conn.cursor()

            interactions = []

            for i in range(len(medicines)):
                for j in range(i + 1, len(medicines)):

                    c.execute(
                        """
                        SELECT severity, description
                        FROM interactions
                        WHERE (salt_1 = ? AND salt_2 = ?)
                           OR (salt_1 = ? AND salt_2 = ?)
                        """,
                        (
                            medicines[i],
                            medicines[j],
                            medicines[j],
                            medicines[i]
                        )
                    )

                    result = c.fetchone()

                    if result:
                        interactions.append({
                            "medicine_1": medicines[i],
                            "medicine_2": medicines[j],
                            "severity": result[0],
                            "description": result[1]
                        })

            return interactions

    except Exception as e:
        print(e)