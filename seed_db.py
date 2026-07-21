import sqlite3

def seed():
    try:
        with sqlite3.connect("med_script.db") as conn:
            c = conn.cursor()
        ## Clear existing medicine records
            c.execute("DELETE FROM medicines")

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
                    "Dolowin Plus",
                    "Aceclofenac + Paracetamol",
                    "Pain Relief",
                    "Tablet",
                    1,
                    "Pfizer"
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
            c.executemany("""

                INSERT INTO medicines(
                    brand_name,
                    generic_salt,
                    uses,
                    dosage_form,
                    prescription_required,
                    manufacturer

                )

                VALUES (?, ?, ?, ?, ?, ?)

            """,  medicine_data)
            conn.commit()

            print("Medicine database seeded successfully.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    seed()