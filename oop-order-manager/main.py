from dataclasses import dataclass

@dataclass
class Prodotto:
    nome: str
    prezzo: float
    disponibile: bool

    def __lt__(self, other) -> bool:
        return self.prezzo < other.prezzo


class ProductNotAvailableError(ValueError):
    pass
    

class Carrello:
    prodotti: list[Prodotto] = []

    @property
    def totale(self) -> float:
        return sum(prod.prezzo for prod in self.prodotti)

    def __init__(self):
        self.prodotti = []

    def __len__(self) -> int:
        return len(self.prodotti)
    
    def __contains__(self, other):
        return other in self.prodotti
    
    def aggiungi(self, prod: Prodotto):

        if not prod.disponibile:
            raise ProductNotAvailableError("Impossibile aggiungere un prodotto non disponibile.")
        else:
            self.prodotti.append(prod)


class Ordine:
    carrello: Carrello
    confermato: bool

    def __init__(self, carrello: Carrello):
        self.confermato = False
        self.carrello = carrello

    def conferma(self):
        
        print("Grazie per aver acquistato da noi! Ecco il riepilogo dell'ordine:")

        for prod in self.carrello.prodotti:
            print(f"- {prod.nome} | {prod.prezzo} €.")

        print("---------------------------------------------------------------------------------")
        print(f"Totale: {self.carrello.totale} €.")