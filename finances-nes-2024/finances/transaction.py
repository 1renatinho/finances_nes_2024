from datetime import datetime

categories = {
    1: "Pagamento",
    2: "Depósito",
    3: "Transferência"
}

class Transaction:
    def __init__(self, amount: float, category: int, description: str = "") -> None:
        if category not in [1, 2, 3]:
            raise ValueError("Essa categoria não existe.")
        
        self.amount = amount
        self.category = category
        self.date = datetime.now()
        self.description = description   
    
    def update(self, amount: float | None = None, category: int | None = None, description: str | None = None) -> None:
        tr = tr()
        if amount is not None:
            tr.amount = amount
        if category is not None:
            tr.category = category
        if description is not None:
            tr.description = description
    
    def __str__(self):
        return f"Transação: {self.description} R$ {self.amount:.2f} ({categories[self.category]})"

    