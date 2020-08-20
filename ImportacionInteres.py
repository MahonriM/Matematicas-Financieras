from math import log10
class menu():
    def menu(self):
        print("Menu de opciones")
        print("1 Interes Simple ")
        print("2 Interes Compuesto")
        print("3 Anualidades vencidas")
        print("4 Anualidades anticipadas")
    def submenuinteressimple(self):
        print("Sub-menu de opciones")
        print("1 Calcular el Interes")
        print("2 Calcular el Monto")
        print("3 Calcular el Capital")
        print("4 Calcular el tiempo")
        print("5 Calcular la tasa de interes")
        print("6 Salir")
    def submenuinterescomp(self):
        print("Sub-menu de opciones")
        print("1 Calcular el Interes")
        print("2 Calcular el Monto")
        print("3 Calcular el Capital")
        print("4 Calcular el periodo")
        print("5 Calcular la tasa de interes")
        print("6 Salir")
    def submenuanualidadesv(self):
        print("1 Renta")
        print("2 Capital")
        print("3 Monto")
        print("4 Periodo")
    def subsubrenta(self):
        print("1 Monto")
        print("2 Capital")
class interesompuesto:#DECLARACION DE LA CLASE Interes compuesto
    def tasacompinte(self):
          try:
              M = float(input("Ingresa el monto"))
              c = float(input("Ingresa el capital"))
              n = float(input("Ingresa el numero de veces que se capitaliza por año"))
              tiep=input("Ingresa el tiempo del periodo")
              timepo1 = input("Ingresa el tiempo  en que desea la tasa de interes")
              tiempo = input("Ingresa la capitalizacion de la tasa")
              if M>0 and c>0 and n>0:
                 if timepo1=="anual":
                     if tiempo=="mensual":
                         if tiep == "anual":
                             n = n*12
                             i= ((M/c)**(1/n))-1
                             print("La Tasa de interes es",i)
                             print("La Tasa de interes en % es",str(i*100),"%")
                         if tiep=="mensual" or tiep=="meses":
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         if tiep=="trimestral" or tiep=="trimestres":
                             n=n*3
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         if tiep=="bimestral"or tiep=="bimestre":
                             n=n*2
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep=="quincenal":
                             n=n/2
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep == "diario" or tiep=="dias":
                             n=n/30
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep =="semanal" or tiep=="semanas":
                             n=n/4
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep == "semestral":
                             n = n *6
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                     if tiempo=="semestral" or tiempo=="semestres":
                         if tiep=="semestral" or tiep=="semestre":
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep=="anual" or tiep=="año":
                             n = n *2
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep=="trimestral" or tiep=="timestre":
                             n = n / 2
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep=="mensual" or tiep=="mes":
                             n = n / 6
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep=="bimestral" or tiep=="bimestre":
                             n = n / 3
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                     elif tiempo=="trimestral" or tiempo=="trimestre":
                         if tiep=="trimestral":
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep =="anual":
                             n = n *4
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep =="mensual":
                             n = n / 3
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep =="semestral" or tiep=="semestre":
                             n = n *2
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep=="bimestral" or tiep=="bimestre":
                             n = n /1.5
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                     elif tiempo=="anual" or tiempo=="año":
                         if tiep=="anual":
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep=="mensual":
                             n = n /12
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep=="trimestral":
                             n = n /4
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep=="bimestral":
                             n = n /6
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep=="quincenal" or tiep=="quincenas":
                             n = n /24
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep=="semanal" or tiep=="semanas":
                             n = n /52
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep=="diario" or tiempo=="dias":
                             n = n /360
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
                         elif tiep=="semestral" or tiep=="semestre":
                             n = n /2
                             i = ((M / c) ** (1 / n)) - 1
                             print("La Tasa de interes es", i)
                             print("La Tasa de interes en % es", str(i * 100), "%")
              else:
                 print("No puedes introducir valores menores a 1")
             
              
          except:
             print("Ha ocurrido un error verifica que uses datos numericos y no de texto")
         



    def periodocompue(self):
        M = float(input("Ingresa el monto"))
        c = float(input("Ingresa el capital"))
        i = float (input("Ingresa la tasa de interes"))
        timepo1 = input("Ingresa el tiempo de la tasa de interes")
        tiempo = input("Ingresa la capitalizacion del tiempo")
        if timepo1 == "anual":
            if tiempo =="semestral":
                n = log10(M/c)/log10((1+(i/100/2)))
                print("El periodo anual es", n)
            elif tiempo == "trimestral" or tiempo == "trimestres":
                n = log10(M/c)/log10((1+(i/100/4)))
                print("El periodo anual es",n)
            elif tiempo == "bimestral":
                n = log10(M/c)/log10((1+(i/100/6)))
                print("El periodo anual es",n)
            elif tiempo == "mensual" or tiempo =="meses":
                n = log10(M/c)/log10((1+(i/100/12)))
                print("El periodo anual es",n)
            elif tiempo == "quincenal":
                n = log10(M/c)/log10((1+(i/100/24)))
                print("El periodo anual es",n)
            elif tiempo =="semanal":
                n = log10(M/c)/log10((1+(i/100/52)))
                print("El periodo anual es",n)
            elif tiempo == "diario" or tiempo == "dias":
                n = log10(M/c)/log10((1+(i/100/360)))
                print("El periodo anual es",n)
        elif timepo1 =="semestral":
            if tiempo == "anual":
             n = log10(M/c)/log10((1+(i/100*2)))
             print("El periodo anual es",n)
            elif tiempo == "semestral":
                n = log10(M/c)/log10((1+(i/100)))
                print("El periodo anual es",n)
            elif tiempo == "trimestral" or tiempo == "trimestres":
                n = log10(M/c)/log10((1+(i/100/2)))
                print("El periodo anual es",n)
            elif tiempo == "bimestral":
                n = log10(M/c)/log10((1+(i/100/3)))
                print("El periodo anual es",n)
            elif tiempo == "mensual" or tiempo =="meses":
                n = log10(M/c)/log10((1+(i/100/6)))
                print("El periodo anual es",n)
            elif tiempo == "quincenal":
                n = log10(M/c)/log10((1+(i/100/12)))
                print("El periodo anual es",n)
            elif tiempo =="semanal":
                n = log10(M/c)/log10((1+(i/100/26)))
                print("El periodo anual es",n)
            elif tiempo == "diario" or tiempo == "dias":
                n = log10(M/c)/log10((1+(i/100/180)))
                print("El periodo anual es",n)
        elif timepo1 == tiempo:
             n = log10(M/c)/log10((1+(i/100)))
             print("El periodo anual es",n)
        elif timepo1 == "trimestral" or timepo1 == "trimestre":
            if tiempo== "anual":
                n = log10(M/c)/log10((1+(i/100*4)))
                print("El periodo anual es",n)
            elif tiempo == "semestral":
                n = log10(M/c)/log10((1+(i/100*2)))
                print("El periodo anual es",n)
            elif tiempo == "bimestral" or tiempo == "bimestres":
                n = log10(M/c)/log10((1+(i/100/1.5)))
                print("El periodo anual es",n)
            elif tiempo == "mensual":
                n = log10(M/c)/log10((1+(i/100/3)))
                print("El periodo anual es",n)
            elif tiempo == "quincenal":
                 n = log10(M/c)/log10((1+(i/100/6)))
                 print("El periodo anual es",n)
            elif tiempo == "semanal" or tiempo == "semanas":
                 n = log10(M/c)/log10((1+(i/100/12)))
                 print("El periodo anual es",n)
            elif tiempo == "diario" or tiempo == "dias":
                 n = log10(M/c)/log10((1+(i/100/90)))
                 print("El periodo anual es",n)
        elif timepo1=="mensual" or timepo1=="meses":
            if tiempo== "anual":
                n = log10(M/c)/log10((1+(i/100*12)))
                print("El periodo anual es",n)
            elif tiempo == "semestral":
                n = log10(M/c)/log10((1+(i/100*6)))
                print("El periodo anual es",n)
            elif tiempo == "bimestral" or tiempo == "bimestres":
                n = log10(M/c)/log10((1+(i/100*2)))
                print("El periodo anual es",n)
            elif tiempo == "mensual":
                n = log10(M/c)/log10((1+(i/100)))
                print("El periodo anual es",n)
            elif tiempo == "quincenal":
                 n = log10(M/c)/log10((1+(i/100/2)))
                 print("El periodo anual es",n)
            elif tiempo == "semanal" or tiempo == "semanas":
                 n = log10(M/c)/log10((1+(i/100/4)))
                 print("El periodo anual es",n)
            elif tiempo == "diario" or tiempo == "dias":
                 n = log10(M/c)/log10((1+(i/100/30)))
                 print("El periodo anual es",n)




    


    def intcompue(self):
        M = int(input("Ingresa el monto"))#Monto
        c=int(input("Ingresa el capital"))#Capital
        print("El valor del interes es"+str(M-c))#resultado
    def montcompu(self):#funcion de la clase monto
        c = float(input("Escriba el capital"))
        i = float(input("Ingresa la tasa de interes"))
        timepo1 = input("Ingresa el tiempo de la tasa de interes")
        tiempo = input("Ingresa la capitalizacion del tiempo")
        n = float(input("Ingresa el numero de veces que se capitaliza por año"))
        tiep=input("Ingresa el tiempo del periodo")
        if timepo1 == "anual":
            if tiempo == "anual" and tiep == "anual":
                M = c * (1 + i/100) ** n
                print("El monto total es ", M)
            elif tiempo == "semestral" and (tiep=="semestral" or tiep == "semestre"):
                M = c * (1 + i / 100/2) ** (n*2)
            elif (tiempo == "mensual"):
                if tiep == "mensual" or tiep == "meses":
                    M = c * (1+ i / 100/12) ** (n)
                    print("El monto total es ", M)
                elif tiep == "anual":
                    M = c * (1+ i / 100/12) ** (n*12)
                    print("El monto total es ", M)
                elif tiep =="diario" or tiep=="diariamente":
                    M = c * (1+ i / 100/12) ** (n*360)
                    print("El monto total es ", M)
            elif tiempo == "semanal":
                M = c * (1+i / 100/52) * (n / 52)
                print("El monto total es ", M)
            elif tiempo == "trimestral":
                M = c * (1 + i / 100/4) * (n / 4)
                print("El monto es"+str(c*i))
            elif (tiempo == "diario" or tiempo == "dias"):
                M = c * (1+i / 100) ** (n / 360)
                print("El monto total aproximado", M)
                print("El monto total real es :" + str(c * (i / 100) * (n / 365)))
            elif tiempo =="bimestral":
                if tiep =="bimestral":
                 M = c * (1+i)/(100/6) **(n /6 )
                 print("El monto total es ", M)
            elif tiempo =="quincenas":
                if tiep=="quincenas":
                  M = c * (1+i / 100/24) * (n /24)
                  print("El monto total es ", M)
        elif timepo1=="mensual":#El tiempo
            if tiempo == "mensual":
                if tiep == "mensual":
                     M = c * (1 + i / 100) ** n
                     print("El monto total es ", M)
                elif tiep == "anual" or tiep =="ANUAL" or tiep=="año".capitalize:
                     M = c * (1 + i / 100) ** (n*12)
                     print("El monto total es ", M)
                elif tiep =="Trimestral" or tiep=="trimestral" or tiep=="trimestres":
                     M = c * (1 + i / 100) ** (n*3)
                     print("El monto total es ", M)
                elif tiep=="bimestral" or tiep=="bimestre" or tiep=="BIMESTRE":
                     M = c * (1 + i / 100) ** (n*2)
                     print("El monto total es ", M)
                elif tiep=="semestral" or tiep=="semestres" or tiep=="semestre":
                     M = c * (1 + i / 100) ** (n*6)
                     print("El monto total es ", M)
                elif tiep=="quincenal" or tiep=="quincenas" or tiep=="quincenal":
                     M = c * (1 + i / 100) ** (n/2)
                     print("El monto total es ", M)
                elif tiep=="diario" or tiep=="dias" or tiep=="dia" or tiep=="diaria":
                     M = c * (1 + i / 100) ** (n/30)
                     print("El monto total es ", M)
            elif tiempo=="anual": 
                if tiep=="anual":
                   M = c * (1 + i / 100*12) ** (n)
                   print("El monto total es ", M)
                if tiep=="mensual" or tiep=="meses" or tiep=="mensual".capitalize:
                     M = c * (1 + i / 100*12) ** (n*12)
                     print("El monto total es ", M)
                elif tiep=="semestral":
                     M = c * (1 + i / 100*12) ** (n/2)
                     print("El monto total es ", M)
                elif tiep=="trimestral":
                     M = c * (1 + i / 100*12) ** (n/4)
                     print("El monto total es ", M)            
            elif tiempo == "bimestre" or tiempo =="bimestral":
                if tiep == "bimestres" or tiep == "bimestral" or tiep=="bimestre":
                     M = c * (1 + i / 100 * 2) ** (n/2)
                     print("El monto es",M)
                elif tiep =="mensual" or tiep=="meses" or tiep=="mes":
                     M = c * (1 + i / 100 * 2) ** (n)
                     print("El monto total es ", M)
                elif tiep =="trimestral" or tiep=="trimestre":
                     M = c * (1 + i / 100 * 2) ** (n*1.5)
                     print("El monto total es ", M)
                elif tiep=="anual":
                     M = c * (1 + i / 100 * 2) ** (n*6)
                     print("El monto total es ", M)
                
        elif (tiempo =="bimestral" or tiep=="bimestres") and (tiep=="Bimestral" or tiep=="bimestres") :
            if timepo1=="diario":
                if tiep=="Bimestral":
                     M = c * (1+i / 60) ** n
            
    def capitalcomp(self):
        M = float(input("Escriba el monto"))
        i = float(input("Ingresa la tasa de interes"))
        timepo1 = input("Ingresa el tiempo de la tasa de interes ")
        tiempo = input("Ingresa la capitalizacion del tiempo")
        n = float(input("Ingresa el numero de veces que se capitaliza por año"))
        tiep = input("Ingresa el tiempo del periodo")
        if timepo1 == "anual":
            if (tiempo == "anual" and tiep == "anual"):
                c = M / (1 + i)**n
                print("El capital total es ", c)
            elif tiempo == "semestral" and (tiep == "semestral" or tiep == "semestre"):
                c = M / (1 + i / 100 / 2) ** n
            elif tiempo == "mensual":
                if tiep=="anual":
                  c = M / (1 + i / 100 / 12) ** (n * 12)
                  print("El capital total es ", c)
                elif tiep=="mensual"or tiep=="meses":
                    c = M / (1 + i / 100 / 12) ** n
                    print("El capital total es ", c)
            elif tiempo == "semanal":
                if tiep == "anual":
                    c = M / (1 + i / 100 / 52) ** (n / 52)
                    print("El capital total es ", c)
                elif tiep=="semanal":
                    c = M / (1 + i / 100 / 52) ** n
                    print("El capital total es ", c)
            elif tiempo == "trimestral" or tiempo =="trimestre" or tiep=="trimestres":
                if tiep =="trimestral" or tiempo =="trimestre" or tiep=="trimestres":
                    print("El capital es" + str(M / (1 + i / 100 /4) ** n))
                elif tiep=="mensual" or tiep =="meses" or tiep=="mes":
                    print("El capital es" + str (M / (1 + i / 100 / 4) ** (n/3)))
            elif tiempo == "Bimestral" or tiempo == "bimestre":
                if tiep == "bimestral" or tiep =="bimestre":
                     print("El capital es" + str( M / (1 + i / 100 /6) ** n))        
            elif tiempo == "quincenal" or tiempo == "quincenas":
                if tiep == "quincenas" or tiep =="quincenal":
                     print("El capital es" + str( M / (1 + i / 100 /24) ** n))
                elif tiep == "anual":
                    print("El capital es" + str( M / (1 + i / 100 /24) ** (n/24)))
            elif tiempo == "diario" or tiempo == "dias":
              print("El capital total es "+ str ( M / (1 + i / 100) ** (n / 360)))
        elif timepo1 == tiempo == tiep:
             c = M / (1 + i)**n
             print("El capital total es ", c)
        elif timepo1 == "mensual" or timepo1=="meses":
            if tiempo == "anual":
                if tiep =="anual":
                 c = M / ((1 + i/12)**(n))
                 print("El capital total es ", c)
            if tiempo=="bimestres" or tiempo=="bimestral":
                if tiep=="mensual" or tiempo=="meses":
                     c = M / ((1 + i/2)**(n))
                     print("El capital total es ", c)
            







                                    
                                
                                    
                                


                            
                            
                            
                                

                                        
                
                   

                
                                      

                            
                 

















