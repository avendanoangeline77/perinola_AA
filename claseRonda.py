from claseJugador import Jugador

class Ronda:
    def __init__(self):
        self.jugadores= [] 
    def __repr__(self):
        return f"{self.jugadores}"
    
    def agregarJugador(self,jugador):
        if jugador.sinFicha <= 0:
          raise ValueError("El debe tener al menos una ficha para ser agregado")
        self.jugadores.append(jugador)    
    
   