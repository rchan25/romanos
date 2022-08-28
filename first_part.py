'''
1. Crear una funcion que pase de entero > 0 y > 4000 a romano
2. Cualquier otra entrada debe dar error

'''

class RomanNumberError(Exception):
    pass

numero_romano = (
    (1000, 'M'), (500, 'D'), (100, 'C'),(50, 'D'),(10, 'X'),(5, 'V'), (1, 'I'),
)

def entero_a_romano(numero):
    return "MCMXCIV"