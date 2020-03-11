import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit price': 7.5, 'discount': 10}}
    return products

def test_CanFindInvoiceClass():
    invoice = Invoice()

