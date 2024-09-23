from claseJugador import Jugador

j = Jugador()

print(j)

j.darFicha(2)
print(j)

j.sacarFicha(1)
print(j)

tieneFichas = j.tieneFicha()
print(tieneFichas)


j.sacarFicha(6)
print(j)

sinFichas = j.sinFicha()
print(sinFichas)