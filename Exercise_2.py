from common import imprimir_conjuntos, imprimir_prediccion, calcular_primero, calcular_siguiente, calcular_prediccion

reglas = {
    'S' : [['A','B','uno']],
    'A' : [['dos','B'],['ε']],
    'B' : [['C','D'],['tres'],['ε']],
    'C' : [['cuatro','A','B'],['cinco']],
    'D' : [['seis'],['ε']]
}

primero = calcular_primero(reglas)
siguiente = calcular_siguiente(reglas, primero, "S")
prediccion = calcular_prediccion(reglas, primero, siguiente)

imprimir_conjuntos("PRIMERO", primero)
imprimir_conjuntos("SIGUIENTE", siguiente)
imprimir_prediccion(prediccion)
