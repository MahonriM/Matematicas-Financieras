import math
def monto(M):
    c = int(input("Ingresa el capital"))
    i = float(input("Ingresa la tasa de interes"))
    tiempo1=input("Ingresa el tiempo de la tasa de interes ")
    t = float(input("Ingresa el tiempo de la inversion"))
    tiempo = input("Ingresa el periodo o tiempo que desea convertir")
    if tiempo1 == "anual":
        if(tiempo=="anual" or tiempo == "años"):
             M=c*(1+(i/100)*t)
             print("El monto total es ",M)   
        elif(tiempo=="semestral" or tiempo == "semestre"):
             M=c*(i/100)*(t/2)
             print("El monto total es ",M)
        elif(tiempo=="mensual"):
             M = c * (i / 100) * (t / 12)
             print("El monto total es ", M)
        elif(tiempo=="semanal"):
             M=c*(i/100)*(t/52)
             print("El monto total es ", M)
        elif(tiempo=="diario" or tiempo=="dias"):
           M = c * (i / 100) * (t / 360)
           print("El monto total aproximado",M)
           print("El monto total real es :"+ str(c*(i/100)*(t/365)))
        elif tiempo =="trimestre":
            M= c*(i/100)*(t/4)
            print("El monto total es",M)
        elif tiempo == "bimestre" or tiempo =="bimestral":
             M= c*(i/100)*(t/6)
             print("El monto total es",M)
        elif tiempo == "quincenal":
            M = c * (i / 100) * (t / 24)
            print("El monto total es ", M)
    if tiempo1 == tiempo:
        M = c * (1 + (i / 100) * t)
        print("El monto total es ", M)
    if tiempo1=="mensual":
        if tiempo=="semestral":
             M = c * (1 + (i / 100) * t/6)
             print("El monto total es ", M)
        elif tiempo=="trimestral":
             M = c * (1 + (i / 100) * t/3)
             print("El monto total es ", M)
        elif tiempo=="bimestral":
             M = c * (1 + (i / 100) * t/2)
             print("El monto total es ", M)

    return M
