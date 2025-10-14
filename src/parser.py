import re
import pdfplumber
from abc import ABC, abstractmethod

# ==============================================================================
# Abstract Base Class - The blueprint for all our parsers
# ==============================================================================
class StatementParser(ABC):
    """
    An abstract base class that defines the structure for all bank-specific parsers.
    It handles the common task of extracting text from a PDF file.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = self._extract_text()

    def _extract_text(self):
        """Extracts all text from the PDF file using pdfplumber."""
        if not self.file_path:
            return ""
        try:
            with pdfplumber.open(self.file_path) as pdf:
                # Concatenate text from all pages, ensuring pages with no text don't cause errors
                pages_text = [p.extract_text() for p in pdf.pages if p.extract_text()]
                return "\n".join(pages_text)
        except Exception as e:
            print(f"Error reading PDF {self.file_path}: {e}")
            return "" # Return empty string on failure

    @abstractmethod
    def parse(self):
        """
        The main method that each subclass must implement.
        This method will contain the specific logic to find and extract data
        for a particular bank's statement format.
        """
        pass

# ==============================================================================
# Concrete Parser Implementations - One for each bank
# ==============================================================================
class ChaseParser(StatementParser):
    """A parser specifically for Chase credit card statements."""
    def parse(self):
        """
        Uses regular expressions (regex) to find and extract the 5 key data points.
        Each pattern is designed to find a specific piece of text in the statement.
        """
        # Regex to find an account number ending in XXXX (captures the 4 digits)
        # Looks for "Account Number:" followed by spaces, then captures 4 digits.
        card_last_4_pattern = re.compile(r'Account Number:.*?(\d{4})')
        
        # Regex to find a due date (e.g., Oct 20, 25)
        # Looks for "Payment Due Date:" followed by a date pattern.
        due_date_pattern = re.compile(r'Payment Due Date:\s*([A-Za-z]{3}\s\d{1,2},\s\d{2,4})')
        
        # Regex to find the new balance amount (e.g., $1,234.56)
        # Looks for "New Balance:" followed by a dollar amount.
        balance_pattern = re.compile(r'New Balance:\s*(\$[\d,]+\.\d{2})')
        
        # --- Search for the patterns in the extracted text ---
        card_last_4 = card_last_4_pattern.search(self.text)
        due_date = due_date_pattern.search(self.text)
        balance = balance_pattern.search(self.text)
        
        # --- Return the data in a structured dictionary ---
        # If a pattern is found (not None), we extract group(1), which is the captured part.
        # Otherwise, we return 'Not Found'.
        return {
            "issuer": "Chase",
            "card_last_4": card_last_4.group(1) if card_last_4 else "Not Found",
            "payment_due_date": due_date.group(1) if due_date else "Not Found",
            "total_balance": balance.group(1) if balance else "Not Found",
            "billing_cycle": "Not Implemented" # Placeholder for now
        }

class AmexParser(StatementParser):
    """A parser specifically for American Express statements."""
    def parse(self):
        # NOTE: These patterns are examples. You'll need to adjust them based on real Amex statements.
        card_last_4_pattern = re.compile(r'Account ending in\s+(\d{4})')
        due_date_pattern = re.compile(r'Please pay by\s+([A-Z][a-z]+\s+\d{1,2})')
        balance_pattern = re.compile(r'Amount Due\s+(\$[\d,]+\.\d{2})')

        card_last_4 = card_last_4_pattern.search(self.text)
        due_date = due_date_pattern.search(self.text)
        balance = balance_pattern.search(self.text)

        return {
            "issuer": "American Express",
            "card_last_4": card_last_4.group(1) if card_last_4 else "Not Found",
            "payment_due_date": due_date.group(1) if due_date else "Not Found",
            "total_balance": balance.group(1) if balance else "Not Found",
            "billing_cycle": "Not Implemented"
        }

class BofAParser(StatementParser):
    """A parser specifically for Bank of America statements."""
    def parse(self):
        # NOTE: These patterns are examples. You'll need to adjust them based on real BofA statements.
        card_last_4_pattern = re.compile(r'Account #:\s+\*{4} \*{4} \*{4} (\d{4})')
        due_date_pattern = re.compile(r'Payment Due Date\n([A-Z][a-z]{2}\s\d{2},\s\d{4})')
        balance_pattern = re.compile(r'New Balance\n(\$[\d,]+\.\d{2})')

        card_last_4 = card_last_4_pattern.search(self.text)
        due_date = due_date_pattern.search(self.text)
        balance = balance_pattern.search(self.text)

        return {
            "issuer": "Bank of America",
            "card_last_4": card_last_4.group(1) if card_last_4 else "Not Found",
            "payment_due_date": due_date.group(1) if due_date else "Not Found",
            "total_balance": balance.group(1) if balance else "Not Found",
            "billing_cycle": "Not Implemented"
        }

class CitiParser(StatementParser):
    """A parser specifically for Citi credit card statements."""
    def parse(self):
        # NOTE: These patterns are examples. You'll need to adjust them based on real Citi statements.
        card_last_4_pattern = re.compile(r'Account Number:.*(\d{4})')
        due_date_pattern = re.compile(r'Payment Due:\s+([A-Z][a-z]{2}\s\d{2},\s\'\d{2})')
        balance_pattern = re.compile(r'Balance Due:\s+(\$[\d,]+\.\d{2})')

        card_last_4 = card_last_4_pattern.search(self.text)
        due_date = due_date_pattern.search(self.text)
        balance = balance_pattern.search(self.text)

        return {
            "issuer": "Citi",
            "card_last_4": card_last_4.group(1) if card_last_4 else "Not Found",
            "payment_due_date": due_date.group(1) if due_date else "Not Found",
            "total_balance": balance.group(1) if balance else "Not Found",
            "billing_cycle": "Not Implemented"
        }

class CapitalOneParser(StatementParser):
    """A parser specifically for Capital One credit card statements."""
    def parse(self):
        # NOTE: These patterns are examples. You'll need to adjust them based on real Capital One statements.
        card_last_4_pattern = re.compile(r'Account\s+Ending\s+In\s+(\d{4})')
        due_date_pattern = re.compile(r'Payment\s+Due\s+by\s+([A-Za-z]+\s+\d{1,2},\s+\d{4})')
        balance_pattern = re.compile(r'New\s+Balance\s+(\$[\d,]+\.\d{2})')

        card_last_4 = card_last_4_pattern.search(self.text)
        due_date = due_date_pattern.search(self.text)
        balance = balance_pattern.search(self.text)

        return {
            "issuer": "Capital One",
            "card_last_4": card_last_4.group(1) if card_last_4 else "Not Found",
            "payment_due_date": due_date.group(1) if due_date else "Not Found",
            "total_balance": balance.group(1) if balance else "Not Found",
            "billing_cycle": "Not Implemented"
        }

# ==============================================================================
# Factory Function - The brain that chooses the right parser
# ==============================================================================
def get_parser(file_path):
    """
    Analyzes the PDF text to identify the bank and returns an instance
    of the correct parser class. This makes the main application flexible.
    """
    # Create a temporary base parser just to extract the text
    temp_parser = ChaseParser(file_path) # We can use any concrete class for text extraction
    text_content = temp_parser.text.lower() # Use lowercase for case-insensitive matching

    # Check for keywords to identify the bank
    if "chase" in text_content:
        return ChaseParser(file_path)
    if "american express" in text_content:
        return AmexParser(file_path)
    if "bank of america" in text_content:
        return BofAParser(file_path)
    if "citi" in text_content or "citibank" in text_content:
        return CitiParser(file_path)
    if "capital one" in text_content:
        return CapitalOneParser(file_path)
    else:
        # If no specific bank is identified, we can return a default or error parser
        class UnknownParser(StatementParser):
            def parse(self):
                return {"error": "Could not determine the credit card issuer from the PDF."}
        return UnknownParser(file_path)

