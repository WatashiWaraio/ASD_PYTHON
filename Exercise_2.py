Reglas = {
    'S' : [['A','B','uno']],
    'A' : [['dos','B'],['ε']],
    'B' : [['C','D'],['tres'],['ε']],
    'C' : [['cuatro','A','B'],['cinco']],
    'D' : [['seis'],['ε']]   
}

no_terminales = list(Reglas.keys())

primeros = {}
siguientes = {}


for simbolo in Reglas:
    primeros[simbolo] = []


def es_terminal(x):
    return not (x in no_terminales)

def calcular_primeros(simbolo):
    if es_terminal(simbolo):
        return [simbolo]  

    resultado = []  

    for produccion in Reglas[simbolo]:
        for i in range(len(produccion)):
            simbolo_actual = produccion[i]

            if simbolo_actual == 'ε':
                if 'ε' not in resultado:
                    resultado.append('ε')
                break

            primeros_sub = calcular_primeros(simbolo_actual)

            for s in primeros_sub:
                if s != 'ε' and s not in resultado:
                    resultado.append(s)

            if 'ε' not in primeros_sub:
                break
        else:
            if 'ε' not in resultado:
                resultado.append('ε')
    
    return resultado

def calcular_siguientes(simbolo):
    




for simbolo in Reglas:
    primeros[simbolo] = calcular_primeros(simbolo)

for simbolo in primeros:
    print(f"PRIMEROS({simbolo}) = {primeros[simbolo]}")



