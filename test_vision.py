from vision_service import extract_medicines
from search_db import search_medicine

image_path = "sample_images/prescription.jpg"

result = extract_medicines(image_path)

print("\nDetected Medicines:\n")

print(result)

medicines = result.splitlines()

print("\nSearching Database...\n")

for medicine in medicines:

    medicine = medicine.replace("[Uncertain]", "").strip()
    if not medicine :
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

else:

    print("Medicine not found in database.")
    