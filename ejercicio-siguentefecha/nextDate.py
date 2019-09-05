import numbers

def calculasiguienteFecha(listaentradas):
    año = listaentradas.pop()
    if (año % 400 == 0):
        año_bisiesto = True
    elif (año % 100 == 0):
        año_bisiesto = False
    elif (año % 4 == 0):
        año_bisiesto = True
    else:
        año_bisiesto = False
    mes  = listaentradas.pop()
    if mes in (1, 3, 5, 7, 8, 10, 12):
        mes_tamanio = 31
    elif mes == 2:
        if año_bisiesto:
            mes_tamanio = 29
        else:
            mes_tamanio = 28
    else:
        mes_tamanio = 30
    dia = listaentradas.pop()
    if dia < mes_tamanio:
        dia += 1
    else:
        dia = 1
        if mes == 12:
            mes = 1
            año += 1
        else:
            mes += 1
    print("La siguiente fecha es: [año/mes/dia]: ["+ str(año)+"/"+str(mes)+"/"+str(dia)+"]")


fecha = []
cont = 0
contador = 0 
bandera = True

while bandera:
    print("Ingresa valores para día, més y año:")
    entrada = input("Ingresa el mes: ")
    try:
        val = int(entrada)
        mes = val
        if (val > 12)  or (val < 1) or (val == None):
            print("Valor del mes no en rango del 1 al 12")
        else:
            entrada = input("Ingresa el día: ")
            val = int(entrada)
            dia = val
            if(val > 31) or ( val < 1) or (val == None):
                print("Valor del día no en rango del 1 al 31")
            else:
                entrada = input("Ingresa el año: ")
                val = int(entrada)
                año = val
                if(val > 2020) or ( val < 1812) or (val == None):
                    print("Valor del año no en rango del 1812 al 2020")
                else:
                    fecha.insert(1,dia)
                    fecha.insert(2,mes)
                    fecha.insert(3,año)
                    calculasiguienteFecha(fecha)
                    bandera = False
    except ValueError:
            print("Dato ingresado no es valido")