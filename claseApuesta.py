

class Apuesta:
    def __init__(self):
        self.fichas = 0 
    def __repr__(self):
        return f"apuesta {self.fichas} fichas"
    def ponerFicha(self, cuentas = 1):
        self.fichas = self.fichas + cuentas
    def tomarFicha(self, cuantas=1):
        if cuantas > self.fichas:
            raise ValueError(f"No hay tantas fichas(quedan{self.fichas})")
        self.fichas = self.fichas - cuantas
   
    def tomarTodas(self):
        return self.fichas
    
    def tieneFichas(self, cuantas=1):
        return self.fichas >= cuantas
    
    def estaVacia(self):
      return self.fichas == 0
       