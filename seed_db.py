import sqlite3


def seed():
    try:
        with sqlite3.connect("med_script.db") as conn:
            c = conn.cursor()

            c.execute("DELETE FROM medicines")
            c.execute("DELETE FROM interactions")

            medicine_data = [

                (
                    "Dolo 650",
                    "Paracetamol",
                    "Fever and Pain Relief",
                    "Tablet",
                    0,
                    "Micro Labs"
                ),

                (
                    "Crocin Advance",
                    "Paracetamol",
                    "Fever and Pain Relief",
                    "Tablet",
                    0,
                    "GSK"
                ),

                (
                    "Combiflam",
                    "Ibuprofen + Paracetamol",
                    "Pain Relief",
                    "Tablet",
                    0,
                    "Sanofi"
                ),

                (
                    "Augmentin 625",
                    "Amoxicillin + Clavulanic Acid",
                    "Antibiotic",
                    "Tablet",
                    1,
                    "GSK"
                ),

                (
                    "Hiflo-AM",
                    "Amlodipine + Metoprolol",
                    "High Blood Pressure",
                    "Tablet",
                    1,
                    "Sun Pharma"
                ),

                (
                    "CORQ-10",
                    "Coenzyme Q10",
                    "Heart Health Supplement",
                    "Capsule",
                    0,
                    "Abbott"
                ),

                (
                    "Polynova",
                    "Multivitamin + Multimineral",
                    "Nutritional Supplement",
                    "Tablet",
                    0,
                    "Mankind"
                ),

                (
                    "Dolowin Plus",
                    "Aceclofenac + Paracetamol",
                    "Pain Relief",
                    "Tablet",
                    1,
                    "Pfizer"
                ),

                (
                    "Ruliz-D",
                    "Cetirizine + Domperidone",
                    "Allergy Relief",
                    "Tablet",
                    1,
                    "Cipla"
                )

            ]

            interaction_data = [

                (
                    "Ibuprofen + Paracetamol",
                    "Paracetamol",
                    "Low",
                    "Avoid unnecessary duplicate Paracetamol exposure."
                ),

                (
                    "Aceclofenac + Paracetamol",
                    "Paracetamol",
                    "Moderate",
                    "May increase total Paracetamol dose."
                ),

                (
                    "Amoxicillin + Clavulanic Acid",
                    "Coenzyme Q10",
                    "Low",
                    "No significant interaction reported."
                )

            ]

            c.executemany(
                """
                INSERT INTO medicines(
                    brand_name,
                    generic_salt,
                    uses,
                    dosage_form,
                    prescription_required,
                    manufacturer
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                medicine_data
            )

            c.executemany(
                """
                INSERT INTO interactions(
                    salt_1,
                    salt_2,
                    severity,
                    description
                )
                VALUES (?, ?, ?, ?)
                """,
                interaction_data
            )

            conn.commit()

            print("Database seeded successfully.")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    seed()