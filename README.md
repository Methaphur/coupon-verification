# Coupon Verification System

This project is a simple Flask web application for verifying and storing 7-digit coupon numbers. The application checks if a coupon number has already been scanned and stores new entries in a CSV file.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/Methaphur/coupon-verification.git
    cd coupon-verification
    ```

2. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

3. Run the application:
    ```
    python server.py
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Enter a 7-digit coupon number in the input field and submit the form.
3. The application will display a message indicating whether the coupon number has already been scanned or if it has been added to the system.
4. A CSV file named `verification_data.csv` will be created in the project directory to store the scanned coupon numbers.
5. To restart the verification process, delete the `verification_data.csv` file and refresh the page.# coupon-verification
