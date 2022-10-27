#Seis opciones Llenar 5 Llenar 3 Vaciar 5 Vaciar 3 Transpasar 5 Transpasar 3

#Recursividad

#estado[0] -> 5L
#estado[1]

def garrafas(estadoActual,estadoHistorico):

    e0 = estadoActual[0]
    e1 = estadoActual[1]
    estadoHistorico.append([e0,e1])

    if (estadoActual[0]+estadoActual[1]) == 7:
        print(f"Solución:\n{estadoHistorico}")
    else:
#Llenar
        if (estadoActual[0]<5):
            estadoActual[0] = 5
            if estadoActual not in estadoHistorico:
                garrafas(estadoActual,estadoHistorico)
        estadoActual[0] = e0

        if (estadoActual[1]<3):
            estadoActual[1] = 3
            if estadoActual not in estadoHistorico:
                garrafas(estadoActual,estadoHistorico)
        estadoActual[1] = e1

#Vaciar
        if (estadoActual[0] > 0):
            estadoActual[0] = 0
            if estadoActual not in estadoHistorico:
                garrafas(estadoActual, estadoHistorico)
        estadoActual[0] = e0

        if (estadoActual[1] > 0):
            estadoActual[1] = 0
            if estadoActual not in estadoHistorico:
                garrafas(estadoActual, estadoHistorico)
        estadoActual[1] = e1

#Transpasar

        # De 3 a 5
        if (estadoActual[0] < 5 and estadoActual[1] > 0):
            res = e0 + e1
            if res >= 5:
                if e1 > e0:
                    estadoActual[0] = 5
                    estadoActual[1] = e1 - e0
                elif e1 == e0:
                    estadoActual[0] = 5
                    estadoActual[1] = res - 5
                else:
                    estadoActual[0] = 5
                    estadoActual[1] = e0 - e1
            else:
                estadoActual[1] = 0
                estadoActual[0] = res
            if estadoActual not in estadoHistorico:
                garrafas(estadoActual, estadoHistorico)
        estadoActual[0] = e0
        estadoActual[1] = e1

        # De 5 a 3
        if (estadoActual[1] < 3 and estadoActual[0] > 0):
            res = e0 + e1
            if res >= 3:
                if e1 > e0:
                    estadoActual[1] = 3
                    estadoActual[0] = e1 - e0
                elif e1 == e0:
                    estadoActual[1] = 3
                    estadoActual[0] = res - 3
                else:
                    estadoActual[1] = 3
                    estadoActual[0] = e0 - e1
            else:
                estadoActual[0] = 0
                estadoActual[1] = res
            if estadoActual not in estadoHistorico:
                garrafas(estadoActual, estadoHistorico)

        estadoActual[1] = e1
        estadoActual[0] = e0

garrafas([0,0],[])

