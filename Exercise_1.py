from common import imprimir_conjuntos, imprimir_prediccion, calcular_primero, calcular_siguiente, calcular_prediccion

reglas = {
    "S": [
            ['A', 'uno' , 'B', 'C'],
            ['S', 'dos']
        ],
    "A": [
            ["B", "C", "D"],
            ["A", "tres"],
            ["ε"]
        ],
    "B": [
            ["D", "cuatro", "C", "tres"],
            ["ε"]
        ],
    "C": [
            ["cinco", "D", "B"],
            ["ε"]
        ],
    "D": [
            ["seis"],
            ["ε"]
        ]
}

primero = calcular_primero(reglas)
siguiente = calcular_siguiente(reglas, primero, "S")
prediccion = calcular_prediccion(reglas, primero, siguiente)

imprimir_conjuntos("PRIMERO", primero)
imprimir_conjuntos("SIGUIENTE", siguiente)
imprimir_prediccion(prediccion)
