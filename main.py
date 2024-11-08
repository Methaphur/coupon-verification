import csv
import os

DATABASE_FILE = "verification_data.csv"

def load_database():
    data = set()
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, mode="r") as file:
            reader = csv.reader(file)
            data = {row[0] for row in reader}
    return data

def save_entry(number):
    with open(DATABASE_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([number])

def verify_entry(number, database):
    if number in database:
        print("This number has already been scanned.")
    else:
        save_entry(number)
        database.add(number)
        print("New entry added to the system.")

database = load_database()
print("Verification system is now running. Type 'exit' to stop.")

while True:
    user_input = input("Enter a 7-digit integer value: ")

    if user_input.lower() == "exit":
        print("Exiting the verification system.")
        break

    try:
        number = int(user_input)
        
        if 1000000 <= number <= 9999999:
            verify_entry(str(number), database)
        else:
            print("Please enter a valid roll number.")
    except ValueError:
        print("Invalid input. Please enter a numeric 7-digit integer.")
