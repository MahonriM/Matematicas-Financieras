from ejemploimportacion import *
from ImportacionInteres import *
from anualidades import *
try:
    men=menu()
    men.menu()
    opc=int(input("Que opcion deseas"))
except:
    print("Verifica")
if (opc == 1):
    sub = menu()
    sub.submenuinteressimple()
    oc = int(input("Que opcion deseas"))
    if (oc == 1):
        I = float
        interes(I)
    elif (oc == 2):
        M = float
        monto(M)
    elif (oc == 3):
        c = int
        capital(c)
    elif (oc == 4):
            tiem = tiempointeres()
            tiem.tiempo()
    elif (oc == 5):
        tasainteres()
    elif oc==6:
        print("Gracias por usr el sitema")
if opc == 2:
      sub = menu()
      sub.submenuinterescomp()
      oc = int(input("Que opcion deseas"))
      if (oc == 1):
          compuesto = interesompuesto()
          compuesto.intcompue()
      elif oc == 2:
          mon=interesompuesto()
          mon.montcompu()
      elif oc == 3:
          mon=interesompuesto()
          mon.capitalcomp()
      elif oc == 4:
          per=interesompuesto()
          per.periodocompue()
      elif oc==5:
          per=interesompuesto()
          per.tasacompinte()
if opc == 3:
    sub = menu()
    sub.submenuanualidadesv()
    oc = int(input("Que opcion deseas"))
    if oc == 1:
        anualidades=Anualidadesvenc()
        sub.subsubrenta()
        op = int(input("que opcion deseas"))
        if op == 1:
            anualidades.renta()
        elif op == 2:
            anualidades.vencidasrent()
    elif oc==2:
        anu=Anualidadesvenc()
        anu.capotalven()
    elif oc == 4:
        anualidades = Anualidadesvenc()
        sub.subsubrenta()
        op = int(input("que opcion deseas"))
        if op==1:
            anualidades.numeropagosvenc()
if opc == 4:
    sub=menu()
    sub.submenuanualidadesv()
    oc=int(input("que opcion deseas"))
    if oc == 1:
       renta1=rentaanticipada()
       sub.subsubrenta()
       op = int(input("que opcion deseas"))
       if op == 1:
           renta1.rentaanticipadamon()
       elif op == 2:
          renta1.rentaantcap()
    elif oc==2:
        anu = Anualidadesvenc()
        anu.capanti()














