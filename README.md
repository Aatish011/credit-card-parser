💳 Credit Card Statement Parser
 A Python application that parses PDF credit card statements, extracts key data, and displays it in a clean web interface. Built with a scalable factory design pattern and validated by a suite of unit tests.


🚀 Features
   🖥️ Simple Web Interface: A clean and easy-to-use GUI built with Flask to upload statements.

   🏦 Multi-Issuer Support: Currently supports 5 major providers: Chase, American Express, Bank of America, Citi, and Capital One.

   🔑 Key Data Extraction: Extracts 5 primary data points (configurable per parser).

   🧩 Scalable Design: Uses a Factory design pattern (get_parser) to easily add support for new credit card issuers.

   ✅ Unit Tested: The core parsing logic is validated by a suite of pytest unit tests to ensure reliability and accuracy.

🛠️ Setup and Installation
Follow these steps to set up the project locally.

Prerequisites
Python 3.8+

Installation
Clone the repository:

git clone [https://github.com/Aatish011/credit-card-parser.git](https://github.com/Aatish011/credit-card-parser.git)
cd credit-card-parser

Create and activate a virtual environment:

# On Windows
python -m venv venv
venv\Scripts\activate


Install the required dependencies:

pip install -r requirements.txt

▶️ How to Run
Ensure your virtual environment is activated.

Run the Flask web application:

python main.py

Open your web browser and navigate to: http://127.0.0.1:5000

Upload a credit card statement PDF to see the parsed results.

🧪 How to Run Tests
The project includes a suite of unit tests to verify the parsing logic.

Ensure your virtual environment is activated.

Run pytest from the root project folder:

pytest

All tests should pass, confirming the core functionality is working as expected.