def interes(I):
    I = float
    c = int(input("Ingresa el capital"))
    i = float(input("Ingresa la tasa de interes"))
    tiempo1=input("Ingresa el tiempo de la tasa de interes ")
    t = float(input("Ingresa el tiempo de la inversion"))
    tiempo = input("Ingresa el periodo o tiempo que desea convertir")
    if tiempo1 == "anual":
        if tiempo == "anual":
            I = c * (i/100) * t
            print("El interes es", I)
        if tiempo == "mensual":
            I = c * (i / 100) * (t / 12)
            print("El valor del interes mensual es ", I)
        elif (tiempo == "semestral"):
            I = c * (i / 100) * (t / 2)
            print("El valor del interes es", I)
        elif (tiempo=="quincenal"):
            I = c * (i / 100) * (t / 26)
            print("El valor del interes es", I)
        elif (tiempo=="trimestres"):
            I=c*(i/100)*(t/4)
            print("El valor del interes es",I)
        elif(tiempo=="bimestre"):
            I = c * (i / 100) * (t / 6)
            print("El valor del interes es", I)
        elif (tiempo == "semanal"):
            I = c * (i / 100) * (t / 52)
            print("El valor del interes es", I)
        elif (tiempo == "diario"):
            I = c * (i / 100) * (t / 360)
            print("El interes simple aproximado es :", I)
            print("El interes simple real es :" + str(c * i / 100 * t / 365))
    if tiempo1 == "mensual":#Si el tiempo del interes es mensual entonces
        if tiempo == "mensual":#Verificar si es mensual
            I = c * (i/100) * t
            print("El interes es", I)
        if tiempo == "anual":#Si es mensual el interes y el tiempo es anual
            I = c * (i / 100 )* (t*12)
            print("El valor del interes mensual es ", I)
        elif tiempo == "semestral":
            I = c * (i / 100) * (t *6)
            print("El valor del interes es", I)
        elif tiempo == "semanal":
            I = c * (i / 100) * (t/4)
            print("El valor del interes es", I)
        elif tiempo=="quincenal":
            I = c * (i / 100) * (t /2)
            print("El valor del interes es", I)
        elif (tiempo=="trimestres"):
            I=c*(i/100)*(t*3)
        elif(tiempo=="bimestre"):
            I = c * (i / 100) * (t * 2)
            print("El valor del interes es", I)
        elif (tiempo == "diario"):
            I = c * (i / 100) * (t / 30)
            print("El interes simple aproximado es :", I)
    if tiempo1 == "semestral":#Es semestral  
        if tiempo == "mensual":  # Verificar si es mensual
            I = c * (i / 100) * t/6
            print("El interes es", I)
        if tiempo == "anual":  
            I = c * (i / 100) * (t * 2)
            print("El valor del interes mensual es ", I)
        elif tiempo == "semestral":
            I = c * (i / 100) * t
            print("El valor del interes es", I)
        elif tiempo == "semanal":
            I = c * (i / 100) * (t / 26)
            print("El valor del interes es", I)
        elif tiempo == "quincenal":
            I = c * (i / 100) * (t / 13)
            print("El valor del interes es", I)
        elif(tiempo=="bimestre"):
            I = c * (i / 100) * (t /3)
            print("El valor del interes es", I)
        elif tiempo == "trimestres"or tiempo1=="trimestral":
            I = c * (i / 100) * (t /2)
        elif (tiempo == "diario"):
            I = c * (i / 100) * (t / 181)
            print("El interes simple aproximado es :", I)
    if tiempo1=="trimestres" or tiempo1=="trimestral":#Conversion de trimestre
        if tiempo == "trimestres"or tiempo1=="trimestral": # Verificar si es Trimestral
            I = c * (i / 100) * t 
            print("El interes es", I)
        if tiempo == "anual":  
            I = c * (i / 100) * (t * 4)
            print("El valor del interes mensual es ", I)
        elif tiempo == "semestral":
            I = c * (i / 100) * (t*2)#Se multiplica por 2 ya que en un semestre hay 2 trimestres
            print("El valor del interes es", I)
        elif tiempo == "semanal":
            I = c * (i / 100) * (t / 12)
            print("El valor del interes es", I)
        elif tiempo == "quincenal":
            I = c * (i / 100) * (t / 6)
            print("El valor del interes es", I)
        elif (tiempo == "mensual"):
            I = c * (i / 100) * (t /3)
            print("El valor del interes es", I)
        elif (tiempo == "diario"):
            I = c * (i / 100) * (t / 90)
            print("El valor del interes es", I)
        elif(tiempo=="bimestre"):
            I = c * (i / 100) * (t /1.5)
            print("El valor del interes es", I)
    if tiempo1 == "Bimestre"or tiempo1=="bimestre":
        if tiempo == "mensual": # Verificar si es mensual
             I = c * (i / 100) * t/2
             print("El interes es", I)
        elif(tiempo=="bimestre"):#Tiempo es bimestral
              I = c * (i / 100) * t#Realizar el calculo
              print("El valor del interes mensual es ", I)#Impresion del resultado
        if tiempo == "anual": 
             I = c * (i / 100) * (t * 6)
             print("El valor del interes mensual es ", I)
        elif tiempo == "semestral":
             I = c * (i / 100) * (t/ 3) 
             print("El valor del interes es", I)
        elif tiempo == "semanal":
             I = c * (i / 100) * (t/8 )
             print("El valor del interes es", I)
        elif tiempo == "quincenal":
             I = c * (i / 100) * (t / 14)
             print("El valor del interes es", I)
        elif (tiempo == "trimestres"):
             I = c * (i / 100) * (t *1.5)
             print("El valor del interes es", I)
        elif tiempo == "diario":
             I = c * (i / 100) * (t *60)
             print("El interes simple aproximado es :", I)


    

    return I
