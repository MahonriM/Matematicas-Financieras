from math import log10
class Anualidadesvenc:
    def renta(self):
        m = float(input("Ingrese la cantidad de monto "))
        n = float(input("Ingresa el numero de pagos "))
        pagos = input("Escriba como seran los pagos")
        i = float(input("Ingresa la tasa de interes "))
        tasa = input(" Escribe el tiempo de la tasa de interes ")
        convertible1 = input(" ¿La tasa es convertible? si o no")#EVALUAR SI ES CONVERTIBLE
        if m > 0 or n>0 or i>0:
            if convertible1 == "si"or convertible1 =="SI" or convertible1=="Si":
                convertible2 = input(" a que tiempo sera convertible  la tasa de interes")
                if (convertible2 == "semanal" or convertible2 =="semanas"):#El tiempo al cual se convertira la tasa
                    if tasa == "diarios":#Tiempo que es la tasa
                        if (pagos == "semanal" or convertible2 =="semanas"):#Evalua el tiempo en el que se encuentra el numero de pagos
                            r1 = (i / 100 / 7 + 1) ** n
                            r1 = (r1 - 1) / i / 100 / 7
                            renta = m / r1
                            print("Renta= ", renta)
                    if tasa == "quincenal":
                        if (pagos == "semanal"):
                            i = (i / 100) * 2
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "mensual"):
                        if (pagos == "semanal"):
                            i = (i / 100) * 4
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "bimestral"):
                        if (pagos == "semanal"):
                            i = (i / 100) * 8
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "trimestral"):
                        if pagos == "semanal":
                            i = (i / 100) * 12
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "semestral"):
                        if pagos == "semanal":
                            i = (i / 100) * 24
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if tasa == "anual":
                        if pagos == "semanal":
                            i = (i / 100) * 52
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                if (convertible2 == "diario"):
                    if (tasa == "semanal"):
                        if (pagos == "diario"):
                           i = (i / 100) * 7
                           r1 = ((i + 1) ** n)
                           r1 = (r1 - 1) / i
                           renta = m / r1
                           print("Renta= ", renta)

                    if (tasa == "mensual"):
                       if (pagos == "diario"):
                          i = (i / 100) * 30
                          r1 = ((i + 1) ** n)
                          r1 = (r1 - 1) / i
                          renta = m / r1
                          print("Renta= ", renta)
                    if (tasa == "bimestral"):
                       if (pagos == "diario"):
                          i = (i / 100) * 60
                          r1 = ((i + 1) ** n)
                          r1 = (r1 - 1) / i
                          renta = m / r1
                          print("Renta= ", renta)
                    if tasa == "trimestral":
                       if pagos == "diario":
                          r1 = ((i / 100 * 90 + 1) ** n)
                          r1 = (r1 - 1) / i
                          renta = m / r1
                          print("Renta= ", renta)
                    if tasa == "semestral":
                       if pagos == "diario":
                          i = (i / 100) * 180
                          r1 = ((i + 1) ** n)
                          r1 = (r1 - 1) / i
                          renta = m / r1
                          print("Renta= ", renta)
                    if tasa == "anual":
                       if pagos == "diario":
                          r1 = (((i / 100 / 360 + 1) ** n) - 1) / i
                          renta = m / r1
                          print("Renta= ", renta)
                    if tasa == "quincenal":
                       if (pagos == "diario"):
                          i = (i / 100) * 14
                          r1 = ((i + 1) ** n)
                          r1 = (r1 - 1) / i
                          renta = m / r1
                          print("Renta= ", renta)
                if convertible2 == "quincenal" or convertible2 == "quincenas":
                    if (tasa == "diarios"):
                       if (pagos == "quincenal"):
                          i = (i / 100) / 14
                          r1 = ((i + 1) ** n)
                          r1 = (r1 - 1) / i
                          renta = m / r1
                          print("Renta= ", renta)
                    if (tasa == "semanal"):
                       if (pagos == "quincenal"):
                           i = (i / 100) / 2
                           r1 = ((i + 1) ** n)
                           r1 = (r1 - 1) / i
                           renta = m / r1
                           print("Renta= ", renta)
                    if (tasa == "mensual"):
                        if (pagos == "quincenal"):
                            i = (i / 100) * 2
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "bimestral"):
                        if (pagos == "quincenal"):
                            i = (i / 100) * 4
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if tasa == "trimestral":
                        if (pagos == "quincenal"):
                            i = (i / 100) * 6
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "semestral"):
                        if (pagos == "quincenal"):
                            i = (i / 100) * 12
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "anual"):
                        if (pagos == "quincenal"):
                            i = (i / 100) / 24
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)

                if convertible2 == "mensual":
                    if (tasa == "diarios"):
                        if (pagos == "mensual"):
                            i = (i / 100) / 30
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "quincenal"):
                        if (pagos == "mensual"):
                            i = (i / 100) / 2
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "semanal"):
                        if (pagos == "mensual"):
                            i = (i / 100) / 4
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "bimestral"):
                        if (pagos == "mensual"):
                            i = (i / 100) * 2
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "trimestral"):
                        if (pagos == "mensual"):
                            i = (i / 100) * 3
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "semestral"):
                        if (pagos == "mensual"):
                            i = (i / 100) * 6
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "anual"):
                        if (pagos == "mensual"):
                            i = (i / 100) / 12
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)

                if (convertible2 == "bimestral"):
                    if (tasa == "diarios"):
                        if (pagos == "bimestral"):
                            i = (i / 100) / 60
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "quincenal"):
                        if (pagos == "bimestral"):
                            i = (i / 100) / 4
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "semanal"):
                        if (pagos == "bimestral"):
                            i = (i / 100) / 8
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "mensual"):
                        if pagos == "bimestral":
                            i = (i / 100) / 2
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "trimestral"):
                        if (pagos == "bimestral"):
                            i = (i / 100) * 1.5
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "semestral"):
                        if (pagos == "bimestral"):
                            i = (i / 100) * 3
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "anual"):
                        if (pagos == "bimestral"):
                            i = (i / 100) / 6
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                if (convertible2 == "trimestral"):
                    if (tasa == "diarios"):
                        if (pagos == "trimestral"):
                            i = (i / 100) / 90
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "quincenal"):
                        if (pagos == "trimestral"):
                            i = (i / 100) / 6
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "semanal"):
                        if (pagos == "trimestral"):
                            i = (i / 100) / 12
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "mensual"):
                        if (pagos == "trimestral"):
                            i = (i / 100) / 3
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "bimestral"):
                        if (pagos == "trimestral"):
                            i = (i / 100) / 1.5
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "semestral"):
                        if (pagos == "trimestral"):
                            i = (i / 100) * 2
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "anual"):
                        if (pagos == "trimestral"):
                            i = (i / 100) / 4
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)

                if (convertible2 == "semestral"):
                    if (tasa == "diarios"):
                        if (pagos == "semestral"):
                            i = (i / 100) / 180
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "quincenal"):
                        if (pagos == "semestral"):
                            i = (i / 100) / 12
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "semanal"):
                        if (pagos == "semestral"):
                            i = (i / 100) / 24
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "mensual"):
                        if (pagos == "semestral"):
                            i = (i / 100) / 6
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "bimestral"):
                        if (pagos == "semestral"):
                            i = (i / 100) / 3
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "trimestral"):
                        if (pagos == "semestral"):
                            i = (i / 100) / 2
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)

                if convertible2 == "anual" or convertible2 == "años":
                    if (tasa == "anual"):
                        if (pagos == "semestral"):
                            i = (i / 100) / 2
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "diarios" or tasa == "diario" or tasa == "dias"):
                        if (pagos == "anual"):
                            i = (i / 100) / 360
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "quincenal"):
                        if (pagos == "anual"):
                            i = (i / 100) / 24
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "semanal"):
                        if (pagos == "anual"):
                            i = (i / 100) / 52
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)
                    if (tasa == "trimestral"):
                        if (pagos == "anual"):
                            i = (i / 100) / 4
                            r1 = ((i + 1) ** n)
                            r1 = (r1 - 1) / i
                            renta = m / r1
                            print("Renta= ", renta)

            else:
                if (tasa == "diarios"):

                    if (pagos == "diarios"):
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "diarios"):
                    if (pagos == "semanal"):
                        n = n * 7
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "diarios"):
                    if (pagos == "quincenal"):
                        n = n * 14
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "diarios"):
                    if (pagos == "mensual"):
                        n = n * 30
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "diarios"):
                    if (pagos == "bimestral"):
                        n = n * 60
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "diarios"):
                    if (pagos == "trimestral"):
                        n = n * 90
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "diarios"):
                    if (pagos == "semestral"):
                        n = n * 180
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "diarios"):
                    if (pagos == "anual"):
                        n = n * 360
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "semanal"):
                    if (pagos == "diarios"):
                        n = n / 7
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "semanal"):
                    if (pagos == "semanal"):
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "semanal"):
                    if (pagos == "quincenal"):
                        n = n * 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "semanal"):
                    if (pagos == "mensual"):
                        n = n * 4
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "semanal"):
                    if (pagos == "bimestral"):
                        n = n * 8
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "semanal"):
                    if (pagos == "trimestral"):
                        n = n * 12
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "semanal"):
                    if (pagos == "semestral"):
                        n = n * 24
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "semanal"):
                    if (pagos == "anual"):
                        n = n * 52
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "quincenal"):
                    if (pagos == "diarios"):
                        n = n / 14
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "quincenal"):
                    if (pagos == "semanal"):
                        n = n / 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "quincenal"):
                    if (pagos == "quincenal"):
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "quincenal"):
                    if (pagos == "mensual"):
                        n = n * 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "quincenal"):
                    if (pagos == "bimestral"):
                        n = n * 4
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "quincenal"):
                    if (pagos == "trimestral"):
                        n = n * 6
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "quincenal"):
                    if (pagos == "semestral"):
                        n = n * 12
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "quincenal"):
                    if (pagos == "anual"):
                        n = n * 24
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "mensual"):
                    if (pagos == "diarios"):
                        n = n / 30
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "mensual"):
                    if (pagos == "semanal"):
                        n = n / 4
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "mensual"):
                    if (pagos == "quincenal"):
                        n = n / 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "mensual"):
                    if (pagos == "mensual"):
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "mensual"):
                    if (pagos == "bimestral"):
                        n = n * 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "mensual"):
                    if (pagos == "trimestral"):
                        n = n * 3
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "mensual"):
                    if (pagos == "semestre"):
                        n = n * 6
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "mensual"):
                    if (pagos == "anual"):
                        n = n * 12
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "bimestral"):
                    if (pagos == "diarios"):
                        n = n / 60
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "bimestral"):
                    if (pagos == "semanal"):
                        n = n / 8
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "bimestral"):
                    if (pagos == "quincenal"):
                        n = n / 4
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "bimestral"):
                    if (pagos == "mensual"):
                        n = n / 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "bimestral"):
                    if (pagos == "bimestral"):
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "bimestral"):
                    if (pagos == "trimestral"):
                        n = n * 1.5
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "bimestral"):
                    if (pagos == "semestre"):
                        n = n * 3
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "bimestral"):
                    if (pagos == "anual"):
                        n = n * 6
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "trimestral"):
                    if (pagos == "diarios"):
                        n = n / 90
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "trimestral"):
                    if (pagos == "semanal"):
                        n = n / 12
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "trimestral"):
                    if (pagos == "quincenal"):
                        n = n / 6
                        i = (i / 100) / 360
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "trimestral"):
                    if (pagos == "mensual"):
                        n = n / 3
                        print("los pagos trimestrales son " + n)
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "trimestral"):
                    if (pagos == "bimestral"):
                        n = n / 1.5
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "trimestral"):
                    if (pagos == "trimestral"):
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "trimestral"):
                    if (pagos == "semestral"):
                        n = n * 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "trimestral"):
                    if (pagos == "anual"):
                        n = n * 4
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "semestral"):
                    if (pagos == "diarios"):
                        n = n / 180
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "semestral"):
                    if (pagos == "semanal"):
                        n = n / 24
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "semestral"):
                    if (pagos == "quincenal"):
                        n = n / 12
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "semestral"):
                    if (pagos == "mensual"):
                        n = n / 6
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "semestral"):
                    if (pagos == "bimestral"):
                        n = n / 3
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "semestral"):
                    if (pagos == "trimestral"):
                        n = n / 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "semestre"):
                    if (pagos == "semestral"):
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "semestre"):
                    if (pagos == "anual"):
                        n = n * 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "anual"):
                    if (pagos == "diarios"):
                        n = n / 360
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "anual"):
                    if (pagos == "semanal"):
                        n = n / 52
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "anual"):
                    if (pagos == "quincenal"):
                        n = n / 24
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "anual"):
                    if (pagos == "mensual"):
                        n = n / 12
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "anual"):
                    if (pagos == "bimestral"):
                        n = n / 6
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "anual"):
                    if (pagos == "trimestral"):
                        n = n / 4
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "anual"):
                    if (pagos == "semestre"):
                        n = n / 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = (r1 - 1) / i
                        renta = m / r1
                        print("Renta= ", renta)
                if (tasa == "anual"):
                    if (pagos == "anual"):
                        r1 = ((i / 100 + 1) ** n)
                        r1 = (r1 - 1) / (i / 100)
                        renta = m / r1
                        print("Renta= ", renta)
    def vencidasrent(self):
        c = float(input("Ingrese la cantidad de capital "))
        n = float(input("Ingresa el numero de pagos "))
        pagos = input("Escriba como seran los pagos")
        i = float(input("Ingresa la tasa de interes "))
        tasa = input(" Escriba como sera la tasa de interes")
        convertible1 = input(" ¿La tasa es convertible?")
        if convertible1 == "si":
            convertible2 = input(" a que tiempo sera convertible  la tasa de interes")
            if convertible2 == "semanal" or convertible2=="semanas":
                if tasa == "diarios" or tasa=="dias" or tasa=="diario":
                    if pagos == "semanal"or pagos=="semanas":
                        i = (i / 100) / 7
                        r1 = (i + 1) ** -n
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if tasa == "quincenal" or tasa=="quincenas":
                    if pagos == "semanal" or convertible2=="semanas":
                        i = (i / 100) * 2
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if tasa == "mensual" or tasa=="mes":
                    if (pagos == "semanal"):
                        i = (i / 100) * 4
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "bimestral"):
                    if (pagos == "semanal"):
                        i = (i / 100) * 8
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "trimestral"):
                    if (pagos == "semanal"):
                        i = (i / 100) * 12
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "semestral"):
                    if (pagos == "semanal"):
                        i = (i / 100) * 24
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "anual"):
                    if (pagos == "semanal"):
                        i = (i / 100) * 52
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
            if (convertible2 == "diario"):
                if (tasa == "semanal"):
                    if (pagos == "diario"):
                        i = (i / 100) * 7
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "quincenal"):
                    if (pagos == "diario"):
                        i = (i / 100) * 14
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "mensual"):
                    if (pagos == "diario"):
                        i = (i / 100) * 30
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "bimestral"):
                    if (pagos == "diario"):
                        i = (i / 100) * 60
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "trimestral"):
                    if (pagos == "diario"):
                        i = (i / 100) * 90
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "semestral"):
                    if (pagos == "diario"):
                        i = (i / 100) * 180
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "anual"):
                    if (pagos == "diario"):
                        i = (i / 100) / 365
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
            if (convertible2 == "quincenal"):
                if (tasa == "diarios"):
                    if (pagos == "quincenal"):
                        i = (i / 100) / 14
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "semanal"):
                    if (pagos == "quincenal"):
                        i = (i / 100) / 2
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "mensual"):
                    if (pagos == "quincenal"):
                        i = (i / 100) * 2
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "bimestral"):
                    if (pagos == "quincenal"):
                        i = (i / 100) * 4
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "trimestral"):
                    if (pagos == "quincenal"):
                        i = (i / 100) * 6
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "semestral"):
                    if (pagos == "quincenal"):
                        i = (i / 100) * 12
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "anual"):
                    if (pagos == "quincenal"):
                        i = (i / 100) / 24
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
            if (convertible2 == "mensual"):
                if (tasa == "diarios"):
                    if (pagos == "mensual"):
                        i = (i / 100) / 30
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "quincenal"):
                    if (pagos == "mensual"):
                        i = (i / 100) / 2
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "semanal"):
                    if (pagos == "mensual"):
                        i = (i / 100) / 4
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "bimestral"):
                    if pagos == "mensual":
                        i = (i / 100) * 2
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if tasa == "trimestral":
                    if pagos == "mensual":
                        i = (i / 100) * 3
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "semestral"):
                    if pagos == "mensual":
                        i = (i / 100) * 6
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "anual"):
                    if (pagos == "mensual"):
                        i = (i / 100) / 12
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
            if (convertible2 == "bimestral"):
                if (tasa == "diarios"):
                    if (pagos == "bimestral"):
                        i = (i / 100) / 60
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "quincenal"):
                    if (pagos == "bimestral"):
                        i = (i / 100) / 4
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "semanal"):
                    if (pagos == "bimestral"):
                        i = (i / 100) / 8
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "mensual"):
                    if (pagos == "bimestral"):
                        i = (i / 100) / 2
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "trimestral"):
                    if (pagos == "bimestral"):
                        i = (i / 100) * 1.5
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "semestral"):
                    if (pagos == "bimestral"):
                        i = (i / 100) * 3
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "anual"):
                    if (pagos == "bimestral"):
                        i = (i / 100) / 6
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
            if (convertible2 == "trimestral"):
                if (tasa == "diarios"):
                    if (pagos == "trimestral"):
                        i = (i / 100) / 90
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "quincenal"):
                    if (pagos == "trimestral"):
                        i = (i / 100) / 6
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if tasa == "semananal" or tasa == "semanas":
                    if pagos == "trimestral" or pagos =="trimestre":
                        i = (i / 100) / 12
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "mensual"):
                    if (pagos == "trimestral"):
                        i = (i / 100) / 3
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "bimestral"):
                    if pagos == "trimestral":
                        i = (i / 100) / 1.5
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if tasa == "semestral":
                    if (pagos == "trimestral"):
                        i = (i / 100) * 2
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "anual"):
                    if (pagos == "trimestral"):
                        i = (i / 100) / 4
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
            if (convertible2 == "anual"):
                if (tasa == "diarios"):
                    if (pagos == "anual"):
                        i = (i / 100) / 360
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "quincenal"):
                    if (pagos == "anual"):
                        i = (i / 100) / 24
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "semanal"):
                    if (pagos == "anual"):
                        i = (i / 100) / 52
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "mensual"):
                    if (pagos == "anual"):
                        i = (i / 100) / 12
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "bimestral"):
                    if (pagos == "anual"):
                        i = (i / 100) / 6
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "trimestral"):
                    if (pagos == "anual"):
                        i = (i / 100) / 4
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "semestral"):
                    if (pagos == "anual"):
                        i = (i / 100) / 2
                        r1 = ((i + 1) ** -n)
                        r1 = (1 - r1) / i
                        renta = c / r1
                        print("R=", renta)
        else:
            if (tasa == "diarios"):
                if (pagos == "diarios"):
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "semanal"):
                    n = n * 7
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if pagos == "quincenal":
                    n = n * 14
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "mensual"):
                    n = n * 30
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "bimestral"):
                    n = n * 60
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "trimestral"):
                    n = n * 90
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "semestral"):
                    n = n * 180
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "anual"):
                    n = n * 360
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
            if (tasa == "semanal"):
                if (pagos == "diarios"):
                    n = n / 7
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "semanal"):
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "quincenal"):
                    n = n * 2
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "mensual"):
                    n = n * 4
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "bimestral"):
                    n = n * 8
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "trimestral"):
                    n = n * 12
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "semestral"):
                    n = n * 24
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "anual"):
                    n = n * 52
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
            if (tasa == "quincenal"):
                if (pagos == "diarios"):
                    n = n / 14
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "semanal"):
                    n = n / 2
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "quincenal"):
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "mensual"):
                    n = n * 2
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "bimestral"):
                    n = n * 4
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "trimestral"):
                    n = n * 6
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "semestral"):
                    n = n * 12
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "anual"):
                    n = n * 24
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
            if (tasa == "mensual"):
                if (pagos == "diarios"):
                    n = n / 30
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "semanal"):
                    n = n / 4
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "quincenal"):
                    n = n / 2
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "mensual"):
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "bimestral"):
                    n = n * 2
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "trimestral"):
                    n = n * 3
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "semestre"):
                    n = n * 6
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "anual"):
                    n = n * 12
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
            if (tasa == "trimestral"):
                if (pagos == "diarios"):
                    n = n / 90
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "semanal"):
                    n = n / 12
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "quincenal"):
                    n = n / 6
                    i = (i / 100) / 360
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "mensual"):
                    n = n / 3
                    print("los pagos trimestrales son " + n)
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "bimestral"):
                    n = n / 1.5
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "trimestral"):
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "semestral"):
                    n = n * 2
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "anual"):
                    n = n * 4
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
            if (tasa == "semestral"):
                if (pagos == "diarios"):
                    n = n / 180
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "semanal"):
                    n = n / 24
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "quincenal"):
                    n = n / 12
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "mensual"):
                    n = n / 6
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "bimestral"):
                    n = n / 3
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "trimestral"):
                    n = n / 2
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "semestral"):
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "anual"):
                    n = n * 2
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
            if (tasa == "anual"):
                if (pagos == "diarios"):
                    n = n / 360
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "semanal"):
                    n = n / 52
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "quincenal"):
                    n = n / 24
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "mensual"):
                    n = n / 12
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "bimestral"):
                    n = n / 6
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "trimestral"):
                    n = n / 4
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "semestre"):
                    n = n / 2
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
                if (pagos == "anual"):
                    i = (i / 100)
                    r1 = ((i + 1) ** -n)
                    r1 = (1 - r1) / i
                    renta = c / r1
                    print("R=", renta)
    def numeropagosvenc(self):
       try:
           m = float(input("Inserte el valor de monto"))
           renta = float(input("Inserte el valor de Renta"))
           i = float(input("Inserte la tasa de interes"))
           tasa=input("Ingresa el tiemp de la tasa")
           #convertible1 = input(" ¿La tasa es convertible? si o no")
           #if convertible1=="si":
           convertible2 = input(" a que tiempo sera convertible  la tasa de interes")
           if (convertible2 == "semanal"):
               if (tasa == "diarios" or tasa == "diario" or tasa == "dias"):
                   n = (m / renta)
                   i = (i / 100) / 7
                   n = n * (i)
                   n = n + 1
                   n = log10(n) / log10(1 + i)
                   print("numero de pagos son ", n)
               if (tasa == "anual"):
                   n = (m / renta)
                   i = (i / 100) *52
                   n = n * (i)
                   n = n + 1
                   n = log10(n) / log10(1 + i)
                   print("numero de pagos son ", n)
               elif tasa=="quincenal":
                   n = (m / renta)
                   i = (i / 100) * 2
                   n = n * (i)
                   n = n + 1
                   n = log10(n) / log10(1 + i)
                   print("numero de pagos son ", n)
               if (tasa == "mensual"):
                    n = (m / renta)
                    i = (i / 100) * 4
                    n = n * (i)
                    n = n + 1
                    n = log10(n) / log10(1 + i)
                    print("numero de pagos son ", n)
               if (tasa == "bimestral"):
                    n = (m / renta)
                    i = (i / 100) * 8
                    n = n * (i)
                    n = n + 1
                    n = log10(n) / log10(1 + i)
                    print("numero de pagos son ", n)
               if (tasa == "trimestral"):
                     n = (m / renta)
                     i = (i / 100) * 12
                     n = n * (i)
                     n = n + 1
                     n = log10(n) / log10(1 + i)
                     print("numero de pagos son ", n)
               if (tasa == "semestral"):
                    n = (m / renta)
                    i = (i / 100) * 24
                    n = n * (i)
                    n = n + 1
                    n = log10(n) / log10(1 + i)
                    print("numero de pagos son ", n)   
           if tasa=="anual":
               if convertible2=="mensual":
                   n = (m / renta)
                   i = i / 100/ 12
                   n = n * (i)
                   n = n + 1
                   n = log10(n) / log10(1 + i)
                   print("numero de pagos son ", n)
               if convertible2=="bimestral":
                    n = (m / renta)
                    i = (i / 100) /6
                    n = n * (i)
                    n = n + 1
                    n = log10(n) / log10(1 + i)
                    print("numero de pagos son ", n)
               if convertible2=="quincenal":
                    n = (m / renta)
                    i = (i / 100) /24
                    n = n * (i)
                    n = n + 1
                    n = log10(n) / log10(1 + i)
                    print("numero de pagos son ", n)
               if convertible2=="trimestral":
                    n = (m / renta)
                    i = (i / 100) /4
                    n = n * (i)
                    n = n + 1
                    n = log10(n) / log10(1 + i)
                    print("numero de pagos son ", n)
               if convertible2=="semanal":
                    n = (m / renta)
                    i = (i / 100) /52
                    n = n * (i)
                    n = n + 1
                    n = log10(n) / log10(1 + i)
                    print("numero de pagos son ", n)
               if convertible2=="diario" or convertible2=="diarios":
                    n = (m / renta)
                    i = (i / 100) /360
                    n = n * (i)
                    n = n + 1
                    n = log10(n) / log10(1 + i)
                    print("numero de pagos son ", n)
               if convertible2=="semestral":
                    n = (m / renta)
                    i = (i / 100) /2
                    n = n * (i)
                    n = n + 1
                    n = log10(n) / log10(1 + i)
                    print("numero de pagos son ", n)
               if convertible2=="anual":
                    n = (m / renta)
                    i = (i / 100)
                    n = n * (i)
                    n = n + 1
                    n = log10(n) / log10(1 + i)
                    print("numero de pagos son ", n)
           if (convertible2 == "diario"):
               if (tasa == "semanal"):
                    n = (m / renta)
                    i = (i / 100) * 7
                    n = n * (i)
                    n = n + 1
                    n = log10(n) / log10(1 + i)
                    print("numero de pagos son ", n)
               if (tasa == "quincenal"):
                   n = (m / renta)
                   i = (i / 100) * 14
                   n = n * (i)
                   n = n + 1
                   n = log10(n) / log10(1 + i)
                   print("numero de pagos son ", n)
               if (tasa == "mensual"):
                   n = (m / renta)
                   #if (pagos == "diario"):
                   i = (i / 100) * 30
                   n = n * (i)
                   n = n + 1
                   n = log10(n) / log10(1 + i)
                   print("numero de pagos son ",n)
               if (tasa == "bimestral"):
                   n=m/renta
                   i = (i / 100) * 60
                   n = n * (i)
                   n = n + 1
                   n = log10(n) / log10(1 + i)
                   print("numero de pagos son ",n)
               if (tasa == "trimestral"):
                   n=m/renta
                   i = (i / 100) * 90
                   n = n * (i)
                   n = n + 1
                   n = log10(n) / log10(1 + i)
                   print("numero de pagos son ",n)
               if (tasa == "semestral"):
                   n=m/renta
                   i = (i / 100) * 180
                   n = n * (i)
                   n = n + 1
                   n = log10(n) / log10(1 + i)
                   print("numero de pagos son ",n)
               if (tasa == "anual"):
                   n= m/renta
                   i = (i / 100) / 365
                   n = n * (i)
                   n = n + 1
                   n = log10(n) / log10(1 + i)
                   print("numero de pagos son ",n)
           if (convertible2 == "bimestral"):
               if tasa == "diarios":
                   n= m/renta
                   i = (i / 100) / 60
                   n = n * (i)
                   n = n + 1
                   n = log10(n) / log10(1 + i)
                   print("numero de pagos son ",n)
               if (tasa == "quincenal"):
                    n= m/renta
                    i = (i / 100) / 4
                    n = n * (i)
                    n = n + 1
                    n = log10(n) / log10(1 + i)
                    print("numero de pagos son ",n)
               if (tasa == "semanal"):
                   n= m/renta
                   i = (i / 100) / 8
                   n = n * (i)
                   n = n + 1
                   n = log10(n) / log10(1 + i)
                   print("numero de pagos son ",n)
               if (tasa == "mensual"):
                   n=m/renta
                   i = (i / 100) / 2
                   n = n * (i)
                   n = n + 1
                   n = log10(n) / log10(1 + i)
                   print("numero de pagos son ",n)                           
               if (tasa == "trimestral"):
                   n=m/renta
                   i = (i / 100) * 1.5
                   n = n * (i)
                   n = n + 1
                   n = log10(n) / log10(1 + i)
                   print("numero de pagos son ",n)
               if (tasa == "anual"):
                    n=m/renta
                    i = (i / 100) / 6
                    n = n * (i)
                    n = n + 1
                    n = log10(n) / log10(1 + i)
                    print("numero de pagos son ",n)







       except:
           print("Verifica los valores que ingresaste")
    def capanti(self):
        renta = float(input("Ingrese el valor de la renta"))
        n = float(input("Ingrese el plazo"))
        pagos = input("Escriba como seran los pagos")
        i = float(input("Escriba la tasa de interés"))
        tasa = input(" Escriba como sera la tasa de interes")
        convertible1 = input(" ¿La tasa es convertible? si o no")
        if (convertible1 == "si"):
            convertible2 = input(" a que tiempo sera convertible  la tasa de interes")
            if (convertible2 == "semanal"):
                if (tasa == "diarios" or tasa == "diario" or tasa == "dias"):
                    if (pagos == "semanal"):
                        i = (i / 100) / 7
                        v1 = 1 + i
                        v2 = 1 + v1
                        v3 = (v2, (-n + 1))
                        v4 = v3 / i
                        v5 = v4 + 1
                        cap = renta * v5
                        print("El valor del capital es ", cap)
                if (tasa == "quincenal"):
                    if (pagos == "semanal"):
                        i = (i / 100) * 2
                        v1 = 1 + i
                        v2 = 1 + v1
                        v3 = (v2, (-n + 1))
                        v4 = v3 / i
                        v5 = v4 + 1
                        cap = renta * v5
                        print("El valor del capital es ", cap)
                if tasa == "mensual":
                    if pagos == "semanal":
                        i = (i / 100) * 4
                        v1 = 1 + i
                        v2 = 1 + v1
                        v3 = (v2, (-n + 1))
                        v4 = v3 / i
                        v5 = v4 + 1
                        cap = renta * v5
                        print("El valor del capital es ", cap)
                if (tasa == "bimestral"):
                    if (pagos == "semanal"):
                        i = (i / 100) * 8
                        v1 = 1 + i
                        v2 = 1 + v1
                        v3 = (v2, (-n + 1))
                        v4 = v3 / i
                        v5 = v4 + 1
                        cap = renta * v5
                        print("El valor del capital es ", cap)
                if (tasa == "trimestral"):
                    if (pagos == "semanal"):
                        i = (i / 100) * 12
                        v1 = 1 + i
                        v2 = 1 + v1
                        v3 = (v2, (-n + 1))
                        v4 = v3 / i
                        v5 = v4 + 1
                        cap = renta * v5
                        print("El valor del capital es ", cap)
                if (tasa == "semestral"):
                    if (pagos == "semanal"):
                        i = (i / 100) * 24
                        v1 = 1 + i
                        v2 = 1 + v1
                        v3 = (v2, (-n + 1))
                        v4 = v3 / i
                        v5 = v4 + 1
                        cap = renta * v5
                        print("El valor del capital es ", cap)
                if (tasa == "anual"):
                    if (pagos == "semanal"):
                        i = (i / 100) * 52
                        v1 = 1 + i
                        v2 = 1 + v1
                        v3 = (v2, (-n + 1))
                        v4 = v3 / i
                        v5 = v4 + 1
                        cap = renta * v5
                        print("El valor del capital es ", cap)
            if (convertible2 == "diario"):
                if (tasa == "semanal"):
                    if (pagos == "diario"):
                        i = (i / 100) * 7
                        v1 = 1 + i
                        v2 = 1 + v1
                        v3 = (v2, (-n + 1))
                        v4 = v3 / i
                        v5 = v4 + 1
                        cap = renta * v5
                        print("El valor del capital es ", cap)
                if (tasa == "quincenal"):
                    if (pagos == "diario"):
                        i = (i / 100) * 14
                        v1 = 1 + i
                        v2 = 1 + v1
                        v3 = (v2, (-n + 1))
                        v4 = v3 / i
                        v5 = v4 + 1
                        cap = renta * v5
                        print("El valor del capital es ", cap)
                if (tasa == "mensual"):
                    if (pagos == "diario"):
                        i = (i / 100) * 30
                        v1 = 1 + i
                        v2 = 1 + v1
                        v3 = (v2, (-n + 1))
                        v4 = v3 / i
                        v5 = v4 + 1
                        cap = renta * v5
                        print("El valor del capital es ", cap)
                if (tasa == "bimestral"):
                    if pagos == "diario":
                        i = (i / 100) * 60
                        v1 = 1 + i
                        v2 = 1 + v1
                        v3 = (v2, (-n + 1))
                        v4 = v3 / i
                        v5 = v4 + 1
                        cap = renta * v5
                        print("El valor del capital es ", cap)

