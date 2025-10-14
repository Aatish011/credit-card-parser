Credit Card Statement Parser
Objective
This project is a Python-based PDF parser designed to extract key data points from credit card statements from multiple major issuers. It demonstrates a scalable and maintainable design pattern for adding new parsers and showcases best practices including a web interface for easy demonstration, and a structured, testable codebase.
Features
• Multi-Issuer Support: Currently supports statements from 5 major providers:
o Chase
o American Express
o Bank of America
o Citi
o Capital One
• Key Data Extraction: Extracts 5 primary data points (configurable per parser).
• Web Interface: A clean Flask web application to upload PDF statements and view the extracted data.
• Scalable Design: Uses a Factory design pattern (get_parser) to easily add support for new credit card issuers.
• Unit Tested: The core parsing logic is validated by a suite of pytest unit tests to ensure reliability and accuracy.
Setup and Installation
Follow these steps to set up the project locally.
Prerequisites
• Python 3.8+
Installation
1. Clone or download the source code.
2. Create and activate a virtual environment:
o On Windows:
o python -m venv venv
o venv\Scripts\activate
o On macOS/Linux:
o python3 -m venv venv
o source venv/bin/activate

3. Install the required dependencies:
4. pip install -r requirements.txt

How to Run
1. Ensure your virtual environment is activated.
2. Run the Flask web application:
3. python main.py

4. Open your web browser and navigate to: http://127.0.0.1:5000
5. Upload a credit card statement PDF to see the parsed results.
How to Run Tests
The project includes a suite of unit tests to verify the parsing logic.
1. Ensure your virtual environment is activated.
2. Run pytest from the project root:
3. pytest

All tests should pass, confirming the core functionality is working as expected.
 