#Declaracion de la clase tiempo esta clase va a servir para calcular el tiempo en Interes Simple
class tiempointeres():
    def tiempo(self):
        c = int(input("Ingresa el capital"))
        i = float(input("Ingresa la tasa de interes"))
        tiempo1=input("Ingresa el tiempo de la tasa de interes ")
        I = float(input("Ingresa el valor del Interes simple"))
        if tiempo1 == "anual":
            t = I / (i/100 * c)
            print("El tiempo es", I)
        if tiempo1 == "mensual":
            t = (I / (i/100 * c))*12
            print("El valor del tiempo mensual es ", I)
        elif (tiempo1 == "semestral"):
            t = (I / (i/100 * c))*2
            print("El valor del tiempo es", I)
        elif (tiempo1 == "semanal"):
            t = (I / (i * c))*52
            print("El valor del tiempo es", I)
        elif (tiempo1 == "diario"):
            t = (I / ((i/100) * c))*360
            print("El tiempo simple aproximado es :", I)
            print("El tiempo simple real es :" + str(c * i / 100 * t / 365))
        elif tiempo1=="quincenal" or tiempo1=="quincenas":
             t = (I / (i * c))*24
             print("El valor del tiempo es", I)
def tasainteres():
    c=float(input("Ingresa el capital"))
    I= float(input("Ingresa el valor del Interes simple"))
    t = float(input("Ingresa el tiempo de la inversion (t)"))
    tiempo = input("Ingresa el  tiempo o periodo en letra")
    tiempo1=input("Ingresa el tiempo en que deseas la tasa ")
    if tiempo1=="anual":
        if tiempo=="mensual":
            i = I / (c * (t/12))
            print("La tasa de interes es",i)
            print("La tasa de interes en porcentaje es", str(i * 100), "%")
        elif tiempo=="bimestral":
            i = I / (c * (t / 6))
            print("La tasa de interes es", i)
            print("La tasa de interes en porcentaje es", str(i * 100), "%")
        elif tiempo=="trimestral" or tiempo=="trimestre":
            i = I / (c * (t / 4))
            print("La tasa de interes es", i)
            print("La tasa de interes en porcentaje es", str(i * 100), "%")
        elif tiempo=="diario" or tiempo=="dias":
            i = I / (c * (t / 360))
            print("La tasa de interes es", i)
            print("La tasa de interes en porcentaje es", str(i * 100), "%")
        elif tiempo=="quincenal" or tiempo=="quincenas":
            i = I / (c * (t / 24))
            print("La tasa de interes es", i)
            print("La tasa de interes en porcentaje es", str(i * 100), "%")
        elif tiempo=="semanal" or tiempo=="semanas":
            i = I / (c * (t / 52))
            print("La tasa de interes es", i)
            print("La tasa de interes en porcentaje es", str(i * 100), "%")
        elif tiempo=="semestral" or tiempo=="semestres":
            i = I / (c * (t / 2))
            print("La tasa de interes es", i)
            print("La tasa de interes en porcentaje es", str(i * 100), "%")
        elif tiempo=="anual" or tiempo=="años" or tiempo=="año":
            i = I / (c * t )
            print("La tasa de interes es", i)
            print("La tasa de interes en porcentaje es", str(i * 100), "%")
    elif tiempo1=="mensual":
        if tiempo=="diario" or tiempo=="dias":
            i = I / (c * (t/30))
            print("La tasa de interes es", i)
            print("La tasa de interes en porcentaje es",str(i*100),"%")
        elif tiempo=="mensual":
            i = I / (c * t )
            print("La tasa de interes es", i)
            print("La tasa de interes en porcentaje es", str(i * 100), "%")
        elif tiempo=="bimestral" or tiempo=="bimestres":
            i = I / (c * (t / 2))
            print("La tasa de interes es", i)
            print("La tasa de interes en porcentaje es", str(i * 100), "%")
        elif tiempo=="trimestral":
            i = I / (c * (t / 3))
            print("La tasa de interes es", i)
            print("La tasa de interes en porcentaje es", str(i * 100), "%")
        elif tiempo=="quincenal" or tiempo=="quincenas":
            i = I / (c * (t/2))
            print("La tasa de interes es", i)
            print("La tasa de interes en porcentaje es", str(i * 100), "%")
    return i
