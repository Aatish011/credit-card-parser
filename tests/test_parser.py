import pytest
from src.parser import ChaseParser, AmexParser, BofAParser, CitiParser, CapitalOneParser, UnknownParser

# Mock text snippets that contain the data we want to extract.
# This makes our tests fast and independent of any actual PDF files.

MOCK_CHASE_TEXT = "Account Summary... Account Number: **** **** **** 1111 ... New Balance: $1,234.56 ... Payment Due Date: Nov 25, 25"
MOCK_AMEX_TEXT = "AMERICAN EXPRESS ... Account ending in: 2222 ... Total Balance $550.88 ... Payment Due Date 11/15/25"
MOCK_BOFA_TEXT = "Bank of America ... Account # **** **** **** 3333 ... New balance: $300.00 ... Please pay by 10/28/2025"
MOCK_CITI_TEXT = "Citi ThankYou ... Account Number **** **** **** 4444 ... NEW BALANCE TOTAL $789.10 ... Payment Due 11/01/25"
MOCK_CAPITALONE_TEXT = "Capital One ... Account Number: ************5555 ... Balance as of Oct 5, 2025 $450.00 ... Payment Due November 5, 2025"
MOCK_UNKNOWN_TEXT = "This is some random text from a bank we don't support."

def test_chase_parser_extraction():
    """Tests that the ChaseParser correctly extracts all data points."""
    parser = ChaseParser("") # The filepath doesn't matter for mock text
    data = parser.parse(text=MOCK_CHASE_TEXT)
    assert data['issuer'] == 'Chase'
    assert data['card_last_4'] == '1111'
    assert data['payment_due_date'] == 'Nov 25, 25'
    assert data['total_balance'] == '$1,234.56'

def test_amex_parser_extraction():
    """Tests that the AmexParser correctly extracts all data points."""
    parser = AmexParser("")
    data = parser.parse(text=MOCK_AMEX_TEXT)
    assert data['issuer'] == 'American Express'
    assert data['card_last_4'] == '2222'
    assert data['payment_due_date'] == '11/15/25'
    assert data['total_balance'] == '$550.88'

def test_bofa_parser_extraction():
    """Tests that the BofAParser correctly extracts all data points."""
    parser = BofAParser("")
    data = parser.parse(text=MOCK_BOFA_TEXT)
    assert data['issuer'] == 'Bank of America'
    assert data['card_last_4'] == '3333'
    assert data['payment_due_date'] == '10/28/2025'
    assert data['total_balance'] == '$300.00'

def test_citi_parser_extraction():
    """Tests that the CitiParser correctly extracts all data points."""
    parser = CitiParser("")
    data = parser.parse(text=MOCK_CITI_TEXT)
    assert data['issuer'] == 'Citi'
    assert data['card_last_4'] == '4444'
    assert data['payment_due_date'] == '11/01/25'
    assert data['total_balance'] == '$789.10'

def test_capitalone_parser_extraction():
    """Tests that the CapitalOneParser correctly extracts all data points."""
    parser = CapitalOneParser("")
    data = parser.parse(text=MOCK_CAPITALONE_TEXT)
    assert data['issuer'] == 'Capital One'
    assert data['card_last_4'] == '5555'
    assert data['payment_due_date'] == 'November 5, 2025'
    assert data['total_balance'] == '$450.00'

def test_unknown_parser_handling():
    """Tests that the UnknownParser returns a clear error message."""
    parser = UnknownParser("")
    data = parser.parse(text=MOCK_UNKNOWN_TEXT)
    assert "Could not identify the credit card issuer" in data['error']

 
