from finances import Account

def default_account():
    ''' Cria uma conta de exemplo
    returns:
        default_account (Account): conta de exemplo
    '''
    default_account = Account("Teste")
    return default_account

def test_account_instance():
    account = default_account()
    assert isinstance(account, Account)

def test_account_attributes():
    account = default_account()
    assert account.name == "Teste"
    assert account.balance == 0
    assert account.transactions == []

def test_account_add_transaction():