def capital(c):
    M = int(input("Ingresa el monto"))
    i = float(input("Ingresa la tasa de interes"))
    tiempo1=input("Ingresa el tiempo de la tasa de interes ")
    t = float(input("Ingresa el tiempo de la inversion"))
    tiempo = input("Ingresa el periodo o tiempo que desea convertir")
    if tiempo1==tiempo:
        c = M / (1 + i * t)
        print("El capital total es ", c)
    if tiempo1=="anual":
     if tiempo == "anual":
        c = M / (1 + i * t)
        print("El capital total es ", c)
     elif tiempo == "semestral":
        c = M / ( i / 100 * t / 2)
        print("El capital total es ", c)
     elif tiempo == "mensual":
        c = M / ((i / 100)*(t / 12))
        print("El capital total es ", c)
     elif tiempo == "semanal":
        c = M /(i / 100 * t / 52)
        print("El capital total es ", c)
     elif tiempo =="trimestral":
        c = M / (i / 100 * t / 4)
        print("El capital total es ", c)
     elif tiempo =="quincenal":
         c = M / (i / 100 * t / 24)
         print("El capital total es ", c)
     elif tiempo=="bimestral":
         c = M / (i / 100 * t / 6)
         print("El capital total es ", c)
     elif tiempo == "diario":
        c = M / (i / 100 * t / 360)
        print("El capital total aproximado", c)
        print("El capital total real es :" + str(M/ (i / 100 * t / 365)))
    if tiempo1 == "mensual" or"mes":#mensual
        if tiempo == "mensual":
            c = M / (1 + i * t)
            print("El capital total es ", c)
        elif tiempo == "semestral":
            c = M / (i / 100 * t * 6)
            print("El capital total es ", c)
        elif tiempo == "aual":
            c = M / ((i / 100) * (t * 12))
            print("El capital total es ", c)
        elif tiempo == "semanal":
            c = M / (i / 100 * t / 4)
            print("El capital total es ", c)
        elif tiempo == "trimestral":
            c = M / (i / 100 * t *3)
            print("El capital total es ", c)
        elif tiempo == "quincenal":
            c = M / (i / 100 * t /2 )
            print("El capital total es ", c)
        elif tiempo == "bimestral":
            c = M / (i / 100 * t *2)
            print("El capital total es ", c)
        elif tiempo == "diario" or "dias":
            c = M / (i / 100 * t /30)
            print("El capital total aproximado", c)
    if tiempo1 == "semestral" or "semestre":#semestral
        if tiempo == "semestral":
            c = M / (1 + i * t)
            print("El capital total es ", c)
        elif tiempo == "mensual":
            c = M / (i / 100 * t /6)
            print("El capital total es ", c)
        elif tiempo == "anual":
            c = M / ((i / 100) * (t * 2))
            print("El capital total es ", c)
        elif tiempo == "semanal":
            c = M / (i / 100 * t / 26)
            print("El capital total es ", c)
        elif tiempo == "trimestral":
            c = M / (i / 100 * t /2)
            print("El capital total es ", c)
        elif tiempo == "quincenal":
            c = M / (i / 100 * t / 13)
            print("El capital total es ", c)
        elif tiempo == "bimestral":
            c = M / (i / 100 * t /3)
            print("El capital total es ", c)
        elif tiempo == "diario" or "dias":
            c = M / (i / 100 * t / 181)
            print("El capital total aproximado", c)

    return c








