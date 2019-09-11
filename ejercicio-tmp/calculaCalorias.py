def calculaCalorias(listaDatos): 
    dias = listaDatos.pop()
    genero = listaDatos.pop()
    actividad = listaDatos.pop()
    altura = listaDatos.pop()
    peso = listaDatos.pop()
    edad = listaDatos.pop()
    peso = peso * 10
    altura = altura * 6.25
    edad = edad * 5
    tmb = peso + (altura * edad)
    if genero == "M":
        tmb = tmb - 161
    else: 
        tmb = tmb + 5
#Si no existe actividad física y trabaja sentado:  TMB X 1.2
    if (dias == 0) and (actividad == "B"):
        tmb = tmb * 1.2
#Si realiza ejercicio ligero dos días por semana: TMB X 1.375
    elif (dias == 2) or (dias == 1)  and (actividad == "B"):
        tmb = tmb * 1.375
#Si realiza ejercicio moderado cuatro días por semana: TMB X 1.55
    elif (dias == 4) or (dias == 3)  and (actividad == "M"):
        tmb = tmb * 1.55
#Si hace deporte regular seis días a la semana: TMB X 1.725
    elif (dias == 6) or (dias == 5)  and (actividad == "M"):
        tmb = tmb * 1.55
#Si es deportista de élite o entrena intenso todos los días: TMB X 1.9
    elif (dias == 7)  and (actividad == "A"):
        tmb = tmb * 1.9
    print("Tu TMB es:"+ str(tmb))
    

listaDatos = []
bandera = True

while bandera:
    print("Sistema para medir TMB------------------------------------------------")
    entrada = input("Ingresa su edad: ")
    try:
            edad = int(entrada)
            if (edad > 130) or (edad < 1) or (edad == None):
                print("El valor que ingresaste como EDAD es incorrecto.")
            else:
                entrada = input("Ingresa su peso (en kilogramos): ")
                peso = int(entrada)
                if (peso > 400) or (peso < 1) or (peso == None):
                    print("El valor que ingresaste como PESO es incorrecto.")
                else:
                    entrada = input("Ingresa su altura (en centimetros): ")
                    altura = int(entrada)
                    if (altura > 300) or (altura < 1) or (altura == None):
                        print("El valor que ingresaste como ALTURA es incorrecto.")
                    else:
                        actividad = input("Ingresa tu nivel de actividad (Ingrese 'A' para alto, 'M' para medio y 'B' para bajo):    ").upper()
                        if actividad != "A" or actividad != "M" or actividad != "B":
                            print("Haz ingresado un nivel de actividad invalido")
                        else:
                            genero = input("Ingrese su género: (Ingrese 'M' para másculino 'F' para femenino) ").upper()
                            if genero != "M" or genero != "F":
                                print("Has ingresado un género invalido")
                            else:
                                entrada = input("Ingrese el número de días que ejercita a la semana:  ").upper()
                                dias = int(entrada)
                                if (dias > 7) or (dias < 0) or (dias == None):
                                    print("El valor que ingresaste como días de actividad es incorrecto.")
                                else: 
                                    listaDatos.insert(1,edad)
                                    listaDatos.insert(2,peso)
                                    listaDatos.insert(3, altura)
                                    listaDatos.insert(4,actividad)
                                    listaDatos.insert(5,genero)
                                    listaDatos.insert(6,dias)
                                    calculaCalorias(listaDatos)
    except ValueError:
        print("Dato ingresado no es valido")