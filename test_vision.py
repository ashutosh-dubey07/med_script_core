from vision_service import extract_medicines
from search_db import search_medicine, suggest_similar_medicines
from interaction_service import check_interactions

image_path = "sample_images/prescription.jpg"

result = extract_medicines(image_path)

print("\nDetected Medicines:\n")
print(result)

medicines = result.splitlines()

print("\nSearching Database...\n")

detected_salts = []

for medicine in medicines:

    medicine = medicine.replace("[Uncertain]", "").strip()

    if not medicine:
        continue

    data = search_medicine(medicine)

    print("--------------------------------")
    print("Detected :", medicine)

    if data:

        print("Brand Name :", data[1])
        print("Generic Salt :", data[2])
        print("Uses :", data[3])
        print("Dosage Form :", data[4])

        if data[5] == 1:
            print("Prescription Required : Yes")
        else:
            print("Prescription Required : No")

        print("Manufacturer :", data[6])

        detected_salts.append(data[2])

    else:

        print("Medicine not found in database.")

        similar = suggest_similar_medicines(medicine)

        if similar:

            print("\nSimilar Medicines:")

            for med, score in similar:
                print(f"- {med} ({score}%)")

        else:

            print("No similar medicines found.")

print("\n--------------------------------")
print("Checking Drug Interactions...")
print("--------------------------------")

interactions = check_interactions(detected_salts)

if interactions:

    for interaction in interactions:

        print()
        print("Interaction Found")
        print("Medicine 1 :", interaction["medicine_1"])
        print("Medicine 2 :", interaction["medicine_2"])
        print("Severity :", interaction["severity"])
        print("Description :", interaction["description"])

else:

    print("No drug interactions found.")