def capotalven(self):
        renta=float(input("Ingrese el valor de la renta"))
        n=float(input("Ingrese el plazo"))
        pagos=input("Escriba como seran los pagos")
        i=float(input("Escriba la tasa de interés"))
        tasa=input(" Escriba como sera la tasa de interes")
        convertible1 = input(" ¿La tasa es convertible? si o no")
        if (convertible1 == "si"):
            convertible2 =input(" a que tiempo sera convertible  la tasa de interes")
            if (convertible2 == "semanal"):
                if (tasa == "diarios" or tasa=="diario" or tasa == "dias"):
                    if (pagos == "semanal"):
                        i = (i / 100) / 7
                        v1 = 1 + i
                        v2 = 1 - v1
                        v3 = (v2, (-n))
                        v4 = v3 / i
                        cap = renta * v4
                        print("El valor del capital es ",cap)
                if (tasa == "quincenal"):
                    if (pagos == "semanal"):
                        i = (i / 100) * 2
                        v1 = 1 + i
                        v2 = 1 - v1
                        v3 = (v2, (-n))
                        v4 = v3 / i
                        cap = renta * v4
                        print("El valor del capital es ",cap)
                if tasa == "mensual":
                    if pagos == "semanal":
                        i = (i / 100) * 4
                        v1 = 1 + i
                        v2 = 1 - v1
                        v3 = (v2, (-n))
                        v4 = v3 / i
                        cap = renta * v4
                        print("El valor del capital es ",cap)
                if (tasa == "bimestral"):
                    if (pagos == "semanal"):
                        i = (i / 100) * 8
                        v1 = 1 + i
                        v2 = 1 - v1
                        v3 = (v2, (-n))
                        v4 = v3 / i
                        cap = renta * v4
                        print("El valor del capital es ",cap)          
                if (tasa == "trimestral"):
                    if (pagos == "semanal"):
                        i = (i / 100) * 12
                        v1 = 1 + i
                        v2 = 1 - v1
                        v3 = (v2, (-n))
                        v4 = v3 / i
                        cap = renta * v4
                        print("El valor del capital es ",cap)                             
                if (tasa == "semestral"):
                    if (pagos == "semanal"):
                        i = (i / 100) * 24
                        v1 = 1 + i
                        v2 = 1 - v1
                        v3 = (v2, (-n))
                        v4 = v3 / i
                        cap = renta * v4
                        print("El valor del capital es ",cap)                                  
                if (tasa == "anual"):
                    if (pagos == "semanal"):
                        i = (i / 100) * 52
                        v1 = 1 + i
                        v2 = 1 - v1
                        v3 = (v2, (-n))
                        v4 = v3 / i
                        cap = renta * v4
                        print("El valor del capital es ",cap)
            if (convertible2 == "diario"):
                if (tasa == "semanal"):
                    if (pagos == "diario"):
                        i = (i / 100) * 7
                        v1 = 1 + i
                        v2 = 1 - v1
                        v3 = (v2, (-n))
                        v4 = v3 / i
                        cap = renta * v4
                        print("El valor del capital es ",cap)
                if (tasa == "quincenal"):
                    if (pagos == "diario"):
                        i = (i / 100) * 14
                        v1 = 1 + i
                        v2 = 1 - v1
                        v3 = (v2, (-n))
                        v4 = v3 / i
                        cap = renta * v4
                        print("El valor del capital es ",cap)         
                if (tasa == "mensual"):
                    if (pagos== "diario"):
                        i = (i / 100) * 30
                        v1 = 1 + i
                        v2 = 1 - v1
                        v3 = (v2, (-n))
                        v4 = v3 / i
                        cap = renta * v4
                        print("El valor del capital es ",cap)
                if (tasa == "bimestral"):
                    if pagos=="diario":
                        i = (i / 100) * 60
                        v1 = 1 + i
                        v2 = 1 - v1
                        v3 = (v2, (-n))
                        v4 = v3 / i
                        cap = renta * v4
                        print("El valor del capital es ",cap)
                    
                
                                    
                        
                   

