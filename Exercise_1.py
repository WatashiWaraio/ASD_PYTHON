# ------------------- GRAMÁTICA -------------------

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

# ------------------- FUNCIÓN PRIMERO -------------------

def calcular_primero(reglas):
    no_terminales = list(reglas.keys())
    primero = {}
    for nt in no_terminales:
        primero[nt] = set()

    cambio = True
    # Algoritmo para calcular PRIMERO

    while cambio:
        cambio = False

        for nt in reglas:
            for produccion in reglas[nt]:
                for simbolo in produccion:

                    # Si es terminal o ε
                    if simbolo not in no_terminales:
                        if simbolo not in primero[nt]:
                            primero[nt].add(simbolo)
                            cambio = True
                        break  # no seguimos, ya encontramos un símbolo válido

                    else:
                        # Es no terminal: agregamos PRIMERO(simbolo) sin ε
                        antes = len(primero[nt])
                        primero[nt].update(primero[simbolo] - {"ε"})
                        despues = len(primero[nt])
                        if despues > antes:
                            cambio = True

                        # Si no tiene ε, ya no seguimos con los siguientes símbolos
                        if "ε" not in primero[simbolo]:
                            break

                else:
                    # Si todos los símbolos pudieron derivar en ε, agregamos ε
                    if "ε" not in primero[nt]:
                        primero[nt].add("ε")
                        cambio = True
    return primero

# ------------------- FUNCIÓN SIGUIENTE -------------------

def calcular_siguiente(reglas, primero, simbolo_inicial):
    no_terminales = list(reglas.keys())
    siguiente = {}
    for nt in no_terminales:
        siguiente[nt] = set()
    siguiente[simbolo_inicial].add("$")  # símbolo inicial lleva $

    cambio = True
    while cambio:
        cambio = False

        for nt in reglas:
            for produccion in reglas[nt]:
                for i in range(len(produccion)):
                    simbolo = produccion[i]

                    if simbolo in no_terminales:
                        # Hay un símbolo después
                        if i + 1 < len(produccion):
                            siguiente_simbolo = produccion[i + 1]

                            # Caso 1: el siguiente es terminal
                            if siguiente_simbolo not in reglas:
                                if siguiente_simbolo not in siguiente[simbolo]:
                                    siguiente[simbolo].add(siguiente_simbolo)
                                    cambio = True

                            # Caso 2: el siguiente es no terminal
                            else:
                                for item in primero[siguiente_simbolo]:
                                    if item != "ε" and item not in siguiente[simbolo]:
                                        siguiente[simbolo].add(item)
                                        cambio = True

                                if "ε" in primero[siguiente_simbolo]:
                                    for item in siguiente[nt]:
                                        if item not in siguiente[simbolo]:
                                            siguiente[simbolo].add(item)
                                            cambio = True
                        else:
                            # No hay símbolo después
                            for item in siguiente[nt]:
                                if item not in siguiente[simbolo]:
                                    siguiente[simbolo].add(item)
                                    cambio = True

    return siguiente

# ------------------- FUNCIÓN DE PREDICCION -------------------

def calcular_prediccion(reglas, primero, siguiente):
    prediccion = {}

    for nt in reglas:
        for produccion in reglas[nt]:
            clave = (nt, tuple(produccion))
            
            if produccion == ["ε"]:
                prediccion[clave] = siguiente[nt]
                continue

            prediccion[clave] = set()
            primero_alpha = set()
            contiene_epsilon = True

            for simbolo in produccion:
                if simbolo not in reglas:  # es terminal
                    primero_alpha.add(simbolo)
                    contiene_epsilon = False
                    break
                else:
                    primero_alpha.update(primero[simbolo] - {"ε"})
                    if "ε" not in primero[simbolo]:
                        contiene_epsilon = False
                        break

            # Si toda la producción puede derivar en ε
            if contiene_epsilon:
                primero_alpha.update(siguiente[nt])  # usar SIGUIENTE del no terminal
                primero_alpha.discard("ε")  # asegurar que 'ε' no se quede

            prediccion[clave] = primero_alpha

    return prediccion


# ------------------- FUNCIÓN PARA IMPRIMIR -------------------

def imprimir_conjuntos(nombre, conjuntos):
    print(f"\nConjuntos {nombre}:")
    for nt in conjuntos:
        print(f"{nombre}({nt}) = {conjuntos[nt]}")

def imprimir_prediccion(prediccion):
    print("\nConjuntos de PREDICCIÓN:")
    for clave, conjunto in prediccion.items():
        nt, produccion = clave
        produccion_str = " ".join(produccion)
        print(f"PREDICCIÓN({nt} → {produccion_str}) = {conjunto}")


# ------------------- PRUEBA -------------------

primero = calcular_primero(reglas)
siguiente = calcular_siguiente(reglas, primero, "S")
prediccion = calcular_prediccion(reglas, primero, siguiente)

imprimir_conjuntos("PRIMERO", primero)
imprimir_conjuntos("SIGUIENTE", siguiente)
imprimir_prediccion(prediccion)

