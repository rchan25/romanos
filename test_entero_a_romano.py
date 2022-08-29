'''
Casos de prueba
a) 1994 -> MCMXCIV
b) 4000 -> ValueError ("El valor es mayor de 3999) Despues pasó a RomanNumberError
c) "unacadena" -> TypeError ("Debe ser un entero")
d) 0 -> RomanNumberError ("El valor debe ser mayor a cero")
e) -3 -> RomanNumberError ("El valor debe ser mayor a cero")
f) 4.5 -> RomanNumberError ("El valor debe ser un entero")
'''
from first_part import entero_a_romano

def test_descomposicion_336():
    assert entero_a_romano(336) == ['0000', '300', '30', '6'] 