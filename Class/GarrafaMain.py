import sys

from Garrafas import Garrafa

garrafaUna = Garrafa(5, 3)
garrafaDos = Garrafa(3, 3)
historicoGarrafa = []

def llenarGar(garrafaSelect, valorOld):
    if valorOld < garrafaSelect.getVMax():
        garrafaSelect.llenar()
    return garrafaSelect

def checkHis(listaGarrafaActual,garrafaSelect,valorOld):
    checkValue = [listaGarrafaActual[0].getVNow(), listaGarrafaActual[1].getVNow()]
    if checkValue not in historicoGarrafa:
        juegoGarrafa(listaGarrafaActual)
    else:
        garrafaSelect.setVNow(valorOld)
    return garrafaSelect

def vaciar(garrafaSelect, valorOld):
    if (valorOld > 0):
        garrafaSelect.vaciar()
    return garrafaSelect

def transpasar(garrafaUno, garrafaDos, valorOldUno, valorOldDos):
    if (garrafaUno.getVNow() != garrafaUno.getVMax() & garrafaDos.getVNow() > 0):
        res = valorOldUno + valorOldDos
        if res >= garrafaUno.getVMax():
            if valorOldDos > valorOldUno:
                garrafaUno.llenar()
                garrafaDos.setVNow(res - garrafaUno.getVMax())
            elif (valorOldDos == valorOldUno):
                garrafaUno.llenar()
                garrafaDos.setVNow(res - garrafaUno.getVMax())
            else:
                garrafaUno.llenar()
                garrafaDos.setVNow(valorOldUno - valorOldDos)
        else:
            garrafaUno.setVNow(res)
            garrafaDos.setVNow(0)

    return [garrafaUno, garrafaDos]

def juegoGarrafa(listaGarrafaActual):
    e0 = listaGarrafaActual[0].vNow
    e1 = listaGarrafaActual[1].vNow
    historicoGarrafa.append([e0, e1])

    if (e0 + e1) == 7:
        print(f"Solución:\n{historicoGarrafa}")
    else:
        # Llenar
        listaGarrafaActual[0] = llenarGar(listaGarrafaActual[0], e0)
        listaGarrafaActual[0] = checkHis(listaGarrafaActual, listaGarrafaActual[0], e0)
        listaGarrafaActual[1] = llenarGar(listaGarrafaActual[1], e1)
        listaGarrafaActual[1] = checkHis(listaGarrafaActual, listaGarrafaActual[1], e1)
        # Vaciar
        vaciar(listaGarrafaActual[0], e0)
        listaGarrafaActual[0] = checkHis(listaGarrafaActual, listaGarrafaActual[0], e0)
        vaciar(listaGarrafaActual[1], e1)
        listaGarrafaActual[1] = checkHis(listaGarrafaActual, listaGarrafaActual[1], e1)

        #Transpasar
        valorTrans = transpasar(listaGarrafaActual[0], listaGarrafaActual[1], e0, e1)
        listaGarrafaActual = [valorTrans[0], valorTrans[1]]
        listaGarrafaActual[0] = checkHis(listaGarrafaActual, listaGarrafaActual[0], e0)
        valorTrans = transpasar(listaGarrafaActual[1], listaGarrafaActual[0], e1, e0)
        listaGarrafaActual = [valorTrans[1], valorTrans[0]]
        listaGarrafaActual[1] = checkHis(listaGarrafaActual, listaGarrafaActual[1], e1)

juegoGarrafa([garrafaUna, garrafaDos])
