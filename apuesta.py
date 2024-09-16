from claseApuesta import Apuesta

a = Apuesta()

a = Apuesta()
print(a)
print(a.fichas)
a.ponerFicha(10)
print(a)
a.ponerFicha()
print(a)
a.tomarFicha(1)
print(a)
a.tomarFicha(1)
print(a)

tomar = a.tomarTodas()
print(tomar)

tiene = a.tieneFichas()
print(tiene)



a.tomarFicha(9)
print(a)
estaVacio = a.estaVacia() 
print(estaVacio)
