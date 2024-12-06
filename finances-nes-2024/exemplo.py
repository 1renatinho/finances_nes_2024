from finances.account import Account
from finances.client import Client
from finances.investment import Investment
from finances.transaction import Transaction

from datetime import datetime 

nano = Client("Nano")
nano.add_account()
transacao = Transaction(300, 2, "Salário do Nano")
transacao = Transaction(100, 3, "Salário do Tiago")
nano.account.add_transaction(300, 2, "Salário do Nano")
nano.account.add_transaction(100, 3, "Salário do Tiago")
nano.account.get_transactions()
investimento_selic = Investment("Selic", 100, 0.001, datetime.now())