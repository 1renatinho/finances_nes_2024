from finances import Transaction, categories
from datetime import datetime

def tr():
    return Transaction(999, 1, "Teste")

def test_transaction_instance():
    tr = tr()
    assert isinstance(tr, Transaction)
    
def test_transaction_attributes():
    tr = tr()
    assert type(tr.date) is datetime
    assert type(tr.description) is str
    assert type(tr.amount) is float
    assert type(tr.category) is int
    
def test_transaction_cat():
    tr = tr()
    assert tr.category in categories.keys()
    
def test_transaction_update():
    tr = tr()
    tr.update(amount=998)
    assert tr.amount == 998
    new_date = datetime.now()
    tr.update(date=new_date)
    assert tr.date == new_date
    tr.update(category=2)
    assert tr.category == 2
    tr.description(description="Teste 2")
    assert tr.description == "Teste 2"
    
def test_transaction_representation():
    tr = tr()
    expected = "Transação: Teste R$ 999.00 (Pagamento)"
    assert str(tr) == expected