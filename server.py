from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

DATABASE_FILE = "verification_data.csv"

def load_database():
    # Load data from the CSV file into a set
    data = set()
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, mode="r") as file:
            reader = csv.reader(file)
            data = {row[0] for row in reader}
    return data

def save_entry(number):
    # Append a new entry to the CSV file
    with open(DATABASE_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([number])

@app.route("/", methods=["GET", "POST"])
def index():
    database = load_database()  # Load the database each time the form is submitted

    if request.method == "POST":
        user_input = request.form.get("number")

        # Check if the input is a valid 7-digit integer
        if user_input.isdigit() and len(user_input) == 7:
            number = user_input

            # Verify entry in the database
            if number in database:
                message = "This number has already been scanned."
            else:
                save_entry(number)
                message = f"New entry {number} added to the system."
        else:
            message = "Please enter a valid 7-digit integer."

        return render_template("index.html", message=message)

    return render_template("index.html", message="")

if __name__ == "__main__":
    app.run(debug=True)