class rentaanticipada():
    def rentaanticipadamon(self):
        #p2=input("Cuenta con monto o capital")
            m=float(input("Ingrese la cantidad de monto "))
            n=float(input("Ingresa el numero de pagos "))
            pagos=input("Escriba como seran los pagos")
            i=float(input("Ingresa la tasa de interes "))
            tasa=input(" Escriba como sera la tasa de interes")
            convertible1 = input(" ¿La tasa es convertible? si o no")
            if (convertible1 == "si"):
                convertible2 =input(" a que tiempo sera convertible  la tasa de interes")
                if (convertible2 == "semanal"):
                    if (tasa == "diarios" or tasa=="diario" or tasa == "dias"):
                        if (pagos == "semanal"):
                            i = (i / 100) / 7
                            r1 = (i + 1)**n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                    if (tasa == "quincenal"):
                        if (pagos == "semanal"):
                            i = (i / 100) * 2
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                    if tasa == "mensual":
                        if pagos == "semanal":
                            i = (i / 100) * 4
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                    if (tasa == "bimestral"):
                        if (pagos == "semanal"):
                            i = (i / 100) * 8
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)           
                    if (tasa == "trimestral"):
                        if (pagos == "semanal"):
                             i = (i / 100) * 12
                             r1 = (i + 1)** n
                             r1 = ((i + 1) * ((r1 - 1) / i))
                             renta = m / r1
                             print("R=" , renta)                             
                    if (tasa == "semestral"):
                        if (pagos == "semanal"):
                            i = (i / 100) * 24
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)                                   
                    if (tasa == "anual"):
                        if (pagos == "semanal"):
                            i = (i / 100) * 52
                            r1 = (i + 1)**n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                if (convertible2 == "diario"):
                    if (tasa == "semanal"):
                        if (pagos == "diario"):
                            i = (i / 100) * 7
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                    if (tasa == "quincenal"):
                        if (pagos == "diario"):
                             i = (i / 100) * 14
                             r1 = (i + 1)** n
                             r1 = ((i + 1) * ((r1 - 1) / i))
                             renta = m / r1
                             print("R=" , renta)           
                    if (tasa == "mensual"):
                        if (pagos== "diario"):
                             i = (i / 100) * 30
                             r1 = (i + 1)** n
                             r1 = (i + 1) * ((r1 - 1) / i)
                             renta = m / r1
                             print("R=" , renta)
                    if (tasa == "bimestral"):
                        if pagos=="diario":
                             i = (i / 100) * 60
                             r1 = (i + 1)** n
                             r1 = ((i + 1) * ((r1 - 1) / i))
                             renta = m / r1
                             print("R=" , renta)
                    if (tasa == "trimestral"):
                        if (pagos == "diario"):
                             i = (i / 100) * 90
                             r1 = (i + 1)** n
                             r1 = ((i + 1) * ((r1 - 1) / i))
                             renta = m / r1
                             print("R=" , renta)           
                    if (tasa == "semestral"):
                        if pagos == "diario":
                             i = (i / 100) * 180
                             r1 = (i + 1)** n
                             r1 = ((i + 1) * ((r1 - 1) / i))
                             renta = m / r1
                             print("R=" , renta)                           
                    if (tasa == "anual"):
                        if (pagos == "diario"):
                            i = (i / 100) / 365
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                if (convertible2 == "quincenal"):
                    if (tasa == "diarios"):
                        if (pagos == "quincenal"):
                            i = (i / 100) / 14
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                    if (tasa == "semanal"):          
                        if (pagos == "quincenal"):
                             i = (i / 100) / 2
                             r1 = (i + 1)** n
                             r1 = ((i + 1) * ((r1 - 1) / i))
                             renta = m / r1
                             print("R=" , renta)
                    if (tasa == "mensual"):
                        if pagos == "quincenal": 
                            i = (i / 100) * 2
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)                      
                    if (tasa == "bimestral"):
                        if (pagos == "quincenal"):
                             i = (i / 100) * 4
                             r1 = (i + 1)** n
                             r1 = ((i + 1) * ((r1 - 1) / i))
                             renta = m / r1
                             print("R=" , renta)
                    if (tasa == "trimestral"):
                        if (pagos == "quincenal"):
                            i = (i / 100) * 6
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)                          
                    if (tasa == "semestral"):
                        if (pagos == "quincenal"):
                            i = (i / 100) * 12
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)                         
                    if (tasa == "anual"):
                        if (pagos == "quincenal"):
                            i = (i / 100) / 24
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                if (convertible2 == "mensual"):
                    if (tasa == "diarios"):
                        if (pagos == "mensual"):
                                i = (i / 100) / 30
                                r1 = (i + 1)** n
                                r1 = ((i + 1) * ((r1 - 1) / i))
                                renta = m / r1
                                print("R=" , renta)
                        if (tasa == "quincenal"):
                            if (pagos == "mensual"):
                                i = (i / 100) / 2
                                r1 = (i + 1)** n
                                r1 = ((i + 1) * ((r1 - 1) / i))
                                renta = m / r1
                                print("R=" , renta)
                        if (tasa == "semanal"):                              
                            if (pagos == "mensual"):
                                i = (i / 100) / 4
                                r1 = (i + 1)** n
                                r1 = ((i + 1) * ((r1 - 1) / i))
                                renta = m / r1
                                print("R=" , renta)
                        if (tasa == "bimestral"):
                            if (pagos == "mensual"):
                                i = (i / 100) * 2
                                r1 = (i + 1)** n
                                r1 = ((i + 1) * ((r1 - 1) / i))
                                renta = m / r1
                                print("R=" , renta)
                        if (tasa == "trimestral"):
                            if (pagos == "mensual"):
                                i = (i / 100) * 3
                                r1 = (i + 1)** n
                                r1 = ((i + 1) * ((r1 - 1) / i))
                                renta = m / r1
                                print("R=" , renta)
                        if (tasa == "semestral"):
                            if (pagos == "mensual"):
                                i = (i / 100) * 6
                                r1 = (i + 1)** n
                                r1 = ((i + 1) * ((r1 - 1) / i))
                                renta = m / r1
                                print("R=" , renta)
                        if (tasa == "anual"):                               
                            if pagos == "mensual":
                                i = (i / 100) / 12
                                r1 = (i + 1)** n
                                r1 = ((i + 1) * ((r1 - 1) / i))
                                renta = m / r1
                                print("R=" , renta)
                if (convertible2 == "bimestral"):
                    if (tasa == "diarios"):
                        if (pagos == "bimestral"):
                                i = (i / 100) / 60
                                r1 = (i + 1)** n
                                r1 = ((i + 1) * ((r1 - 1) / i))
                                renta = m / r1
                                print("R=" , renta)
                    if (tasa == "quincenal"):
                        if (pagos == "bimestral"):
                                i = (i / 100) / 4
                                r1 = (i + 1)** n
                                r1 = ((i + 1) * ((r1 - 1) / i))
                                renta = m / r1
                                print("R=" , renta)
                    if (tasa == "semanal"):
                        if (pagos == "bimestral"):
                                i = (i / 100) / 8
                                r1 = (i + 1)** n
                                r1 = ((i + 1) * ((r1 - 1) / i))
                                renta = m / r1
                                print("R=" , renta)
                    if (tasa == "mensual"):
                        if (pagos == "bimestral"):
                                i = (i / 100) / 2
                                r1 = (i + 1)** n
                                r1 = ((i + 1) * ((r1 - 1) / i))
                                renta = m / r1
                                print("R=" , renta)
                    if (tasa == "trimestral"):
                        if (pagos == "bimestral"):
                             i = (i / 100) * 1.5
                             r1 = (i + 1)** n
                             r1 = ((i + 1) * ((r1 - 1) / i))
                             renta = m / r1
                             print("R=" , renta)
                    if tasa == "semestral":
                        if (pagos == "bimestral"):
                            i = (i / 100) * 3
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                    if (tasa == "anual"):
                        if (pagos == "bimestral"):
                            i = (i / 100) / 6
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                if (convertible2 == "trimestral"):
                    if (tasa == "diarios"):
                        if (pagos == "trimestral"):
                             i = (i / 100) / 90
                             r1 = (i + 1)** n
                             r1 = ((i + 1) * ((r1 - 1) / i))
                             renta = m / r1
                             print("R=" , renta)                                   
                    if (tasa == "quincenal"):
                        if (pagos == "trimestral"):
                             i = (i / 100) / 6
                             r1 = (i + 1)** n
                             r1 = ((i + 1) * ((r1 - 1) / i))
                             renta = m / r1
                             print("R=" , renta)                               
                    if (tasa == "semanal"):
                        if (pagos == "trimestral"):
                            i = (i / 100) / 12
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                    if (tasa == "mensual"):
                        if (pagos == "trimestral"):
                            i = (i / 100) / 3
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                    if (tasa == "bimestral"):
                        if (pagos == "trimestral"):
                            i = (i / 100) / 1.5
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)                           
                    if (tasa == "semestral"):
                        if (pagos == "trimestral"):
                            i = (i / 100) * 2
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)                           
                    if (tasa == "anual"):
                        if (pagos == "trimestral"):
                            i = (i / 100) / 4
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)                               
                    if (tasa == "diarios"):
                        if (pagos == "semestral"):
                            i = (i / 100) / 180
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                if convertible2 == "semestral":
                    if (tasa == "quincenal"):
                        if (pagos == "semestral"):
                            i = (i / 100) / 12
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                    if (tasa == "semanal"):
                        if (pagos == "semestral"):
                            i = (i / 100) / 24
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)                           
                    if tasa == "mensual":
                        if pagos == "semestral":
                            i = (i / 100) / 6
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)                           
                    if (tasa == "bimestral"):
                        if (pagos == "semestral"):
                            i = (i / 100) / 3
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                    if (tasa == "trimestral"):
                        if (pagos == "semestral"):
                            i = (i / 100) / 2
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)                           
                    if (tasa == "anual"):
                        if (pagos == "semestral"):
                            i = (i / 100) / 2
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                if (convertible2 == "anual"):
                    if (tasa == "diarios"):
                        if (pagos == "anual"):
                            i = (i / 100) / 360
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                    if (tasa == "quincenal"):
                        if (pagos == "anual"):
                            i = (i / 100) / 24
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)                           
                    if (tasa == "semanal"):
                        if (pagos == "anual"):
                            i = (i / 100) / 52
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                    if (tasa == "mensual"):
                        if (pagos == "anual"):
                            i = (i / 100) / 12
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                    if (tasa == "bimestral"):
                        if (pagos == "anual"):
                            i = (i / 100) / 6
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)    
                    if (tasa == "trimestral"):
                        if (pagos == "anual"):
                            i = (i / 100) / 4
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
                    if (tasa == "semestral"):
                        if (pagos == "anual"):                                   
                            i = (i / 100) / 2
                            r1 = (i + 1)** n
                            r1 = ((i + 1) * ((r1 - 1) / i))
                            renta = m / r1
                            print("R=" , renta)
            else:
                if (tasa == "diarios"):
                    if (pagos == "diarios"):
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                if (tasa == "diarios"):
                    if (pagos == "semanal"):
                        n = n * 7
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "quincenal"):
                        n = n * 14
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "mensual"):
                        n = n * 30
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "bimestral"):
                        n = n * 60
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "trimestral"):
                        n = n * 90
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "semestral"):
                        n = n * 180
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "anual"):
                        n = n * 360
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                if (tasa == "semanal"):
                    if (pagos == "diarios"):
                        n = n / 7
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "semanal"):
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "quincenal"):
                        n = n * 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "mensual"):
                        n = n * 4
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "bimestral"):
                        n = n * 8
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "trimestral"):
                        n = n * 12
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "semestral"):
                        n = n * 24
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "anual"):
                        n = n * 52
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                if (tasa == "quincenal"):
                    if (pagos == "diarios"):
                        n = n / 14
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "semanal"):
                        n = n / 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if pagos == "quincenal":
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "mensual"):
                        n = n * 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "bimestral"):
                        n = n * 4
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "trimestral"):
                        n = n * 6
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "semestral"):
                        n = n * 12
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "anual"):
                        n = n * 24
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)

                if (tasa == "mensual"):
                    if (pagos == "diarios"):
                        n = n / 30
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "semanal"):
                        n = n / 4
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "quincenal"):
                        n = n / 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "mensual"):
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "bimestral"):
                        n = n * 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "trimestral"):
                        n = n * 3
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "semestre"):
                        n = n * 6
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "anual"):
                        n = n * 12
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)

                if (tasa == "bimestral"):
                    if (pagos == "diarios"):
                        n = n / 60
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "semanal"):
                        n = n / 8
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "quincenal"):
                        n = n / 4
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "mensual"):
                        n = n / 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "bimestral"):
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "trimestral"):
                        n = n * 1.5
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "semestre"):
                        n = n * 3
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "anual"):
                        n = n * 6
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                if (tasa == "trimestral"):
                    if (pagos == "diarios"):
                        n = n / 90
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "semanal"):
                        n = n / 12
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "quincenal"):
                        n = n / 6
                        i = (i / 100) / 360
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "mensual"):
                        n = n / 3
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "bimestral"):
                        n = n / 1.5
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "trimestral"):
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "semestral"):
                        n = n * 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "anual"):
                        n = n * 4
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                if (tasa == "semestral"):
                    if (pagos == "diarios" or pagos == "diario"):
                        n = n / 180
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "semanal" or pagos == "semanas"):
                        n = n / 24
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "quincenal"):
                        n = n / 12
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "mensual"):
                        n = n / 6
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "bimestral"):
                        n = n / 3
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "trimestral"):
                        n = n / 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "semestral"):
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "anual"):
                        n = n * 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                if (tasa == "anual"):
                    if (pagos == "diarios"):
                        n = n / 360
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "semanal"):
                        n = n / 52
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "quincenal"):
                        n = n / 24
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "mensual"):
                        n = n / 12
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "bimestral"):
                        n = n / 6
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "trimestral"):
                        n = n / 4
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "semestre"):
                        n = n / 2
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
                    if (pagos == "anual"):
                        i = (i / 100)
                        r1 = ((i + 1) ** n)
                        r1 = ((i + 1) * ((r1 - 1) / i))
                        renta = m / r1
                        print("R=", renta)
    def rentaantcap(self):
        try:
            c = float(input("Ingrese la cantidad de capital "))
            n = float(input("Ingresa el numero de pagos"))
            pagos = input("Escriba como seran los pagos")
            i = float(input("Ingresa la tasa de interes"))
            tasa = input(" Escriba como sera la tasa de interes")
            convertible = input(" ¿La tasa es convertible?")
            if ( convertible == "si"):
               convertible2 = input(" a que tiempo sera convertible  la tasa de interes")
               if (convertible2 == "semanal"):
                   if (tasa == "diarios"):
                       if (pagos == "semanal"):
                           i = (i / 100) / 7;
                           r1 = (i + 1)** -n
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1;
                           print("R=" ,renta)
                   if (tasa == "quincenal"):
                       if (pagos == "semanal"):
                           i = (i / 100) * 2
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=" , renta)
                   if (tasa == "mensual"):
                       if (pagos == "semanal"):
                           i = (i / 100) * 4
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=" , renta)
                   if (tasa == "bimestral"):
                       if (pagos == "semanal"):
                           i = (i / 100) * 8
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=" , renta)
                   if (tasa == "trimestral"):
                       if (pagos == "semanal"):
                           i = (i / 100) * 12
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=" , renta)
                   if (tasa == "semestral"):
                       if (pagos == "semanal"):
                           i = (i / 100) * 24
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=" , renta)
                   if (tasa == "anual"):
                       if (pagos == "semanal"):
                           i = (i / 100) * 52
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=" , renta)
               if (convertible2 == "diario"):
                   if (tasa == "semanal"):
                       if (pagos == "diario"):
                           i = (i / 100) * 7
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "quincenal"):
                       if (pagos == "diario"):
                           i = (i / 100) * 14
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "mensual"):
                       if (pagos == "diario"):
                           i = (i / 100) * 30
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "bimestral"):
                       if (pagos == "diario"):
                           i = (i / 100) * 60
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "trimestral"):
                       if (pagos == "diario"):
                           i = (i / 100) * 90
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "semestral"):
                       if (pagos == "diario"):
                           i = (i / 100) * 180
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "anual"):
                       if (pagos == "diario"):
                           i = (i / 100) / 365
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
               if (convertible2 == "quincenal"):
                   if (tasa == "diarios"):
                       if (pagos == "quincenal"):
                           i = (i / 100) / 14
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "semanal"):
                       if (pagos == "quincenal"):
                           i = (i / 100) / 2
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "mensual"):
                       if (pagos == "quincenal"):
                           i = (i / 100) * 2
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "bimestral"):
                       if (pagos == "quincenal"):
                           i = (i / 100) * 4
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "trimestral"):
                       if (pagos == "quincenal"):
                           i = (i / 100) * 6
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "semestral"):
                       if (pagos == "quincenal"):
                           i = (i / 100) * 12
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "anual"):
                       if (pagos == "quincenal"):
                           i = (i / 100) / 24
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
               if (convertible2 == "mensual"):
                   if (tasa == "diarios"):
                       if (pagos == "mensual"):
                           i = (i / 100) / 30
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "quincenal"):
                       if (pagos == "mensual"):
                           i = (i / 100) / 2
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "semanal"):
                       if (pagos == "mensual"):
                           i = (i / 100) / 4
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "bimestral"):
                       if (pagos == "mensual"):
                           i = (i / 100) * 2
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "trimestral"):
                       if (pagos == "mensual"):
                           i = (i / 100) * 3
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "semestral"):
                       if (pagos == "mensual"):
                           i = (i / 100) * 6
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "anual"):
                       if (pagos == "mensual"):
                           i = (i / 100) / 12
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
               if (convertible2 == "bimestral"):
                   if (tasa == "diarios"):
                       if (pagos == "bimestral"):
                           i = (i / 100) / 60
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "quincenal"):
                       if (pagos == "bimestral"):
                           i = (i / 100) / 4
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "semanal"):
                       if (pagos == "bimestral"):
                           i = (i / 100) / 8
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "mensual"):
                       if (pagos == "bimestral"):
                           i = (i / 100) / 2
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "trimestral"):
                       if (pagos == "bimestral"):
                           i = (i / 100) * 1.5
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "semestral"):
                       if (pagos == "bimestral"):
                           i = (i / 100) * 3
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "anual"):
                       if (pagos == "bimestral"):
                           i = (i / 100) / 6
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
               if (convertible2 == "trimestral"):
                   if (tasa == "diarios"):
                       if (pagos == "trimestral"):
                           i = (i / 100) / 90
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "quincenal"):
                       if (pagos == "trimestral"):
                           i = (i / 100) / 6
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "semanal"):
                       if (pagos == "trimestral"):
                           i = (i / 100) / 12
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "mensual"):
                       if (pagos == "trimestral"):
                           i = (i / 100) / 3
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "bimestral"):
                       if (pagos == "trimestral"):
                           i = (i / 100) / 1.5
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "semestral"):
                       if (pagos == "trimestral"):
                           i = (i / 100) * 2
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "anual"):
                       if (pagos == "trimestral"):
                           i = (i / 100) / 4
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
               if (convertible2 == "semestral"):
                   if (tasa == "diarios"):
                       if (pagos == "semestral"):
                           i = (i / 100) / 180
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "quincenal"):
                       if pagos == "semestral":
                           i = (i / 100) / 12
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "semanal"):
                       if (pagos == "semestral"):
                           i = (i / 100) / 24
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if tasa == "mensual":
                       if pagos == "semestral":
                           i = (i / 100) / 6
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "bimestral"):
                       if (pagos == "semestral"):
                           i = (i / 100) / 3
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if tasa == "trimestral":
                       if pagos == "semestral":
                           i = (i / 100) / 2
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "anual"):
                       if (pagos == "semestral"):
                           i = (i / 100) / 2
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
               if (convertible2 == "anual"):
                   if (tasa == "diarios"):
                       if (pagos == "anual"):
                           i = (i / 100) / 360
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "quincenal"):
                       if (pagos == "anual"):
                           i = (i / 100) / 24
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "semanal"):
                       if (pagos == "anual"):
                           i = (i / 100) / 52
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "mensual"):
                       if (pagos == "anual"):
                           i = (i / 100) / 12
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "bimestral"):
                       if (pagos == "anual"):
                           i = (i / 100) / 6
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "trimestral"):
                       if (pagos == "anual"):
                           i = (i / 100) / 4
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
                   if (tasa == "semestral"):
                       if (pagos == "anual"):
                           i = (i / 100) / 2
                           r1 = ((i + 1) ** -n)
                           r1 = ((i + 1) * ((1 - r1) / i))
                           renta = c / r1
                           print("R=", renta)
            else:
                if (tasa == "diarios"):
                    if (pagos == "diarios"):
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "semanal"):
                        n = n * 7
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "quincenal"):
                        n = n * 14
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "mensual"):
                        n = n * 30
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "bimestral"):
                        n = n * 60
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "trimestral"):
                        n = n * 90
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "semestral"):
                        n = n * 180
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "anual"):
                        n = n * 360
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "semanal"):
                    if (pagos == "diarios"):
                        n = n / 7
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "semanal"):
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "quincenal"):
                        n = n * 2
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "mensual"):
                        n = n * 4
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "bimestral"):
                        n = n * 8
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "trimestral"):
                        n = n * 12
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "semestral"):
                        n = n * 24
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "anual"):
                        n = n * 52
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                if tasa == "quincenal":
                    if pagos == "diarios":
                        n = n / 14
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if pagos == "semanal":
                        n = n / 2
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "quincenal"):
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "mensual"):
                        n = n * 2
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "bimestral"):
                        n = n * 4
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "trimestral"):
                        n = n * 6
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "semestral"):
                        n = n * 12
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "anual"):
                        n = n * 24
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "mensual"):
                    if (pagos == "diarios"):
                        n = n / 30
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "semanal"):
                        n = n / 4
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "quincenal"):
                        n = n / 2
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "mensual"):
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "bimestral"):
                        n = n * 2
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "trimestral"):
                        n = n * 3
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "semestre"):
                        n = n * 6
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "anual"):
                        n = n * 12
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "bimestral"):
                    if (pagos == "diarios" or pagos == "diario"):
                        n = n / 60
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "semanal"):
                        n = n / 8
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "quincenal"):
                        n = n / 4
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "mensual"):
                        n = n / 2
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "bimestral"):
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "trimestral"):
                        n = n * 1.5
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "semestre"):
                        n = n * 3
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "anual"):
                        n = n * 6
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "trimestral"):
                    if (pagos == "diarios"):
                        n = n / 90
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "semanal"):
                        n = n / 12
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "quincenal"):
                        n = n / 6
                        i = (i / 100) / 360
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "mensual"):
                        n = n / 3
                        print("los pagos trimestrales son " + n)
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "bimestral"):
                        n = n / 1.5
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "trimestral"):
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "semestral"):
                        n = n * 2
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "anual"):
                        n = n * 4
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "semestral"):
                    if (pagos == "diarios"):
                        n = n / 180
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                    print("R=", renta)
                    if (pagos == "semanal"):
                        n = n / 24
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                    print("R=", renta)
                    if (pagos == "quincenal"):
                        n = n / 12
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                    print("R=", renta)
                    if (pagos == "mensual"):
                        n = n / 6
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    elif (pagos == "bimestral"):
                        n = n / 3
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if pagos == "trimestral":
                        n = n / 2
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "semestral"):
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "anual"):
                        n = n * 2
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                if (tasa == "anual"):
                    if (pagos == "diarios"):
                        n = n / 360
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "semanal"):
                        n = n / 52
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "quincenal"):
                        n = n / 24
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "mensual"):
                        n = n / 12
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "bimestral"):
                        n = n / 6
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "trimestral"):
                        n = n / 4
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "semestre"):
                        n = n / 2
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)
                    if (pagos == "anual"):
                        i = (i / 100)
                        r1 = ((i + 1) ** -n)
                        r1 = ((i + 1) * ((1 - r1) / i))
                        renta = c / r1
                        print("R=", renta)






        except:
            print("Ingresa un valor valido")








                               

                                       
                              
                                   
                                        












                               


        




















